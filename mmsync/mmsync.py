#!/usr/bin/python

import argparse

import os
import shutil
import datetime

from .dbRhythmBox import RBox
from .dbPlayerPro import PPro
from .dbItunes import iTun


def main():
    """ The main function: reads the command line arguments and execute the core instructions."""
    parser = create_parser()
    args = parser.parse_args()
    sync(args)


def create_parser():
    """ Create the argument parser: doing this way it's easier to test."""
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', choices=('rb2pp', 'pp2rb', 'it2rb'), dest='action',
                        help='choose the sync direction: rb = Rhythmbox, pp = PlayerPro, it = iTunes')
    parser.add_argument('-rb', '--rhythmbox', required=True, help='the Rhythmbox database xml file')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-pp', '--playerpro', help='the PlayePro database xml file')
    group.add_argument('-it', '--itunes', help='the iTunes database xml file')
    parser.add_argument('--reset-playcounts', action='store_true',
                        help='reset the playcounts instead of accumulating them')
    return parser


def sync(args):
    """ The core function:
    1. read the metadata information from the source
    2. use metadata to update the information on the target
    3. save results
    """
    xml_source, xml_target = define_source_and_target_databases(args)
    songs_and_meta = extract_songs_metadata(xml_source)
    update_songs_metadata(xml_target, songs_and_meta, args)
    save_results(xml_target, args)


def define_source_and_target_databases(args):
    """ Define the source and target databases base on the chosen action."""
    if args.action == 'rb2pp':
        print('Sync: Rhythmbox --> PlayerPro')
        xml_source = RBox(args.rhythmbox)
        xml_target = PPro(args.playerpro)
    elif args.action == 'pp2rb':
        print('Sync: PlayerPro --> Rhythmbox')
        xml_source = PPro(args.playerpro)
        xml_target = RBox(args.rhythmbox)
    elif args.action == 'it2rb':
        print('Sync: iTunes --> Rhythmbox')
        xml_source = iTun(args.itunes)
        xml_target = RBox(args.rhythmbox)
    print('DB1: {}'.format(xml_source.filename))
    print('DB2: {}'.format(xml_target.filename))

    return xml_source, xml_target


def extract_songs_metadata(xml_source):
    """ Create the dictionary containing the music metadata."""
    songs_and_meta = {}
    for song in xml_source.get_all_songs():
        # a tuple of (artist, album, title)
        key = xml_source.get_aat(song)

        # read rating
        rating = '0'
        rating_el = xml_source.get_rating(song)
        if rating_el is not None and rating_el.text is not None:
            rating = rating_el.text

        # read playcount
        playcount = '0'
        playcount_el = xml_source.get_playcount(song)
        if playcount_el is not None and playcount_el.text is not None:
            playcount = playcount_el.text

        # add new item to the dictionary
        songs_and_meta[key] = {'rating': rating, 'playcount': playcount}

    return songs_and_meta


def update_songs_metadata(xml_target, songs_and_meta, args):
    """ Use metadata to update the information on the target database."""
    for song in xml_target.get_all_songs():
        key = xml_target.get_aat(song)
        if key in songs_and_meta:
            # update rating
            new_rating = songs_and_meta[key]['rating']
            old_rating = xml_target.get_rating(song)
            if old_rating is not None:
                old_rating.text = new_rating
            else:
                xml_target.add_rating(song, new_rating)

            # update playcount
            new_playcount = songs_and_meta[key]['playcount']
            old_playcount = xml_target.get_playcount(song)
            if old_playcount is not None:
                if args.reset_playcounts or old_playcount.text is None:
                    old_playcount.text = new_playcount
                else:
                    old_playcount.text = str(int(old_playcount.text) + int(new_playcount))
            else:
                xml_target.add_playcount(song, new_playcount)


def save_results(xml_target, args):
    """ Write down the updated database as an xml file."""
    now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    new_db = ''
    if args.action == 'pp2rb' or args.action == 'it2rb':
        new_db = args.rhythmbox
        backup_db = new_db.replace('.xml', '_backup_{}.xml'.format(now))
        shutil.copyfile(new_db, backup_db)
        print('Backup: {}'.format(backup_db))
    elif args.action == 'rb2pp':
        PP_path = os.path.dirname(args.playerpro)
        new_db = os.path.join(PP_path, 'PlayerPro_{}.xml'.format(now))

    xml_target.write(new_db)
    print('...')
    print('New database: {}'.format(new_db))

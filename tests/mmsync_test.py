import mmsync.mmsync as mmsync
import unittest

import datetime
import filecmp
import glob
import os
import shutil


class MmsyncTest(unittest.TestCase):

    def tearDown(self):
        file_to_remove = glob.glob('PlayerPro*')
        file_to_remove.extend(glob.glob('rhythmdb*'))
        for file in file_to_remove:
            os.remove(file)

    def test_sync_with_empty_args(self):
        with self.assertRaises(SystemExit):
            mmsync.create_parser().parse_args([])

    def test_sync_rhythmbox_2_playerpro(self):
        args = mmsync.create_parser().parse_args(
            ['-rb', 'test_data_rhythmdb_source.xml',
             '-pp', 'test_data_playerpro_target.xml',
             '-a', 'rb2pp'])
        mmsync.mmsync(args)
        output = 'PlayerPro_' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.xml'
        self.assertTrue(filecmp.cmp(output, 'test_result_rb2pp.xml'))

    def test_sync_playerpro_2_rhythmbox(self):
        shutil.copy('test_data_rhythmdb_source.xml', 'rhythmdb.xml')
        args = mmsync.create_parser().parse_args(
            ['-rb', 'rhythmdb.xml',
             '-pp', 'test_data_playerpro_source.xml',
             '-a', 'pp2rb'])
        mmsync.mmsync(args)
        self.assertTrue(filecmp.cmp('rhythmdb.xml', 'test_result_pp2rb.xml'))

    def test_sync_itunes_2_rhythmbox(self):
        shutil.copy('test_data_rhythmdb_source.xml', 'rhythmdb.xml')
        args = mmsync.create_parser().parse_args(
            ['-rb', 'rhythmdb.xml',
             '-it', 'test_data_iTunes_source.xml',
             '-a', 'it2rb'])
        mmsync.mmsync(args)
        self.assertTrue(filecmp.cmp('rhythmdb.xml', 'test_result_it2rb.xml'))

if __name__ == '__main__':
    unittest.ma
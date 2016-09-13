# mmsync
**MusicMetaSync**: sync music metadata between Rhythmbox and PlayerPro.

## What?

I love to have my music library in iTunes and syncing it to my iPod. And by syncing I mean rate a song on my Ipod and find the same rating in iTunes and viceversa. It's a great way to sort and organize your music.

Well, this tool aims to do (almost) the same in Linux, by replacing iTunes with [Rhythmbox](https://wiki.gnome.org/Apps/Rhythmbox/) and the Ipod with an android based device running [PlayerPro](https://play.google.com/store/apps/details?id=com.tbig.playerpro).

## How?

Syncing the music files it's easy, you can use several tools for this task: rsync, [Syncthing](https://syncthing.net/), [Resilio](https://www.resilio.com/), etc. Once you choose your way, you have you music library (or part of it) on both your pc and your android device.

But what about metadata? What about **ratings and playcounts**? For those you can use mmsync.

With mmsync you can import/export ratings and playcounts between Rhythmbox and PlayerPro. And if you already have your music library in iTunes you can use mmsync to import your data from iTunes to Rhythmbox.

### More details

...

## Installation

mmsync is a command line tool written in python. To install it clone the repository and use pip:
```
$ git clone https://github.com/mafffigo/mmsync
$ cd mmsync
$ pip install .
```

## Usage

### Basic

Once installed with pip you should be able to call mmsync directly from the terminal:

#### Get help

```
$ mmsync -h
```

#### Sync: Rhythmbox --> PlayerPro

```
$ mmsync -rb path/to/your/rhythmdb.xml --pp path/to/your/playerprodb.xml -a rb2pp 
```

#### Sync: PlayerPro --> Rhythmbox

```
$ mmsync -rb path/to/your/rhythmdb.xml --pp path/to/your/playerprodb.xml -a pp2rb 
```

## License

The source code is licensed under GPL v3. License is available [here](/LICENSE).

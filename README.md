# mmsync
Music Meta Sync: sync music metadata between iTunes (Read only), Rhythmbox and PlayerPro.

What you can do:
- import ratings and playcounts from iTunes to Rhythmbox
- import/export ratings and playcounts between Rhythmbox (linux) and PlayerPro (android)

## Installation

Clone the repository and install using pip
```
$ git clone https://github.com/mafffigo/mmsync
$ cd mmsync
$ pip install .
```

## Usage

```
$ mmsync --help
usage: mmsync [-h] [-a {rb2pp,pp2rb,it2rb}] -rb RHYTHMBOX
              [-pp PLAYERPRO | -it ITUNES] [--reset-playcounts]

optional arguments:
  -h, --help            show this help message and exit
  -a {rb2pp,pp2rb,it2rb}
                        choose the sync direction: rb = Rhythmbox, pp =
                        PlayerPro, it = iTunes
  -rb RHYTHMBOX, --rhythmbox RHYTHMBOX
                        the Rhythmbox database xml file
  -pp PLAYERPRO, --playerpro PLAYERPRO
                        the PlayePro database xml file
  -it ITUNES, --itunes ITUNES
                        the iTunes database xml file
  --reset-playcounts    reset the playcounts instead of accumulating them
```

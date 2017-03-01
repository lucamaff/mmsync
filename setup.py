from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='mmsync',
    version=version,
    description='Music Meta Sync: sync music metadata between iTunes, Rhythmbox and PlayerPro',
    author='Luca Maff',
    author_email='mafffigo@gmail.com',
    url='https://github.com/mafffigo/mmsync',
    download_url = 'https://github.com/mafffigo/mmsync/archive/' + version + '.tar.gz',
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points = {
        'console_scripts': ['mmsync=mmsync.command_line:main'],
    }
)

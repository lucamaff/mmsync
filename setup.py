from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mmsync',
    version='0.1.0',
    description='Music Meta Sync: sync music metadata between iTunes, Rhythmbox and PlayerPro',
    long_description=readme,
    author='Luca Maffenini',
    author_email='lucamaffen@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points = {
        'console_scripts': ['mmsync=mmsync.command_line:main'],
    }
)

# medialibs
Puts Media files to certain folders from their media tags, for example, if the song's creator is foo and the album name bar itll store all of its songs in /foo/bar/Song1.flac.


# Getting started
0: Download this program/script 

1: Install all requirements. Python can be get [here](https://python.org/) and you can install TinyTag using pip3.

2: Install tinytag using `pip3 install tinytag`


# Usage:
1: Place music in an folder.

2: Copy path.

3: Paste in program.

4: Let the program do the magic.

---
### or alternatively:
---
1: Open up an command prompt/terminal window

2: `cd` into the directory the program is downloaded to.

3: Execute the program as followed: `python3 main.py <path of folder here> <--verbose if required>`

#### This depends on python being as as PATH! If you installed python and didn't do that, click [here](https://docs.python.org/3/using/windows.html) (windows only)

---

Note: If the Song has no media tags or the file isnt media at all, itll store it in UNKNOWN/UNKNOWN.


# Bugs:

~~-Shows permission denied errors, but theyre safe and dont do anything.~~ Fixed!

~~-Only OGG and FLAC supported at this moment, MP3 and more coming soon...?~~ Support added!

# Requirements:

~~-Mutagen~~ we moved to tinytag!

-Python 3

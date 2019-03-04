# medialibs
Puts Media files to certain folders from their media tags, for example, if the song's creator is foo and the album name bar itll store all of its songs in /foo/bar/Song1.flac.


# Usage:
-1: Install all requirements. Python can be get [here](https://python.org/) and you can install TinyTag using pip3.

0: Install tinytag using `pip3 install tinytag`

1: Place music in an folder.

2: Copy path.

3: Paste in program.

4: Let the program do the magic.


Note: If the Song has no media tags or the file isnt media at all, itll store it in UNKNOWN/UNKNOWN.


# Bugs:

~~-Shows permission denied errors, but theyre safe and dont do anything.~~ Fixed!

~~-Only OGG and FLAC supported at this moment, MP3 and more coming soon...?~~ Support added!

# Requirements:

~~-Mutagen~~ we moved to tinytag!

-Python 3

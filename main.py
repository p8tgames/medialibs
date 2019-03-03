import mutagen
import os
import sys

print(sys.argv)
launchargs = sys.argv

if len(launchargs)==1:
    launchargs.append("")
elif len(launchargs)==2:
    launchargs.append("--normal")

if launchargs[1]=="":
    print("Permission denied errors are normal here, they show up when an folder already exists. They can be safely ignored. If you found a fix to hide this, please make a PR.")
    print("Do not use Windows' style of paths! Instead use /, for example (if file is on your windows disk) /path/to/file/")

def start():
    if launchargs[1]!="":
        sourcedir = launchargs[1]
    else:
        sourcedir = input("Enter the Source Directory of your Music files (if folder contains File without Media Tags, itll get stored at root of save dir): ")
    if sourcedir.endswith("/"):
        pass
    else:
        sourcedir = sourcedir + "/"
    try:
        musiclistdir = os.listdir(sourcedir)
        print("Going to process these files: ")
        for abc in musiclistdir:
            try:
                if os.path.isdir(sourcedir + abc):
                    musiclistdir.remove(abc)
                    pass
                else:

                    print("---------------------------------------")
                    print("File Name: {}".format(abc))
                    print(sourcedir+abc)
                    file = mutagen.File(sourcedir+abc)
                    try:
                        artistname = file['artist']
                        albumname = file['album']
                    except Exception:
                        print("I wasn't able to fetch tags. Ill declare them as UNKNOWN here.")
                        artistname = ["UNKNOWN"]
                        albumname = ["UNKNOWN"]
                    print('{} by {}'.format(albumname[0], artistname[0]))
            except PermissionError:
                print("Folder exists, skipping...")
                musiclistdir.remove(abc)
                pass
    except NotADirectoryError:
        print("The program could not find the dir you specified. Is it entered correctly?????????")
        print(Exception)
        start()
    listoftracks = len(sourcedir)
    if launchargs[1]=="":
        print("Are you sure you want to move these files listed above?")
        inp2 = input("Enter 'YES' to proceed.")
        if inp2 == "YES":
            oeufstart(musiclistdir, listoftracks, sourcedir)
        elif inp2 == "yes":
            print("DO NOT TYPE IT IN LOWERCASE IDIOT")
        elif inp2 == "y":
            print("DONT TYPE y ONLY YOU LAZY IDIOT")
        else:
            print("LMAO NERD DIDNT TYPE YES")
    else:
        oeufstart(musiclistdir, listoftracks, sourcedir)

def oeufstart(filedir, dilenr, direc):
    print("Passed succ")
    #print(filedir)
    #print(dilenr)
    for ded in filedir:
        if "." not in ded:
            filedir.remove(ded)
            pass
        else:
            #print("2")debug crap
            file = mutagen.File(direc + ded)
            try:
                artistname = file['artist']
                albumname = file['album']
            except Exception:
                artistname = ["UNKNOWN"]
                albumname = ["UNKNOWN"]
            gonnamake = direc + artistname[0] + "/" + albumname[0] + "/"
            try:
                os.makedirs(gonnamake)
                os.rename(direc + ded, gonnamake + ded)
                #os.makedirs(direc + "lol") was fro debugging
            except FileExistsError:
                if launchargs[2]=="--verbose":
                    print("Skipped {} as it already existed.".format(gonnamake))
                try:
                    os.rename(direc + ded, gonnamake + ded)
                except Exception:
                    if launchargs[2] == "--verbose":
                        print("Skipped {} as it already existed".format(ded))


start()
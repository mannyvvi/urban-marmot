#!/usr/bin/env python
from shutil import copyfile
import os

def Backup(filelist,backuppath):
    for file in filelist:
        filepath = os.path.dirname(os.path.realpath(file))
        backuppath = backuppath + file
        if os.path.exists(filepath):
            print "Got it!"
            print file
            #copyfile(filepath,backuppath)
            print "Backup created"
            
        else:
            print "Not found"
        



def Get_Filelist(filename):
    file = open(filename,"r")
    filelist = file.readlines()
    print filelist
    global filelist
    file.close()

Get_Filelist("FileList.txt")
Backup(filelist,"/Backup Folder/")


#!/usr/bin/python3
import os

dir1 = raw_input("Insert source directory: ")
dir2 = raw_input("Insert destination directory: ")

if dir1[len(dir1)-1] != r"/":
	dir1 += r"/"
if dir2[len(dir2)-1] != r"/":
	dir2 += r"/"


os.system("ls " + dir1 + " > list.txt")

with open("list.txt", "r") as f:
    linee = f.readlines()
    for s in linee:
        print()
        
        if s[len(s)-1] == '\n':
            s = s[0 : len(s)-1]
            
        print("Copying %s ..." %s)
        name= '\"'+s+'\"'
        
        if os.path.isdir(dir1 + s):
            command = "cp -R " + dir1 + name + " " + dir2 + name
        else:
            command = "cp " + dir1 + name + " " + dir2 + name

        #print("%s" %command)
        os.system(command)
        os.system("echo -e '\e[92m\e[1mDONE!!!'")
        os.system("echo -e '\e[0m'")

os.system("rm list.txt")

#import pygame
import os
import sys

from baltie_file_parser import LoadBPRFile, LoadBankFile

argc = len(sys.argv)
print(os.listdir("res/",))
print(argc)
if argc <= 1:
    print("Please select input file.")
    quit()
    
program = LoadBPRFile(sys.argv[argc-1])
if program == 0:
    print("Incorrect file format!")
elif program == 1:
    print("This file version is unsupported!")
elif program == 2:
    print("The file is corrupted!")
else:
    print("File loaded successfully!")
    print(program)
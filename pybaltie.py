#import pygame
import os
import sys
#import GMStuff
from baltie_file_parser import LoadBPRFile, LoadBankFile
import baltie_lib


argc = len(sys.argv)
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
    for i in range(program["blockcount"]):
        #print(int.from_bytes(program["program"][i][:1], byteorder='big'),int.from_bytes(program["program"][i][1:2], byteorder='big'),int.from_bytes(program["program"][i][2:3], byteorder='big'),int.from_bytes(program["program"][i][3:4], byteorder='big'))
        try:
            print(str(i+1)+".",baltie_lib.getInstruction(int.from_bytes(program["program"][i], byteorder='little')))
        except KeyError:
            print(str(i+1)+".","Unknown")
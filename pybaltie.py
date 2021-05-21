from tkinter.constants import NUMERIC
import pygame
import PySimpleGUI as sg

from baltie_file_parser import LoadBPRFile, LoadBankFile

from PySimpleGUI.PySimpleGUI import InputText

sg.theme('Dark')

layout1 =   [
            [sg.Text("PyBaltie"),sg.Image(filename="res/img/pybaltie_small.png")],
            [sg.FileBrowse("Load File",k="file"),sg.Button("Ok")]
            ]

window = sg.Window("PyBaltie",layout1,size=(640,480),icon="res/img/pybaltie.ico",titlebar_icon="res/img/pybaltie.ico")

while True:

    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
	    break
    if event == "Ok":
        if values["file"] == '':
            sg.Popup(f"Please select a file!")
        else:
            if LoadBPRFile(values["file"]) == 0:
                sg.Popup(f"Incorrect file format!")
            elif LoadBPRFile(values["file"]) == 1:
                sg.Popup(f"This file version is unsupported!")
            elif LoadBPRFile(values["file"]) == 2:
                sg.Popup(f"The file is corrupted!")
            else:
                program = LoadBPRFile(values["file"])
                sg.Popup(f"File loaded successfully!")
                print(program)
            print(LoadBankFile(values["file"]))
        

window.close()
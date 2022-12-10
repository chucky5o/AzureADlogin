import os
import easygui

import os

invalidchar = ['~', "#", "%", "&", "*", "}", "{", "<", ">", "?", "+", ]

# simple version for working with CWDx
# path joining version for other paths
DIR = easygui.diropenbox("Choose directory", "")

# create file to be evaluated
x = open(easygui.filesavebox(msg='Save file.', default='document.txt', filetypes=['*.txt', '*.csv']), 'w')

for root, directories, filenames in os.walk(DIR):
    for directory in directories:

        if len(os.path.join(root, directory)) > 255:
            print(os.path.join(root, directory), len(os.path.join(root, directory)))
            x.write(os.path.join(root, directory) + "   " + str(len(os.path.join(root, directory))) + "\n")

x.close()

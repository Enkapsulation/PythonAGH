#!/usr/bin/python3
import os, os.path

#Count a number of file in /dev directory
folder_name = '/dev'
print(len([name for name in os.listdir(folder_name)]))


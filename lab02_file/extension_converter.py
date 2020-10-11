#!/usr/bin/python3
from PIL import Image
from os import listdir
from os.path import splitext

direcotry = 'ConvertTest/'
target = '.png'

#function to covert jpg extension to png extension
for file in listdir(direcotry):
    filename, extension = splitext(file)
    try:
        if extension in ['.jpg', '.jpeg']:
            im = Image.open(direcotry + filename + extension)
            im.save(direcotry + filename + target, "PNG")
    except OSError:
        print(f'Error, can not convert file {file}')

        
    
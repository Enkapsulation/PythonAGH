#!/usr/bin/python3
import shutil
import re
from typing import List

temporaryText: List[str] = []
tmpLine: List[str] = []

def parse_and_change(filename):
    '''
    Method to change a specific word in file.
    '''
    #create copy of file 
    src=filename
    dst=filename + ".copy"
    shutil.copy(src,dst)

    try:
        #read input file
        with open(filename, "r", encoding='utf8') as fdin:
            for line in fdin:
                #replace all occurrences of the required string
                line = re.sub(r'\band\b', 'as well as', line)
                line = re.sub(temp, 'and', line)
                line = re.sub(r'\bnever\b', 'almost never', line)
                line = re.sub(r'\bwhy\b', 'czemu', line)
                temporaryText.append(line)
    
        
        #open the input file in write mode
        with open(filename, 'w+') as fdout:
            for line in temporaryText:
                fdout.write(line)
    except:
        raise "[-]Error: Can't open or save file"
                

def test():
    filename = input("Filename to parse: ")
    parse_and_change(filename)


if __name__ == "__main__":
    test()
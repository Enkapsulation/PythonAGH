#!/usr/bin/python3
import shutil

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
        f = open(filename, "rt")
        
        #read file contents to string
        data = f.read()
        
        #replace all occurrences of the required string
        data = data.replace('and', 'as well as')
        data = data.replace('never', 'almost never')
        data = data.replace('why', 'czemu')
        
        #close the input file
        f.close()
        
        #open the input file in write mode
        f = open(filename, "wt")
        
        #overrite the input file with the resulting data
        f.write(data)
        
        #close the file
        f.close()
    except:
        raise "[-]Error: Can't open or save file"
                

def test():
    filename = input("Filename to parse: ")
    parse_and_change(filename)


if __name__ == "__main__":
    test()
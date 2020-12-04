#!/usr/bin/python3
import shutil

def parse_and_delete(filename):
    '''
    Method to delete a specific word from file.
    '''
    #create copy of file 
    src=filename
    dst=filename + ".copy"
    shutil.copy(src,dst)

    #word to delete
    delete_list = ["and", "never", "why", "self"]
    try:
        #read input file
        f = open(filename,'r')
        
        lst = []
        for line in f:
            for word in delete_list:
                if word in line:         
                    line = line.replace(word,'')
            lst.append(line)
            
        f.close()
        #open the input file in write mode
        f = open(filename,'w')

        #overrite the input file with the resulting data
        for line in lst: 
            f.write(line)
        f.close()
    except:
        raise "[-]Error: Can't open or save file"
                

def test():
    filename = input("Filename to parse: ")
    parse_and_delete(filename)


if __name__ == "__main__":
    test()
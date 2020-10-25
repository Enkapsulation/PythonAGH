#!/usr/bin/python3
import os

def list_files(start_path):
    for root, dir, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * ( level + 1)
        for f in files:
            print("{}{}".format(subindent, f))

def main():
    #directory_name = input("Directory to parse: ")
    directory_name = "/home/jarek/Pulpit/PythonAGH"
    list_files(directory_name)

if __name__ == "__main__":
    main()
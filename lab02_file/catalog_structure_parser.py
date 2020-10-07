#!/usr/bin/python3
import os

def parse_directory(directory_name):
    if os.path.isdir(directory_name):
        os.listdir(directory_name)
        parse_directory()
    

def main():
    directory_name = input("Directory to parse: ")

if __name__ == "__main__":
    main()
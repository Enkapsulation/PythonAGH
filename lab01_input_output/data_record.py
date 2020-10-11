#!/usr/bin/python3
import hashlib
import os

file_path = "secret_password"

def save_password():
    """
        Method to create a hash from user input and save it in file.
     """
    user_cipher = input("Please input your cipher code: ")

    #Create hash
    user_cipher_hash = hashlib.sha256(str.encode(user_cipher)).hexdigest()

    #open file and save password hash 
    fd = open(file_path, "w")
    fd.write(user_cipher_hash)
    fd.close


def check_password():
    """ 
        Method to create a hash from user input 
    """
    user_input = input("Input password:")

    #create hash
    user_input_hash = hashlib.sha256(str.encode(user_input)).hexdigest()

    #return hash from user input
    return user_input_hash


def Test():
    while 1:
        #Check whether secret password exists 
        if 0 == os.stat(file_path).st_size:
            
            #if no, we create new secret password
            save_password()

        else:
            user_password = check_password()

            #open file and read secret password
            fd = open(file_path, "r")
            secret_cipher = fd.read()
            fd.close

            #check hash value of secret cipher in file and user input 
            if secret_cipher == user_password:
                print("Correct password!")
                break
            else:
                print("Wrong password, try again")


if __name__ == "__main__":
    Test()



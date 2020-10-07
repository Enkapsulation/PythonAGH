#!/usr/bin/python3

class Person:
    def __init__(self, name, surname, birth_date):
        self.name = name
        self.surname = surname
        self.birth = birth_date
    
    def introduce(self):
        print(f'Your name is: {self.name}, surname: {self.surname} and your date birth: {self.birth}')

def main():
    # Take parameters from user
    name, surname, birth_date = input("Please type your name, surname and birth date: "). split()

    #create object
    person = Person(name, surname, birth_date)

    #show personal data
    person.introduce()

if __name__ == "__main__":
    main()
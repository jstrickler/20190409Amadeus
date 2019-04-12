#!/usr/bin/env python
FILE_NAME = 'DATA/wombat.txt'

class AmadeusError(Exception):
    pass


def main():
    read_file()
    print_numerical_results()
    try_amadeus()

def read_file():
    try:
        with open(FILE_NAME) as file_in:
            for line in file_in:
                print(line, end='')
    except FileNotFoundError as err:
        print(err)

def print_numerical_results():
    values = 5, 8, 0, 9, "ABC", 4
    for value in values:
        try:
            result = 26 / value
        except Exception as err:
            print(err)
        else:
            print(result)

def raise_amadeus():
    print("Hello")
    raise AmadeusError("THIS IS A TEST")

def try_amadeus():
    try:
        raise_amadeus()
    except AmadeusError as err:
        print(err)



if __name__ == '__main__':
    main()

#!/usr/bin/python3
""" This is a  beautiful code that passes the pycodestyle checks. """

val = int(input("Write any number of your choice: "))


def print_int(val):
    """ Takes int from user and prints it on the std output """
    print("Your choice of number is {}".format(val))


print_int(val)

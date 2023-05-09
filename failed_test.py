#!/usr/bin/python3
""" This code passes the pycodestyle checks. """


def sort_func(list_of_int):
    """ This function sorts a list of integers """

   # str(list_of_int)
    if len(list_of_int) == 1:
        return list_of_int
    count = 0
    while count >= 0:
        count = 0
        i = 1
        for num in list_of_int:
            if num[i] < num[i - 1]:
                num[i - 1], num[i] = num[i], num[i - 1]
                count += 1
        if count == 0:
            return list_of_int


my_list = ["1", "2", "5", "4", "3", "8", "7"]
print(my_list)
print(sort_func(my_list))

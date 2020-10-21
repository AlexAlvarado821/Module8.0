"""
Author: Alex Alvarado
Program: set_membership.py
Date: 10-18-20
Description: Returns a value inside of a set
"""


def in_set(some_set, some_value):
    """
    :param some_set: Provided set
    :param some_value: A value potentially in the set
    :return: Boolean: whether or not some_value is in some_set
    """
    return some_value in some_set

if __name__ == '__main__':
    print(in_set([1,2,3], 3))




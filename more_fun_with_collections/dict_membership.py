"""
Author: Alex Alvarado
Program: dict_membership.py
Date: 10 - 17 - 20
Description:
"""


def in_dict(value):
    """
    :param value: the target value that will be searched for in the dictionary
    :return: returns whether or not value was in the dictionary
    """
    my_dict =  {1: True,
                2: True,
                3: True,
                4: True,
                5: True}
    # if found the the dict should return true for every value

    result = my_dict.get(value, False)
    return result


if __name__ == '__main__':
    print(in_dict(-1))








"""
Author: Alex Alvarado
Program: assign_average.py
Date: 10-18-20
Description: Assigns a message to every grade entered.
"""



def switch_average(entry):
    """
    :param entry: The letter grade entered
    :return: returns the assigned message from the dictionary
    """

    switcher = {
        'A': 'You entered an A!',
        'B': 'You entered a B!',
        'C': 'You entered a C!',
        'D': 'You entered a D!',
        'F': 'You entered a F!'
    }
    return switcher.get(entry, "This is not a valid grade")
    #in case no value is found the code above will return a message as to not cause an error.

if __name__ == '__main__':

    print(switch_average('A'))



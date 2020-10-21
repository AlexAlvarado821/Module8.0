"""
Author: Alex Alvarado
Program: update_scores_dict.py
Date: 10-17-20
Description: Accepts a set amount of scores and calculates the average of the scores.
"""

MAX = 100
MIN = 0

def get_test_scores():
    """
    :return: returns a dictionary with the scores
    """
    scores_dict = dict()
    try:
        num_scores = int(input("How many scores would you like to enter: "))
        if MIN > num_scores:
            raise ValueError
    except ValueError:
        raise ValueError

    for num in range(num_scores):
        flag = False
        while not flag:
            try:

                your_score = float(input("Enter score {} ".format(num+1)))
                if MIN < your_score <= MAX:
                    scores_dict.update({str(num):your_score})
                    flag = True
                else:
                    raise ValueError
            except ValueError:
                print("enter a valid score between {} and {} ".format(MIN, MAX))
    return scores_dict


def average_scores(scores):
    """
    :param scores: input of a dictionary
    :return: returns the average of the values in scores
    """
    total = 0
    for key in scores:
        total += scores[key]
    average = total/len(scores)
    return average


if __name__ == '__main__':
    my_scores = get_test_scores()
    print("My average is {: .2f} ".format(average_scores(my_scores)))

"""
    This file contains your final_strategy that will be submitted to the contest.
    It will only be run on your local machine, so you can import whatever you want!
    Remember to supply a unique PLAYER_NAME or your submission will not succeed.
"""
import csv
PLAYER_NAME = 'weiweimonster'  # Change this line!

def final_strategy(score, opponent_score):
    count=0
    Policy={}
    with open('hog4.csv', 'r') as r:
        csv_reader = csv.DictReader(r)
        fieldname = []
        for i in range(99, -1, -1):
            for j in range(8):
                fieldname.append((i, j))
        for row in csv_reader:
            for k in range(len(fieldname)):
                Policy[(99 - count, int(fieldname[k][0]), int(fieldname[k][1]))] = row[str(fieldname[k])]
            count += 1
    if score<=99 and score>=97:
        return 0





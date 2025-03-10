from art import logo, vs
from game_data import data
import random
first = random.randint(0, 49)
second = random.randint(0, 49)
while first == second:
    second = random.randint(0, 49)
count = 0
win = True
while win:
    print(logo)
    print(f"Compare A: {data[first]['name']},a {data[first]['description']} from {data[first]['country']}")
    print(vs)
    print(f"Against B: {data[second]['name']},a {data[second]['description']}, from {data[second]['country']}")
    win2 = str(input("\nWho has more followers? Type 'A' or 'B':")).upper()
    win1 = '0'

    if data[first]['follower_count'] > data[second]['follower_count']:
        win1 = 'A'
    else:
        win1 = 'B'
    if win1 != win2:
        print(f"Sorry it ends, points: {count}")
        win = False
    else:
        count += 1
        print(f"Ur correct next round, No of points: {count}")
    first = second
    while first == second:
        second = random.randint(0, 49)

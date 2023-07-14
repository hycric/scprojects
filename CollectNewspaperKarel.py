from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Richard Huang
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    go_get()
    come_back()

def go_get():
    """
    Pre-condition: Karel is in the wall area facing east on street 4 avenue 3
    Post-condition: Karel is outside the wall area facing north on street 3 avenue 6
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()

def come_back():
    """
    Pre-condition: Karel is outside the wall area facing north on street 3 avenue 6
    Post-condition: Karel is in the wall area facing east on street 4 avenue 3
    """
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_right()
    move()
    put_beeper()


def turn_right():
    """
    to save time from writing turn_left() three times
    """
    turn_left()
    turn_left()
    turn_left()







# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

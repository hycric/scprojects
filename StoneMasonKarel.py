from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Richard Huang
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():

    move_up()
    move_right()
    move_down()
    return_up()
    move_right()
    move_down()
    return_up()
    move_right()
    move_down()



def move_up():
    """
    Pre-Condition: Karel is on street 1 facing east
    Post-Condition: Karel is on street 5  facing north
    """

    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()


def turn_right():
    """
    to save time from writing turn_left() 3 times
    """
    turn_left()
    turn_left()
    turn_left()


def move_right():
    """
    Pre-Condition: Karel is on street 5  facing north
    Post-Condition: Karel is on street 5 facing south
    """
    turn_right()
    move()
    while left_is_clear():
        move()
    turn_right()


def move_down():
    """
    Pre-Condition: Karel is on street 5 facing south
    Post-Condition: Karel is on street 1 facing north
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper():
        put_beeper()


def turn_around():
    """
    to save time from writing turn_left() 3 times
    """
    turn_left()
    turn_left()


def return_up():
    """
    Pre-Condition: Karel is on street 1 facing south
    Post-Condition: Karel is on street 5 facing north
    """
    turn_around()
    while front_is_clear():
        move()






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

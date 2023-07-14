from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Richard Huang
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    drive_up()
    drive_down()
    while not front_is_clear():
        if not front_is_clear():
            turn_left()
        if front_is_clear():
            turn_right()
            drive_up_right()
            drive_down_right()
        else:
            turn_around()


def turn_around():
    """
    to save time from writing turn_left() 2 times
    """
    turn_left()
    turn_left()


def drive_up():
    """
    Pre-Condition: Karel is on street 1 facing east
    Post-Condition: Karel is on street 8 facing north
    """
    turn_left()
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()



def drive_down():
    """
    Pre-Condition: Karel is on street 8 facing north
    Post-Condition: Karel is on street 1 facing south
    """

    if not on_beeper():
        turn_right()
        move()
        turn_right()
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()
    else:
        turn_right()
        move()
        turn_right()
        move()
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()


def turn_right():
    """
    to save time from writing turn_left() 3 times
    """
    turn_left()
    turn_left()
    turn_left()

def drive_up_right():
    """
    Pre-Condition: Karel is on street 1 facing south
    Post-Condition: Karel is on street 8 facing north
    """
    if not on_beeper():
        turn_left()
        move()
        turn_left()
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()
    else:
        turn_left()
        move()
        turn_left()
        move()
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()


def drive_down_right():
    """
    Pre-Condition: Karel is on street 8 facing north
    Post-Condition: Karel is on street 1 facing south
    """
    if not on_beeper():
        turn_right()
        move()
        turn_right()
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()
    else:
        turn_right()
        move()
        turn_right()
        move()
        put_beeper()
        while front_is_clear():
            move()
            if front_is_clear():
                move()
                put_beeper()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)

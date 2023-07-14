from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: Richard Huang
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    pave()
    plumb_left_one()
    plumb_right_one()
    while not on_beeper():
        dumb_plumb_left()
        dumb_plumb_right()
        if not front_is_clear():
            turn_around()
            while not on_beeper():
                move()
            move()
            if not on_beeper():
                turn_around()
                move()
            else:
                move()
                if not on_beeper():
                    turn_around()
                    move()
                    pick_beeper()
                    move()
                else:
                    turn_around()
                    while front_is_clear():
                        move()



def turn_around():
    """
    to save time from writing turn_left() 2 times
    """
    turn_left()
    turn_left()


def pave():
    """
    Karel puts a street of beepers
    """
    put_beeper()
    while front_is_clear():
        move()
        put_beeper()


def plumb_left_one():
    """
    Karel removes the first beeper on the right hand side
    """
    if not front_is_clear():
        turn_around()
        pick_beeper()
    while front_is_clear():
        move()


def plumb_right_one():
    """
    Karel removes the first beeper on the left hand side
    """
    if not front_is_clear():
        turn_around()
        pick_beeper()
    while front_is_clear():
        move()


def dumb_plumb_left():
    """
    Karel removes  beeper on the right hand side
    """
    turn_around()
    while not on_beeper():
        move()
    pick_beeper()
    while front_is_clear():
        move()


def dumb_plumb_right():
    """
    Karel removes the beeper on the left hand side
    """
    turn_around()
    while not on_beeper():
        move()
    pick_beeper()
    while front_is_clear():
        move()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)

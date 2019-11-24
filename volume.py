#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program calculates the volume of a cylinder

import math


def calculate_volume(radius, height):
    # calculate volume
    # process
    volume = math.pi * radius ** 2 * height

    # output
    print("Volume is {:.2f} cm3".format(volume))
    return volume


def main():
    # this function gets radius and height
    while True:
        # input
        radius_user_input = input("Enter the Radius of The Cylinder (cm): ")
        height_user_input = input("Enter the Height of The Cylinder(cm): ")
        print("")

        # process
        try:
            radius_from_user_int = int(radius_user_input)
            height_from_user_int = int(height_user_input)
            print("You Entered A Number Correctly")
            # call functions
            calculate_volume(radius_from_user_int, height_from_user_int)

        # Prevents the program from crashing
        except ValueError:
            print("Not An Integer")
            continue

        else:
            break


if __name__ == "__main__":
    main()

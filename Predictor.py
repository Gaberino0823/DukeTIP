from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

user = "" # variable for the input

degrees = [-40, -20, 0, 20, 40, 60, 80] # degrees for corresponding measurements
measurements = [65.33333333,  130, 383.6666667, 642.6666667, 717.6666667, 626, 365.3333333] # the measurements for the nerf gun

poly = np.polyfit(degrees, measurements, 3)
eq = np.poly1d(poly)

while True: # while the user input is empty
    user = raw_input("Type a Angle(type q to quit): ") # Prompts user to type an angle
    userint = 0

    if user == "q":
        print("You have quit")
        exit()

    try:
        userint = int(user)
    except ValueError:
        print("That is not a Angle")
        continue


    print(str(eq))
    print(eq(userint))


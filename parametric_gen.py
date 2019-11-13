import matplotlib.pyplot as plt
import numpy as np
import random

precs = 10
completed = False

while completed == False:
    mode = input("Mode ([r]andom or [c]hoose): ")

    if mode == "r":
        val1 = random.randint(6,12)
        val2 = random.randint(6,12)
        n = 1000*precs

        rotations = 2*np.pi*val1*val2
        
        t = np.linspace(0, rotations, n+1)

        x = np.cos(val1*t)
        y = np.sin(val2*t)

        plt.axis("equal")
        plt.grid()
        plt.plot(x, y)
        plt.show()

        finishedInput = input("Are you finished? (y/n): ")
        
        if finishedInput == "n":
            completed = False
        else:
            completed = True

    elif mode == "c":
        val1 = int(input("Val1: "))
        val2 = int(input("Val2: "))
        n = 1000*precs

        rotations = 2*np.pi*val1*val2
        
        t = np.linspace(0, rotations, n+1)

        x = np.cos(val1*t)
        y = np.sin(val2*t)

        plt.axis("equal")
        plt.grid()
        plt.plot(x, y)
        plt.show()

        finishedInput = input("Are you finished? (y/n): ")
        
        if finishedInput == "n":
            completed = False
        else:
            completed = True

    else:
        print('Please choose "r" or "c"')

print("Thank you for using this program!")
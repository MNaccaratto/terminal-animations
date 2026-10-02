"""
Terminal Animations
Author: Maxwell Naccaratto

This is just a silly passtime to see if I can make different kinds of animations in the command line terminal
"""

import time


def dot():
    dotstr = "•"

    i = 0
    while i <= 10:
        print(f"{dotstr}", end="\r", flush=True)
        i += 1
        time.sleep(0.25)
        dotstr = " " + dotstr


def bounce():
    bouncestr = "•"

    while True:
        height = input("How high do you want the ball to bounce [10-50]? ")


if __name__ == "__main__":

    valid_ani = ["bounce", "dot"]
    print("_____Welcome to Maxwell's Terminal Animations_____")

    while True:
        print("* You have the following options:")
        print("*      Dot")
        print("*      Quit Animation [enter quit]")
        user = str(input("\nPlease give me the animation you'd like to see: ")).lower()

        if user not in valid_ani:
            print(f"{user} is not a valid animation")
            continue

        print(f"You selected {user}")
        match user:
            case "dot":
                dot()
            case "bounce":
                bounce()
            case "quit":
                break

        time.sleep(0.1)
        more = str(input("Would you like to see another animation? [y/n] ")).lower()
        if more == "n":
            break
        else:
            continue

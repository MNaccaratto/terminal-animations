"""
Terminal Animations
Author: Maxwell Naccaratto

This is just a silly passtime to see if I can make different kinds of animations in the command line terminal
"""

import time


def dot():
    dotstr = "•"

    i = 0
    while i <= 20:
        print(f"{dotstr}", end="\r", flush=True)
        i += 1
        time.sleep(0.5)
        dotstr = " " + dotstr


if __name__ == "__main__":

    print("_____Welcome to Maxwell's Terminal Animations_____")

    while True:
        print("* You have the following options:")
        print("*      Dot")
        print("*      Quit Animation [enter quit]")
        user = str(input("\nPlease give me the animation you'd like to see: ")).lower()

        print(f"You selected {user}")
        match user:
            case "dot":
                dot()
            case "quit"

        time.sleep(0.1)
        more = str(input("Would you like to see another animation? [y/n] ")).lower()
        if more == "n":
            break
        else:
            continue

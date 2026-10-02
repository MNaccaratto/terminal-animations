"""
Terminal Animations
Author: Maxwell Naccaratto

This is just a silly passtime to see if I can make different kinds of animations in the command line terminal
"""

import time

if __name__ == "__main__":

    dotstr = "•"

    i = 0
    while i <= 10:
        print(f"{dotstr}", end="\r", flush=True)
        i += 1
        time.sleep(0.5)
        dotstr = " " + dotstr

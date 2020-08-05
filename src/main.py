# Import the curses library...
import curses
import os
import random
# ...and some other files
from TWS.windowClass import *
from TWS.screenCycle import *

# The main function
def main(stdscr):
    # Color combinations
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK) # For the shadows
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE) # Same, but inverted
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE) # The background color
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK) # For the titles

    # Stdscr settings
    curses.curs_set(0)
    stdscr.bkgd(" ", curses.color_pair(3))
    stdscr.refresh()
    stdscr.timeout(500)
    
    # The core of the program
    scr = Screen(stdscr)

    def appLauncherFunction(window, key, clickedButton):
        if clickedButton != 0:
            if clickedButton["widgetID"] == "endSession":
                exit()

            else:
                try:
                    exec(open("Programs/" + clickedButton["widgetID"] + "/main.py").read())

                except Exception as ex:
                    window.alert("Error Running Program", "There was an error while trying to run the program. Error: " + str(ex))

    appLauncher = Window(5, 5, curses.LINES-10, curses.COLS-10, "TWS-App_Launcher", appLauncherFunction)
    appLauncher.addLabel("", 1, 2, "Use arrow keys to highlight an option and <ENTER> to 'click' an option.")

    # Create a button for each file in the 'Programs' directory
    idx = 0
    for program in os.listdir("./Programs"):
        idx += 1

        # If the file has "." as the first letter it's a hidden file.
        if program[0] != "." and os.path.isfile(os.getcwd() + "/Programs/" + program) == False:
            # Get the programs metadata from the 'TWSProgram.txt' file
            settingsData = str(open("./Programs/" + program + "/TWSProgram.txt").read())
            displayname = settingsData.split("\n")[0][13:]
            displayname = displayname[:-1]

            displaysymbol = settingsData.split("\n")[1][15:]
            displaysymbol = displaysymbol[:-1]

            appLauncher.addButton(str(program), idx+2, 2, "[" + displaysymbol + "] " + displayname)

        else:
            idx -= 1

    appLauncher.addButton("endSession", curses.LINES-12, 2, "[x] End Session")

    scr.mainloop()

    # Update the screen and wait for 1 second (curses.napms())
    stdscr.refresh()
    curses.napms(1000)

curses.wrapper(main)
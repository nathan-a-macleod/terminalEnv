import os
import datetime
import curses

curses.endwin()

startDir = os.getcwd()
commandHistory = []

command = ""
    
os.system("clear")
print(f"To return to the semi-graphical terminal windowing system, type: 'exit'")

while command != "exit":
    now = datetime.datetime.now()
    command = input("\033[37;44m" + now.strftime("<%I:%M:%p>") + "\033[0m~\033[31;4m" + os.popen("whoami").read().split()[0] + "\033[0m~\033[36m" + os.popen("pwd").read().split("\n")[0] + "/\033[0m~$ ")

    if command.split()[0] != "ls":
        os.system(command)

    else:
        command += " --color"
        os.system(command)

    if command != "" and command != " ":
        # To allow the user to press up arrow to go to the last command (not completed yet):
        commandHistory.append(command)

        if command.split()[0] == "cd":
            # To allow changing of directories:
            try:
                os.chdir(command.split()[1])

            except:
                pass

os.chdir(startDir)

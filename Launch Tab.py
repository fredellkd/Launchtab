import os
import webbrowser
from pathlib import Path
import time

home = str(Path.home())
t1 = home + "/Desktop/urls.txt"
chrome = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


def option1():
    os.system("cls")
    print("""We will create a text file on your Desktop and opened it for you.
Please add domains to this text file, one per line not spaces.
Once finished save and close the file.
    
Example below:

nypost.com
businessinsider.com
washingtonpost.com
https://thehackernews.com/
    """)
    input("Press Enter to continue...")

    file = open(t1, "a+")
    file.close()

    os.system('notepad.exe ' + t1)

    with open(t1, "r") as data:
        os.system("cls")
        print("""
We will now open your saved URLS"""
              )
        time.sleep(3)
        for i in data:
            webbrowser.get(chrome).open_new(i)


def option2():
    os.system("cls")
    print("""We will open the text file containing your urls for you to edit.
Once finished save and close the file.
    """)
    input("Press Enter to continue...")

    os.system('notepad.exe ' + t1)

    with open(t1, "r") as data:
        os.system("cls")
        print("""
We will now open your saved URLS"""
              )
        time.sleep(3)
        for i in data:
            webbrowser.get(chrome).open_new(i)


def option3():
    os.system("cls")
    with open(t1, "r") as data:
        print("""
We will now open your saved URLS"""
              )
        time.sleep(3)
        for i in data:
            webbrowser.get(chrome).open_new(i)


print("""Welcome to Launch Tab. This tool speeds up the opening all the sites you need
on a daily basis by launching multiple urls at once. Created by Daniel Fredell
Note: If any errors occur using this tool, delete the 'urls.txt' file from your
Desktop and choose option 1.
WARNING: You are responsible for all link/URLs entered into this program
Please select from one of the following options.

1 = First Time User? Set up your links
2 = Need to update your links
3 = Open your links""")

choice = ""
while choice != "1" and choice != "2" and choice != "3":
    choice = input("""
Choose option 1-3: """
                   )
    if choice != "1" and choice != "2" and choice != "3":
        os.system("cls")
        print("""You did not choose option 1, 2, or 3
Please choose from one of the three options.
    
1 = First Time User? Set up your links
2 = Need to update your links
3 = Open your links
        """)


if choice == "1":
    option1()
elif choice == "2":
    option2()
elif choice == "3":
    option3()

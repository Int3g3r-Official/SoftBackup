from os import listdir
from time import sleep
import googlesearch
from webbrowser import open_new_tab

def ScanApps(OS):
    if OS == "Darwin":
        OSXPATH = "/Applications"
        #Declare default path of applications
        Blocked=[
            '.DS_Store',
            '.localized',
            'Utilities',
            'Safari.app'
        ]
        #Declare defaultly blocked apps
        installed = listdir(OSXPATH)
        for i in range(len(Blocked)):
            installed.remove(Blocked[i])
        #Remove blocked apps from the list
        print("Done scanning default OSX path -> /Applications\nApps found: ")
        print(installed)
        #Print the list to the screen
        additionalPaths = input("Additional path (If none press enter without typing anything)-> ")
        if additionalPaths != '':
            installed.append(listdir(additionalPaths))
        #Check if user has any other paths they need to be included.
        SaveFile(installed)
    if OS == "Windows":
        print("Not supported currently")
    if OS == "Linux":
        print("Not supported currently")
def SaveFile(installed):
    file = open("saved.txt","w+")
    for i in range(len(installed)):
        if i != len(installed)-1:
            file.write(f"{installed[i]}\n")
        else:
            file.write(installed[i])
def RestoreFiles():
    print("Taking you to the download pages!")

    toInstall = []
    file = open("saved.txt","r")
    toInstall.append(file.read())
    toInstall = "".join(toInstall)
    toInstall = toInstall.split("\n")
    file.close()
    progressGoal = len(toInstall)
    progress  = 0
    fatals = 0
    for i in range(len(toInstall)):
        while True:
            try:
                print(f"Searching for {toInstall[i]}")
                result = list(googlesearch.search(f"{toInstall[i]} download",num=1,stop=1))
                break
            except:
                fatals +=1
                print(f"Tries {fatals} of 3")
                file = open("log.txt","a")
                file.write(f"Unable to search google. Tries -> {fatals}\n")
                if fatals == 3:
                    print("Try again later.")
                    exit(199)
                print("Google is blocking our requests so we will wait 5 minutes.")
                sleep(300)
        try:
            print(f"opening {result[0]}")
            open_new_tab(result[0])
            progress += 1
        except:
            print("Google was unable to find the specified application.")
            file = open("log.txt","a")
            file.write(f"Unable to find app -> {toInstall[i]}\n")

        print(f"{progress} of {progressGoal}")

    if progress != progressGoal:
        print("Some apps were not found, check log for errors.")
    
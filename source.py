from os import listdir
from os import makedirs
from os import path
from time import sleep
from webbrowser import open as webopen
from webbrowser import open_new as webopennew
#Define public variables
OSXPath = '/Applications'
Blocked = [
    '.DS_Store',
    '.localized',
    'Utilities'
]
Default = [
    'Safari.app'
]

#Get the installed programs.
installed = listdir(OSXPath)
for i in range(len(Blocked)):
    installed.remove(Blocked[i])

#Check for default programs:
print("Default app check:\n")
for i in range(len(Default)):
    if Default[i] in installed:
        print(Default[i] + " is a default app. Skipping\n")
        installed.remove(Default[i])


#Show installed programs in the console.
print("Apps found:\n")
print(installed)
print("")
def SaveRestore(mode,installed="Nothing found."):
    if mode == 0:
        try:
            if not path.exists('Output'):
                makedirs("Output")
            f = open("Output/programs.txt","a")
            for app in installed:
                f.write(app + '\n')
            f.close()
            print("Done\n")
            print("\nSave the file you got that is in Output/programs.txt\nYou will need it for reinstalling the apps.\n\n")
        except:
            print("There was an error saving to file.")
    elif mode == 1:
        if not path.exists("Input"):
            makedirs("Input")
        try:
            toInstall = []
            f = open("Input/programs.txt")
            toInstall.append(f.read())
            toInstall = "".join(toInstall)
            toInstall = toInstall.split("\n")
            toInstall.remove("")
            f.close()
        except:
            print("Error reading the file, are you sure there is a file in input?")
            pass
        for i in range(len(toInstall)):
            webopennew(f"https://www.google.com/search?q={toInstall[i]}")
            print("Done.")


        

# User chooses the mode.
mode = int(input("1. Save\n2. Restore\n3. Exit\n-> "))
mode -= 1

if mode == 2:
    exit(100)
# Run the desired action.
SaveRestore(mode,installed)

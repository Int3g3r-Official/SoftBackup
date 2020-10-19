from engine import ScanApps
from engine import RestoreFiles
from platform import system

choice = input("Backup / Restore -> ").lower()

if choice == "backup" or choice == "b":
    OS = system()
    ScanApps(OS)
elif choice == "restore" or choice == "r":
    RestoreFiles()
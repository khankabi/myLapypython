"""
Shutil Module in Python
Shutil is a Python module that provides a higher level interface for working with file and directories. The name "shutil" is short for shell utility. It provides a convenient and efficient way to automate tasks that are commonly performed on files and directories. In this repl, we'll take a closer look at the shutil module and its various functions and how they can be used in Python.

Importing shutil
The syntax for importing the shutil module is as follows:

import shutil

Functions
The following are some of the most commonly used functions in the shutil module:

shutil.copy(src, dst): This function copies the file located at src to a new location specified by dst. If the destination location already exists, the original file will be overwritten.

shutil.copy2(src, dst): This function is similar to shutil.copy, but it also preserves more metadata about the original file, such as the timestamp.

shutil.copytree(src, dst): This function recursively copies the directory located at src to a new location specified by dst. If the destination location already exists, the original directory will be merged with it.

shutil.move(src, dst): This function moves the file located at src to a new location specified by dst. This function is equivalent to renaming a file in most cases.

shutil.rmtree(path): This function recursively deletes the directory located at path, along with all of its contents. This function is similar to using the rm -rf command in a shell.
"""
import shutil

shutil.copy("temp.txt","temp2.txt")

# import shutil
shutil.copy(src="F:/Original.txt", dst="C:/Test/Original.txt")


"""
code to copy data from usb
import os
import shutil

# 1. Check and clean USB

def USB():
    usb_inserted = os.path.isdir("F:") # <-- returns boolean...checks whether a directory exists

    if usb_inserted == False:
        print("\n\nUSB stick is not plugged in. Waiting for connection...")

        while usb_inserted == False: # wait

             updating variable, because it takes only the return value of function 'isdir()'
             and stays the same regardless of the fact, that 'isdir()' changed
            usb_inserted = os.path.isdir("F:")
            continue

    SECURITY_FILE = "System Volume Information"

    if os.listdir("F:") == [SECURITY_FILE] or os.listdir("F:") == []: # if list of files contains only the security file (is empty)
        print("\nUSB flash is already empty.") # send a message and continue

    else:
        files = os.listdir("F:") # list of names of files in the usb flash, that will be deleted

        if SECURITY_FILE in files:

             taking out the security file from the list, because attempting to delete it causes
            'PermissionError [WinError 5]' exception
            files.remove(SECURITY_FILE)

        for file in files: # Loop through the file list

            if os.path.isfile(f"F:\\{file}"): # if it's a file
                os.remove(f"F:\\{file}") # Delete the file

            elif os.path.isdir(f"F:\\{file}"): # if it's a directory/folder
                shutil.rmtree(f"F:\\{file}") # remove the folder

        print("\nAll files/folders are deleted from USB.")

USB()
"""
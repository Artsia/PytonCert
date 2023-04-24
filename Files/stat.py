
# read first lines of file

import os
f = open("t.txt", "r")
# print(f.readline())


f.close()


'''
read first 21 characters of the file
'''
MAX = 21
a = open("t.txt", "r")
a.read(MAX)
a.close()


try:

    # save passwords to local machine by creating a file

    file_name = input("enter only the name of the file: ")

    if os.path.exists(file_name + ".txt"):
        content = input("Enter content to existing file:  ")
        w = open(file_name+".txt", "a")
        w.write("\n"+content+"\n")
        w.close()
        
    else:
        nFile = open(file_name+".txt", "w")
        content = input("Enter new content:  ")
        nFile.write("\n"+content+"\n")
        nFile.close()

except:
    Exception

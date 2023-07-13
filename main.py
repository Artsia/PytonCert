

'''
f = ["banana","apple","pineaple", "yoyo",23]
counter = 0
while counter < len(f):
    print(f[counter])
    counter = counter + 1
'''

'''
def printCategory(age):
    if age >= 65:
        print("senior")
    
    if age >= 18 and age < 64:
        print("adult")
        
    if age < 18:
        print("teen")
'''

from time import *
def myPw():
    pw = input("Password?")
    o_pw = "phi"
    if pw == o_pw:
        return ("welcome")
    else:
        sleep(1)
        return "Bye" , quit()

myPw()









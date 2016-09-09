"""
To get name and age
"""
import datetime
NAME = input("Hi\nWhat is your name?\n")
AGE = int(input("Please enter your age:"))
print ("Hi %s. You are %d years old and you will turn %d in %d"
       %(NAME, AGE, 100, datetime.datetime.now().year - AGE + 100))

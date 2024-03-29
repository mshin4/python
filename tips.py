
####################
### slicing ########
####################
'''

list1 = ["a", "b", "c", "d", "e", "f", "g"]
# 0-"a"-1-"b"-2-"c"-3-"d"-4-"e"-5-"f"-6-"g"-7

print(list1[2:5])
# [2:5] is 2-"c"-3-"d"-4-"e"-5
# output ['c', 'd', 'e']

print(list1[2:])
# from 2 to the end
# output ['c', 'd', 'e', 'f', 'g']

print(list1[:5])
# from 0 to 5
# output ['a', 'b', 'c', 'd', 'e']

print(list1[2:5:2])
# from 2 to 5 in increments of 2
# output ['c', 'e']

print(list1[::-1])
# all elements incremented by one starting from the end to the beginning 
# output ['g', 'f', 'e', 'd', 'c', 'b', 'a']
'''



# This compares two lists and filters out only the items not in common
'''
my_list1=list('Skywalker')
#print(my_list1)
my_list2=list('Vader')
#print(my_list2)
my_list3=list(filter(lambda x: x not in my_list2, my_list1))
print(my_list3)
'''

'''
class Animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale and exhale")


# how to inherit a class
class Fish(Animal):

    def __init__(self):
        super().__init__()

    
    # to alter the superclass method breathe
    def breathe(self):
        super().breathe()
        print("while under water")

    def swim(self):
        print("moving in water")

fishy = Fish()
# notice this prints both from super class and subclass
fishy.breathe()
print(fishy.num_eyes)
'''


# addint inputs to a variable
'''
coins_inserted = 0
coins_inserted += int(input("Add Quarters: ")) * .25
coins_inserted += int(input("Add Dimes: ")) * .1
coins_inserted += int(input("Add Nickels: ")) * .05
coins_inserted += int(input("Add Pennies: ")) * .01
print(f"${coins_inserted}")
'''

#######################
### DICTIONARIES {} ###
#######################

# update a dictionary value
#'''
resources = {
    "water": 200,
    "milk": 100,
    "coffee": 50
}

resources["water"] -= 100
# or
resources['water'] = 50
# or update multiple keys' value

for item in resources:
    resources[item] *= 2
print(resources)
#'''

# compare two dictionaries where one is deeply nested
'''
MENU = {
    "espresso": {
        "ingredients": {
            "water": 200,
            "coffee": 100,
        }
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "coffee": 100,
            "milk": 50
        }
    },
    "cappuccino": {
        "ingredients": {
            "water": 150,
            "coffee": 100,
            "milk": 100
        }
    }
}

resources = {
    "water": 10,
    "coffee": 10,
    "milk": 100
}

coffee = input("espresso/latte/cappuccino: ")
coffee_choice = MENU[coffee]

def order_coffee():
    for item in coffee_choice["ingredients"]:
        if coffee_choice["ingredients"][item] > resources[item]:
            return False
        else:
            return True

print(order_coffee())
'''

### Using Dictionary to find DUPES - how to find and list duplicate files
'''
file_dict = {
    "file1": "ABCDE",
    "file2": "FGHIJ",
    "file3": "ABCD",
    "file4": "ABCDE"
}


new_dict = {}

for file in file_dict:
    file_hash = file_dict[file]
    if file_hash in new_dict:
        new_dict[file_hash].append(file)
    else:
        new_dict[file_hash] = [file]


print(new_dict)
'''


### More dictionaries - creating a dictionary looping strings
'''
l = {}
for i in 'Skywalker': # Skywdlkdd
    if i in 'Vader':
        l[ord(i)] = i # { : a, e, r}
else:
    l[ord('d')] = 'd' # { a, e, r, d}
print(l)
for j in l.keys():
    print(l[j], end=' ')

'''

# multiple input values can be split into a list
# split method will create a list and separate the entries below whenever there is a space or comma
'''
any_answer = input("Please enter values for variables: ").split(",")

print("The value for variables are :", any_answer)
print(any_answer[2])
'''


# lambda usage
# you can use it almost like a class template and reuse functions as needed
'''
squared = lambda num: num * num # simple example
print(squared(5))

def myfunc(n):
    """lambda is useful for reuisng the function with different variable names"""
    return lambda b: b * n

doubler = myfunc(2)
tripler = myfunc(3)
print(doubler(11))
print(tripler(11))
'''

# factorial function
'''
import math
import os
import random
import re
import sys

def factorial(n):
    # Write your code here
    if n == 0:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':

    n = int(input().strip())

    result = factorial(n)
    print(result)
'''

'''
# Create multiple instances\objects using a class
# Add the instances to a list
# Print an attribute of each instance

from turtle import Turtle, Screen

colors = ["red", "orange", "green", "blue", "purple"]
y_position = [-60, -20, 20, 60, 100]
all_turtles = []
screen = Screen()


for turtle_index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-100, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


for turtle in all_turtles:
    print(turtle.pencolor())

screen.exitonclick()

'''
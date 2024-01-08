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

# update a dictionary value
'''
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
'''

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
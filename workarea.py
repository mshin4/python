
def greet():
    print("Welcome!")
    print("Bienvenido!")
    print("Come on in!")

greet()

'''
import random
import os
from hangman_art import stages, logo
from hangman_words import word_list


end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
incorrect_guess = []
lives = 6

# Create the list that shows the number of blank spaces.
for _ in range(word_length):
    display.append("_")

# Game starting point
print(logo)
while not end_of_game:
    print("")
    guess = input("Guess a letter. ").lower()
    print("")
    os.system('clear')
    if guess in display:
        print("You have already guessed that letter.")
 
 # Loop through the chosen word from index 0 to the ending index and compare the letters with the guessed letter.
 # If the guess matches, add the letter to the display list at the appropriate placement.
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

# Checked to see if incorrected guessed letter was already guessed. If it was not, then, update the number of lives minus 1.
# Print a message to the user stating that they guessed incorrectly and show which letters they guessed wrong.
    if guess not in chosen_word:
        if guess in incorrect_guess:
            print(f"You have already guessed the letter {guess}.")
        else:
            incorrect_guess.append(guess)
            lives -= 1
            print(f"Sorry, '{guess}' is not in the word. You lose a life.")
            print(stages[lives])
            if len(incorrect_guess) > 0:
                print(f"Incorrectly guessed letter(s): {' '.join(incorrect_guess)}")
    if lives == 0:
        end_of_game = True
        print("Sorry, you lose.")
        print(f"The word is: {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
'''
'''
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

new_password = []
letters_length = len(letters) #52
numbers_length = len(numbers)
symbols_length = len(symbols)
#print(letters_length)

for x in range(0, nr_letters):
    pick_rletter = random.randint(0,letters_length -1)
    new_password.append(letters[pick_rletter])

for y in range(0, nr_numbers):
    pick_rnumber = random.randint(0,numbers_length -1)
    new_password.append(numbers[pick_rnumber])

for z in range(0, nr_symbols):
    pick_rsymbol = random.randint(0,symbols_length -1)
    new_password.append(symbols[pick_rsymbol])


random.shuffle(new_password)
print(new_password)

password = ""
# for a1 in range(0, len(new_password)):
#     password += new_password[a1]
for char in new_password:
    password += char
print(password)

'''
'''
target = int(input("Enter a number between 0 and 1000.\n"))
total = 0

#print(end_range)
for number in range(0, target + 1, 2):
    total += number
    #print(total)
print(total)
'''
'''
# Input a list of student scores
#student_scores = input().split()
student_scores = ["78", "65", "89", "86", "55", "91", "64", "89"]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    print(highest_score)

print(f"The highest score in the class is: {highest_score}")
'''

"""
# Input a Python list of student heights
#student_heights = input().split()
student_heights = ["135", "145", "140", "155", "160"]
#print(type(student_heights[0]))
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for x in student_heights:
  total_height += x

print(f"total height = {total_height}")

total_students = 0
for y in student_heights:
  total_students += 1

print(f"number of students = {total_students}")
average_height = round(total_height / total_students)
print(f"average height = {average_height}")

"""



"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if user_choice > 2:
    print("You typed an invalid number. You lose!")
else:
    print(game[user_choice])
    computer_choice = random.randint(0,2)
    print(f"Computer chose: {computer_choice}")
    print(game[computer_choice])
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw.")

"""      

"""
choice = input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n")
print(choice)
computer_hand = str(random.randint(0,2))

if choice == "0":
    if computer_hand == "0":
        print(rock)
        print("Computer chose:")
        print(rock)
        print("It's a tie.")
    elif computer_hand == "1":
        print(rock)
        print("Computer chose:")
        print(paper)
        print("You lose.")
    elif computer_hand == "2":
        print(rock)
        print("Computer chose:")
        print(scissors)
        print("You win.")

elif choice == "1":
    if computer_hand == "0":
        print(paper)
        print("Computer chose:")
        print(rock)
        print("You win.")
    elif computer_hand == "1":
        print(paper)
        print("Computer chose:")
        print(paper)
        print("It's a tie.")
    elif computer_hand == "2":
        print(paper)
        print("Computer chose:")
        print(scissors)
        print("You lose.")

elif choice == "2":
    if computer_hand == "0":
        print(scissors)
        print("Computer chose:")
        print(rock)
        print("You win.")
    elif computer_hand == "1":
        print(scissors)
        print("Computer chose:")
        print(paper)
        print("You lose.")
    elif computer_hand == "2":
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("It's a tie.")
else:
    print("Start over, you did not pick a valid number.")
#print(computer_hand)
"""
"""
line1 = ["⬜️","️⬜️","️⬜️"] #0
line2 = ["⬜️","⬜️","️⬜️"] #1
line3 = ["⬜️️","⬜️️","⬜️️"] #2
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

letter = position[0].lower()
abc = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) -1
map[number_index][letter_index] = "X"
"""
"""
if "1" in position.lower():
    print("0")
    x = 0
if "2" in position.lower():
    print("1")
    x = 1
if "3" in position.lower():
    print("2")
    x = 2
if "a" in position.lower():
    print("0")
    y = 0
if "b" in position.lower():
    print("1")
    y = 1
if "c" in position.lower():
    print("2")
    y = 2

map[x][y] = "X"
"""
# # Write your code above this row 👆
# # 🚨 Don't change the code below 👇
# print(f"{line1}\n{line2}\n{line3}")
"""
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
#print(dirty_dozen)
print(dirty_dozen[1] [2])
print(dirty_dozen[1] [3])

#print(dirty_dozen[0][1])

"""


"""
import random

# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(names)
print(f"{random.choice(names)} is going to buy the meal today.")
new = len(names)
print(new)
"""

"""
random_number = random.randint(0,1)
print(random_number)
if random_number == 1:
    print("Heads")
else:
    print("Tails")

"""
"""
#########################################################################################################
print('''
       ___
     o|* *|o
     o|* *|o
     o|* *|o
      \===/
       |||
       |||
       |||
       |||
    ___|||___
   /   |||   \\
  /    |||    \\
 |     |||     |
  \   (|||)   /
   |   |||   |
  /    |||    \\
 /     |||     \\
/      |||      \\
|     [===]     |
 \             /
  '.         .'
    '-------'

''')
print('Welcome to the mood music game!')
print('Your mission is to find out your dad\'s favorite type of songs.')

mood1 = input("Is his music sad or happy? Type either sad or happy. ")
answer1 = mood1.lower()

if answer1 == "sad":
    gender = input("You guessed correctly. Is the artist male, female or doesn't matter? Type either male, female or doesn't matter. ")
    #print("Yes!")
    answer2 = gender.lower()
    if answer2 == "male":
        print("Game over.")
    if answer2 == "female":
        print("Game over.")
    elif answer2 == "doesn't matter":
        mood2 = input("That's correct! Now are the songs based mainly in response to heart break or anger. Type either heart break or anger. ")
        answer3 = mood2.lower()
        if answer3 == "anger":
            print("Game over.")
        elif answer3 == "heart break":
            print("You did it! You've got a piece of dad's heart.")
elif answer1 == "happy":
    print("Game over.")

#########################################################################################################
"""
"""
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

 
# using naive method to get count
# counting e
both_names = name1 + name2
#print(both_names)
lower_names = both_names.lower()
#print(lower_case)
count = 0
 
for i in lower_names:
    if i == 't':
        count = count + 1
    elif i == 'r':
        count = count + 1
    elif i == 'u':
        count = count + 1
    elif i == 'e':
        count = count + 1

# for i in name2:
#     if i == 't':
#         count = count + 1
#     elif i == 'r':
#         count = count + 1
#     elif i == 'u':
#         count = count + 1
#     elif i == 'e':
#         count = count + 1
# printing result
first_number = count
print(first_number)

count = 0
for i in lower_names:
    if i == 'l':
        count = count + 1
    elif i == 'o':
        count = count + 1
    elif i == 'v':
        count = count + 1
    elif i == 'e':
        count = count + 1

second_number = count
print(second_number)

converted = int(str(first_number) + str(second_number))
#converted = int(combined)
if converted < 10 or converted > 90:
    print(f"Your score is {converted}, you go together like coke and mentos.")
elif 40 <= converted <= 50:
    print(f"Your score is {converted}, you are alright together.")
else:
    print(f"Your score is {converted}.")
"""

#########################################################################################################

# #print("Hello " + input("What is your name? "))
# # print(int(6 / 2))
# # print(6 / 2)
# # print(type(6 / 2))
# # print(2 ** 4)

# #print(int(3 / 2))

# # r = round(3 / 2)
# # print(type(r))

# # print(8 / 3)
# # print(8 // 3)
# # print(int(8 / 3))

# score = 0
# score += 1
# print("The score is: " + str(score))
# score += 2
# print(f"The score now is: {score}")
# score += 1
# print(score)

# x = 10 / 3
# print(round(x, 2))

# # 🚨 Don't change the code below 👇
# year = int(input("Which year do you want to check? "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# #>>> isinstance(y, float)

# #leap1 = year // 4
# if year % 4 == 0:
#     #print("First check passed.")
#     if year % 100 == 0:
#         #print("Second check passed.")
#         if year % 400 == 0:
#             print(f"{year} is a leap year!")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is not a leap year.")
# else:
#     print(f"{year} is not a leap year.")

#    if year // 50 == 2:
#        print("yes")
#    else:
#        print("no")

#else:
#    print("nope")


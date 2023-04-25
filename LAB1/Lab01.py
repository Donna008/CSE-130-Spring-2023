# 1. Name: 
#    Na Tang
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    The program is a guessing number game.
#    First, it asks a user to input a number to represent a range of guesses. 
#    And then the need to guess the number is one of the ranges of the input number.
#    And then ask the user to input a guess number, if the guess number is high or low, 
#    we will display a hint reminder user until the user guesses the correct number.
#    In the end, we will display the list of users who try to guess the numbers 
#    and the total to find the correct number of guess times.
# 4. What was the hardest part? Be as specific as possible.
#    I think the hard part is how to MATCH the random numbers and the numbers the user needs to guess,
#    when I looked at the instructions I didn't see there was a template code so I thought the whole 
#    game was very complicated. When I looked at the instructions again I found the template code,
#    and then the hardest part was already given in the template.
#    Was there some aspect of the problem that was particularly difficult to solve?
#       Not yet!
#    Was there an especially difficult bug? If so, how did you resolve it?
#       Not yet!
#    Was there some difficulty with the instructions or any part of the problem definition?
#       Not yet!
# 5. How long did it take for you to complete the assignment?
#    -total of about 2 hours. write code for about 1 hour, take demonstration video for about 1 hour-  

import random
guess_number = None
# total_times = 0
# Game introduction.
intro = [
    'This is the "guess a number" game.',
    'You try to guess a random number in the smallest number of attempts.'
]
for i in intro:
    print (i)

# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input("Enter an integer number: " + '\x1B[1;4m'))

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print('\x1B[0m' + "Guess a number between 1 and " + str(value_max))

# Initialize the sentinal and the array of guesses.
numbers = []

# Play the guessing game.
while guess_number != value_random:

    # Prompt the user for a number.
    guess_number = int(input("Enter a guessing number: " + '\x1B[1;4m'))

    # Store the number in an array so it can be displayed later.
    numbers.append(guess_number)
    print('\x1B[0m'f"{numbers}")
    
    # Make a decision: was the guess too high, too low, or just right.
    if guess_number > value_random:
        print('\x1B[0m' + "Too high!")
    elif guess_number < value_random:
        print('\x1B[0m' + "Too low!")
    
print('\x1B[0m' + "Congratulations!")

# Give the user a report: How many guesses and what the guesses where.
# for i in len(numbers):

#     # total_times += 1
print('\x1B[0m' + f"You guess {len(numbers)} times.")
print('\x1B[0m' + f"You are guessed those numbers: {numbers}")

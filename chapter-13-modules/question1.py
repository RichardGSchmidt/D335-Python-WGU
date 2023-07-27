#    13.8 LAB: Guess the random number
#   
#   Given the code that reads a list of integers, complete the number_guess() function, which should choose a random number between 1 and 100 by calling random.randint() and then output if the guessed number is too low, too high, or correct.
#   
#   Import the random module to use the random.seed() and random.randint() functions.
#   
#       random.seed(seed_value) seeds the random number generator using the given seed_value.
#       random.randint(a, b) returns a random number between a and b (inclusive).
#   
#   For testing purposes, use the seed value 900, which will cause the computer to choose the same random number every time the program runs.
#   
#   Ex: If the input is:
#   
#   32 45 48 80
#   
#   the output is:
#   
#   32 is too low. Random number was 80.
#   45 is too high. Random number was 30.
#   48 is correct!
#   80 is too low. Random number was 97.
 
# Solution:

# This is pretty straightforward, import random
# and call it's randint() function

import random

def number_guess(num):
    # TODO: Get a random number between 1-100
    rand_num = random.randint(1, 100)
    # TODO: Compare parameter num to the random number
    if num > rand_num:
        print(f'{num} is too high. Random number was {rand_num}.')
    elif num < rand_num:    
        print(f'{num} is too low. Random number was {rand_num}.')
    else:
        print(f'{num} is correct!')
        
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        number_guess(num)


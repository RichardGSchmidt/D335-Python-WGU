# 33.10 LAB: Print string in reverse
# Instructor note:
# The skills required for this lab are covered in Chapter 6. Loops. To successfully complete this lab, review the content of Chapter 6, as well as the preceding chapters, and complete the Challenge Activities associated.

# Write a program that takes in a line of text as input, and outputs that line of text in reverse. The program repeats, ending when the user enters "Done", "done", or "d" for the line of text.

# Ex: If the input is:

# Hello there
# Hey
# done
# then the output is:

# ereht olleH
# yeH

# Solution String Slicing inside a while loop

# User input
user_input = input()

# A while loop is used to check for the exit keyword
while((user_input != 'done') and (user_input != 'd') and (user_input != 'Done')):
    
    # In the slice: [::-1] 
    # The two empty colons slice the default scope (the entire string),
    # but the -1 in the slice makes the interval count backwards from the end
    print(user_input[::-1])

    # next input is take, if the exit keyword (done variations)
    # are entered, the while loop will exit.
    user_input = input()
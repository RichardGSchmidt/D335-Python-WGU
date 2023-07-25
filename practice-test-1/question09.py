# 33.9 LAB: Output range with increment of 5

# Write a program whose input is two integers. Output the first integer and subsequent increments of 5 as long as the value is less than or equal to the second integer. End with a newline.

# Ex: If the input is:

# -15
# 10

# the output is:

# -15 -10 -5 0 5 10 
# Ex: If the second integer is less than the first as in:

# 20
# 5
# the output is:

# Second integer can't be less than the first.
#For coding simplicity, output a space after every integer, including the last.

# Solution:
# Essentially this question is to make sure you can
# iterate through a loop giving a range and an interval

# A for loop is used to do this

user_floor = int(input())
user_ceil = int(input())
out_str = ''

# An if statement first checks to make sure range makes sense
if user_ceil >= user_floor:
    # if the range makes sense a for loop is initialized
    # in the range starting at the floor value 
    # and ending at the ceiling value
    # by increments of 5

    for i in range(user_floor, user_ceil+1, 5):
        # The code inside the for loop
        # Appends each interval integer to a string 
        # for later output.
        out_str += f'{i} '
else:
    # required error output if the floor is greater than the ceiling
    out_str = "Second integer can't be less than the first."

# Results output
print (out_str)
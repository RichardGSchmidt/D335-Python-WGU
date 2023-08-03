#     11.17 LAB: Filter and sort a list
#    
#    Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).
#    
#    Ex: If the input is:
#    
#    10 -7 4 39 -6 12 2
#    
#    the output is:
#    
#    2 4 10 12 39 
#    
#    For coding simplicity, follow every output value by a space. Do not end with newline.

# Solution:

# Next portion same as chapter-11-lists\question1.py
user_input = input()
tokens = user_input.split()
nums = []
for token in tokens:
    if int(token) >= 0:
        nums.append(int(token))

# Sort and output
nums.sort()
for num in nums:
    print(num, end=" ")

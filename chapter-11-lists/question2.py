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

# Take input and add to num list if non-negative
nums = [int(i) for i in input().split() if int(i) >= 0]

# Sort and output
nums.sort()
for num in nums:
    print(num, end=" ")
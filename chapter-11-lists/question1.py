#     11.16 LAB: Varied amount of input data
#    
#    Statistics are often calculated with varying amounts of input data. Write a program that takes any number of integers as input, and outputs the average and max.
#    
#    Ex: If the input is:
#    
#    15 20 0 5
#    
#    the output is:
#    
#    10 20
#    
#    Note: For output, round the average to the nearest integer.

# Solution:

# Get raw input and convert to list of ints
nums = [int(i) for i in input().split()]

# Output max and average
print(f'{sum(nums)//len(nums)} {max(nums)}')

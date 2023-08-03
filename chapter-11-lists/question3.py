#     11.18 LAB: Elements in a range
#    
#    Write a program that first gets a list of integers from input. That list is followed by two more integers representing lower and upper bounds of a range. Your program should output all integers from the list that are within that range (inclusive of the bounds).
#    
#    Ex: If the input is:
#    
#    25 51 0 200 33
#    0 50
#    
#    the output is:
#    
#    25 0 33 
#    
#    The bounds are 0-50, so 51 and 200 are out of range and thus not output.
#    
#    For coding simplicity, follow each output integer by a space, even the last one. Do not end with newline.


user_input = input()
user_input2 = input()

# determine limits based on input
limits = [int (i) for i in user_input2.split()]

# determine numbers in range based on input
nums = [int (i) for i in user_input.split() if ((int(limits[0]) <= int(i)) and (int(i) <= int(limits[1])))]

#print output
for num in nums:
    print(f'{num}', end=' ')

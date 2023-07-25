# 33.7 LAB: Smallest number
# Instructor note:
# The skills required for this lab are covered in Chapter 5. Branching. To successfully complete this lab, review the content of Chapter 5, as well as the preceding chapters, and complete the Challenge Activities associated.

# Write a program whose inputs are three integers, and whose output is the smallest of the three values.

# Ex: If the input is:

# 7
# 15
# 3
# the output is:

# 3

# Solution: Take all inputs as members of a list, this allows you to utilized the built in min function 
# without needing to write your own min function.

nums = []
nums.append(int(input()))
nums.append(int(input()))
nums.append(int(input()))
print(min(nums))

# If you don't want to use the built in min function (which you really should):

# min_val = nums[0]

# if nums[1] < min_val:
#    min_val = nums[1]
# elif nums[2] < min_val:
#    min_val = nums[2]
# print(min_val)

# 33.12 LAB: Calculate average

# Complete the calc_average() function that has an integer list parameter and returns the average value of the elements in the list as a float.

# Ex: If the input list is:

# 1 2 3 4 5
# then the returned average will be:

# 3.0

# Solution:

def calc_average(nums):
    return (sum(nums) / len(nums))
    
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    print(calc_average(nums))   # calc_average() should return 3.0
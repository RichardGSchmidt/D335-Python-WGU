#33.4 LAB: Driving costs

# Driving is expensive. 
# Write a program with a car's gas mileage (miles/gallon) 
# and the cost of gas (dollars/gallon) as floating-point 
# input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

# Output each floating-point value with two digits after the 
# decimal point, which can be achieved as follows:
# print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

# Ex: If the input is:

# 20.0
# 3.1599

# where the gas mileage is 20.0 miles/gallon and the cost of gas is $3.1599/gallon, the output is:

# 3.16 11.85 79.00


mpg = float(input())
dpg = float(input())

miles20 = 20 * dpg / mpg
miles75 = 75 * dpg / mpg
miles500 = 500 * dpg / mpg

print(f'{miles20:.2f} {miles75:.2f} {miles500:.2f}')
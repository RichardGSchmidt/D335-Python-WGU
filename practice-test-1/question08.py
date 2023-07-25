# 33.8 LAB: Exact change
# Instructor note:
# The skills required for this lab are covered in Chapter 5. Branching. 
# To successfully complete this lab, review the content of Chapter 5, 
# as well as the preceding chapters, and complete the Challenge Activities associated.

# Write a program with total change amount as an integer input, 
# and output the change using the fewest coins, one coin type per line. 
# The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. 
# Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

# Ex: If the input is:

# 0 
# (or less than 0), the output is:

# No change 
# Ex: If the input is:

# 45
# the output is:

# 1 Quarter
# 2 Dimes

#Variable Declaration

dollars = 0
quarter = 0
dimes = 0
nickles = 0
cents = 0

#User Input
cents = int(input())

#The first if statement fulfills requirement:

# Ex: If the input is:

# 0 
# (or less than 0), the output is:

# No change 


#  
if cents <= 0:
    print("No change")
else:

    # Assignment of values for each currency size
    # starting from greatest to least:

    dollars = cents // 100

    # which is the even amount of dollars
    # in the total cent amount.


    # The total cents is then updated the modulo of the
    # currency size:  

    cents = cents % 100

    # The process is then logically repeated for all 
    # currency divisions:

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

# Total change amounts are now correctly calculated
# The following if statements output the data in the
# required format:

if dollars > 0:
    if dollars == 1:
        print(f'{dollars} Dollar')
    else:
        print(f'{dollars} Dollars')
if quarters > 0:
    if quarters == 1:
        print(f'{quarters} Quarter')
    else:
        print(f'{quarters} Quarters')
if dimes != 0:
    if dimes > 1:
        print(f'{dimes} Dime')
    else:
        print(f'{dimes} Dimes')
if nickels > 0:
    if nickels == 1:
        print(f'{nickels} Nickel')
    else:
        print(f'{nickles} Nickels')
if cents > 0:
    if cents == 1:
        print(f'{cents} Penny')
    else:
        print(f'{cents} Pennies')
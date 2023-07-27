#    34.15 PRACTICE: Import custom module
#   Instructions:
#   
#   Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
#   Task:
#   
#   Create a solution that accepts an integer input representing the age of a pig. Import the existing module pigAge and use its pre-built pigAge_converter() function to calculate the human equivalent age of a pig. A year in a pig's life is equivalent to five years in a human's life. Output the human-equivalent age of the pig.
#   
#   The solution output should be in the format
#   
#   input_pig_age is converted_pig_age in human years
#   
#   Sample Input/Output:
#   
#   If the input is
#   
#   8
#   
#   then the expected output is
#   
#   8 is 40 in human years

#   Solution (NOTE: this code will NOT work outside of the zylabs environment)



import pigAge
input_pig_age = int(input())

# IMPORTANT: Know how to find this function in a module with the help() function.
converted_pig_age = pigAge.pigAge_converter(input_pig_age)

print(f'{input_pig_age} is {converted_pig_age} in human years')

#    34.14 PRACTICE: Math module
#   Instructions:
#   
#   Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
#   Task:
#   
#   Create a solution that accepts an integer input. Import the built-in module math and use its factorial() method to calculate the factorial of the integer input. Output the value of the factorial, as well as a Boolean value identifying whether the factorial output is greater than 100.
#   
#   The solution output should be in the format
#   
#   factorial_value
#   Boolean_value
#   
#   Sample Input/Output:
#   
#   If the input is
#   
#   10
#   
#   then the expected output is
#   
#   3628800
#   True
#   
#   Alternatively, if the input is
#   
#   3
#   
#   then the expected output is
#   
#   6
#   False

# This is pretty straightforward, just import the
#   math module and use math.factorial to get your
#   computed result, then assign a bool based on
#   that value.
import math
user_input = int(input())
input_fact = math.factorial(user_input)
is_greater100 = True if input_fact > 100 else False

print(input_fact)
print(is_greater100)
#    34.13 PRACTICE: Manipulate CSV files
#   Instructions:
#   
#   Create a Python solution to the following task. Ensure that the solution produces output in exactly the same format shown in the sample(s) below, including capitalization and whitespace.
#   Task:
#   
#   Create a solution that accepts an input identifying the name of a CSV file, for example, "input1.csv". Each file contains two rows of comma-separated values. Import the built-in module csv and use its open() function and reader() method to create a dictionary of key:value pairs for each row of comma-separated values in the specified file. Output the file contents as two dictionaries.
#   
#   The solution output should be in the format
#   
#   {'key': 'value', 'key': 'value', 'key': 'value'}
#   {'key': 'value', 'key': 'value', 'key': 'value'}
#   
#   Sample Input/Output:
#   
#   If the input is
#   
#   input1.csv
#   
#   then the expected output is
#   
#   {'a': '100', 'b': '200', 'c': '300'}
#   {'bananas': '1.85', 'steak': '19.99', 'cookies': '4.52'}
#   
#   Alternatively, if the input is
#   
#   input2.csv
#   
#   then the expected output is
#   
#   {'d': '400', 'e': '500', 'f': '600'}
#   {'celery': '2.81', 'milk': '4.34', 'bread': '5.63'}

import csv
file_name = input()
dictionary1 = {}
dictionary2 = {}

# File IO, delimiter isn't needed in this case, but I've used it anyways
#   because it's important to remember how it works in case you are working
#   with a different seperator.
with open(file_name, 'r') as file_in:
    intake = csv.reader(file_in, delimiter = ',')

# Processing the intake file and stripping whitespace    
for i, row in enumerate(intake):
    if i == 0:
        for item in range(0, len(row), 2):
            dictionary1[row[item].strip()] = row[item+1].strip()
    else:
        for item in range(0, len(row), 2):
            dictionary2[row[item].strip()] = row[item+1].strip()

print(dictionary1)
print(dictionary2)

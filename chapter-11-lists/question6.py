#     11.19 LAB: Contact list
#    
#    A contact list is a place where you can store a specific contact with other associated information such as a phone number, email address, birthday, etc. Write a program that first takes in word pairs that consist of a name and a phone number (both strings), separated by a comma. That list is followed by a name, and your program should output the phone number associated with that name. Assume the search name is always in the list.
#    
#    Ex: If the input is:
#    
#    Joe,123-5432 Linda,983-4123 Frank,867-5309
#    Frank
#    
#    the output is:
#    
#    867-5309

# Solution:

# take inputs
user_input1 = input()
user_input2 = input()

# varible declaration
phone_directory = {}
search_key = user_input2

# split the input into tokens
tokens = user_input1.split()

# create a dictionary of phone numbers
# based on token values
for token in tokens:
    # split the token into name and phone number
    temp = token.split(',')
    # add the name and phone number to the dictionary
    phone_directory[temp[0]] = temp[1]

# print the phone number associated with the name
print(phone_directory[search_key])
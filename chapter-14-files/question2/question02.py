#    14.9 LAB: Sorting TV Shows (dictionaries and lists)
#    Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. 
#    The input file contains an unsorted list of number of seasons followed by the corresponding TV show. 
#    Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, 
#    and a list of TV shows are the values (since multiple shows could have the same number of seasons).
#    
#    Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt. 
#    Separate multiple TV shows associated with the same key with a semicolon (;), ordering by appearance in the input file. 
#    Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.
#    
#    Ex: If the input is:
#    
#    file1.txt
#    and the contents of file1.txt are:
#    
#    20
#    Gunsmoke
#    30
#    The Simpsons
#    10
#    Will & Grace
#    14
#    Dallas
#    20
#    Law & Order
#    12
#    Murder, She Wrote
#    the file output_keys.txt should contain:
#    
#    10: Will & Grace
#    12: Murder, She Wrote
#    14: Dallas
#    20: Gunsmoke; Law & Order
#    30: The Simpsons
#    and the file output_titles.txt should contain:
#    
#    Dallas
#    Gunsmoke
#    Law & Order
#    Murder, She Wrote
#    The Simpsons
#    Will & Grace
#    Note: There is a newline at the end of each output file, and file1.txt is available to download.

# Solution:

# Varible Declaration Block
input_file = input()
my_dict = {}
out_keys = 'output_keys.txt'
out_titles = 'output_titles.txt'
titles = []

# with open block takes in lines from the file
with open(input_file, 'r') as file_in:
    lines = file_in.readlines()

# For every other line read, (interval of 2)
#   Add the Key and the value inside a list to the dictionary if the key isn't already in the dictionary.
#   If the key is in the dictionary updates the key by appending the value to the existing value's list.
for i in range(0, len(lines), 2):
    # words from the line are stripped to prevent unwanted whitespace such as leading spaces or newlines (\n's) 
    #   from being entered into the dictionary.
    my_key = int(lines[i].strip())
    my_value = lines[i+1].strip()
    if my_key in my_dict:
        my_dict[my_key].append(my_value)
    else:
        my_dict[my_key] = [my_value]
    
    titles.append(my_value)

# Sorts the dictionary based on key (seasons run)
my_dict = sorted(my_dict.items())

out_str = ''


# This assembles a string to export output_keys.txt 
for i in range(len(my_dict)):
    out_str += str(my_dict[i][0])
    for j in range(len(my_dict[i][1])):
        sep_str = ': '
        if j > 0:
            sep_str = '; '
        out_str += sep_str + my_dict[i][1][j]
    out_str += '\n'

# Exports string into the output_keys.txt    
with open(out_keys, 'w') as file_out:
    file_out.write(out_str)
# print(out_str) # test outputs, no effect on grading, but I would disable 
# this on the real test.

# Builds string for output into out_titles.txt
out_str = ''
titles.sort()
for title in titles:
    out_str += title + '\n'
# print(out_str) # test outputs, no effect on grading, but I would disable 
# this on the real test.

# Exports string into out_titles.txt
with open(out_titles, 'w') as file_out:
    file_out.write(out_str)
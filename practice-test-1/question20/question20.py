#    33.20 LAB: Word frequencies (lists)
#    Instructor note:
#    The skills required for this lab are covered in Chapter 14. Files. To successfully complete this lab, review the content of Chapter 14, as well as the preceding chapters, and complete the Challenge Activities associated.
#    
#    Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method. The file contains a list of words separated by commas. Your program should output the words and their frequencies (the number of times each word appears in the file) without any duplicates.
#    
#    Ex: If the input is:
#    
#    input1.csv
#    and the contents of input1.csv are:
#    
#    hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
#    the output is:
#    
#    hello 1
#    cat 2
#    man 2
#    hey 2
#    dog 2
#    boy 2
#    Hello 1
#    woman 1
#    Cat 1
#    Note: There is a newline at the end of the output, and input1.csv is available to download.

import csv

file_name = input()
out_str = ''
word_dict = {}

with open(file_name, 'r') as file_in:
    intake = csv.reader(file_in, delimiter=",")
    for row in intake:
        for field in row:
            # for each field in each row
            # if it isn't in the dictionary
            # add it, otherwise increment the key
            # by one.
            if field not in word_dict:
                word_dict[field] = 1
            else:
                word_dict[field] += 1

# for every word in the dictionary print the word and the count value, using the word as the key.
for word in word_dict:
    print(f'{word} {word_dict[word]}')
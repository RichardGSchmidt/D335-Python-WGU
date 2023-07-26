#    14.10 LAB: Course Grade
#   
#   Write a program that reads the student information from a tab separated values (tsv) file. The program then creates a text file that records the course grades of the students. Each row of the tsv file contains the Last Name, First Name, Midterm1 score, Midterm2 score, and the Final score of a student. A sample of the student information is provided in StudentInfo.tsv. Assume the number of students is at least 1 and at most 20. Assume also the last names and first names do not contain whitespaces.
#   
#   The program performs the following tasks:
#   
#       Read the file name of the tsv file from the user.
#       Open the tsv file and read the student information.
#       Compute the average exam score of each student.
#       Assign a letter grade to each student based on the average exam score in the following scale:
#           A: 90 =< x
#           B: 80 =< x < 90
#           C: 70 =< x < 80
#           D: 60 =< x < 70
#           F: x < 60
#       Compute the average of each exam.
#       Output the last names, first names, exam scores, and letter grades of the students into a text file named report.txt. Output one student per row and separate the values with a tab character.
#       Output the average of each exam, with two digits after the decimal point, at the end of report.txt. Hint: Use the format specification to set the precision of the output.
#   
#   Ex: If the input of the program is:
#   
#   StudentInfo.tsv
#   
#   and the contents of StudentInfo.tsv are:
#   
#   Barrett    Edan    70  45  59
#   Bradshaw    Reagan  96  97  88
#   Charlton    Caius   73  94  80
#   Mayo    Tyrese  88  61  36
#   Stern    Brenda  90  86  45
#   
#   the file report.txt should contain:
#   
#   Barrett    Edan    70  45  59  F
#   Bradshaw    Reagan  96  97  88  A
#   Charlton    Caius   73  94  80  B
#   Mayo    Tyrese  88  61  36  D
#   Stern    Brenda  90  86  45  C
#   
#   Averages: midterm1 83.40, midterm2 76.60, final 61.60


# Solution:

# The CSV module will be used to read the tsv file.
import csv

# Function to read a file and return a list containing the contents
def read_file(user_input):
    # declare output varible
    grades_out = []
    with open(user_input, 'r') as file_in:

        # *The delimiter attribute is something you should remember
        grades_in = csv.reader(file_in, delimiter = '\t')

        # Converting the object to a list.  Returning grades_in would 
        #   return a raw csv class object, which is much more awkward 
        #   to manipulate than a list.
        for row in grades_in:
            grades_out.append(row)
    
    return(grades_out)

# Varible declarations and input function calls
grades = read_file(input())
exam_totals = [0,0,0]
exam_averages = [0.0,0.0,0.0]
fileout = ''

# A lot of what is coming up is hard to decipher at first, but
#   each record (i) is made of 5 parts, 0-4 whos index we'll call j.
#   
#       Like this:
#     i
#     |
#     V
# j->    [0]         [1]    [2]  [3] [4]
#    [0] Barrett     Edan    70   45  59
#    [1] Bradshaw    Reagan  96   97  88
#    [2] Charlton    Caius   73   94  80
#    [3] Mayo        Tyrese  88   61  36
#    [4] Stern       Brenda  90   86  45

# To find the final grade for each student we take the sum of
# the values at j indexes 2, 3 and 4 and divide by 3.
# Then a branching statement determines the letter grade.

for i in range(len(grades)):
    grade = (int(grades[i][2])+int(grades[i][3])+int(grades[i][4])) / 3
    letter_grade = ''
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    grades[i].append(letter_grade)

    # totals taken here are used later for exam averages
    exam_totals[0] += int(grades[i][2])
    exam_totals[1] += int(grades[i][3])
    exam_totals[2] += int(grades[i][4])

# For loop calculates the exam averages
for i in range(3):
    exam_averages[i] = exam_totals[i] / len(grades)

# Each line is added according to required format.
#   fileout is initialy a blank string (declared above).
for i in range(len(grades)):
    fileout += f'{grades[i][0]}\t{grades[i][1]}\t{grades[i][2]}\t{grades[i][3]}\t{grades[i][4]}\t{grades[i][5]}\n'

# Closing line according to format, notice the leading newline
#   that is used to double space the lines as per output requirements. 
fileout += f'\nAverages: midterm1 {exam_averages[0]:.2f}, midterm2 {exam_averages[1]:.2f}, final {exam_averages[2]:.2f}\n'

with open('report.txt', 'w') as file_out:
    file_out.write(fileout)
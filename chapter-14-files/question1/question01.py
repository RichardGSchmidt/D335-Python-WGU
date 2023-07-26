#    14.8 LAB: Words in a range (lists)
#    Write a program that first reads in the name of an input file, followed by two strings representing the lower and upper bounds of a search range. The file should be read using the file.readlines() method. The input file contains a list of alphabetical, ten-letter strings, each on a separate line. Your program should output all strings from the list that are within that range (inclusive of the bounds).
#    
#    Ex: If the input is:
#    
#    input1.txt
#    ammoniated
#    millennium
#    and the contents of input1.txt are:
#    
#    aspiration
#    classified
#    federation
#    graduation
#    millennium
#    philosophy
#    quadratics
#    transcript
#    wilderness
#    zoologists
#    the output is:
#    
#    aspiration
#    classified
#    federation
#    graduation
#    millennium
#    Notes:
#    
#    There is a newline at the end of the output.
#    All input files are hosted in the zyLab and file names can be directly referred to. input1.txt is available to download so that the contents of the file can be seen.
#    In the tests, the first word input always comes alphabetically before the second word input.


file_name = input()
start_term = input()
final_term = input()

with open(file_name, 'r') as myfile:
    lines = myfile.readlines()
    for line in lines:
        # whitespace is first stripped for comparison
        # (otherwise you could this behavior: 'millenium\n' <= 'millenium' 
        # as user inputs do not have \n on the end) and the file does.
        line = line.strip()

        # Simple range checks are used to see if the word should be output
        if ((start_term <= line) and (line <= final_term)):
            print(line, end='\n')
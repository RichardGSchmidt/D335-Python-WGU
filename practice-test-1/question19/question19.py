#    33.19 LAB: Thesaurus
#    Instructor note:
#    The skills required for this lab are covered in Chapter 14. Files. To successfully complete this lab, review the content of Chapter 14, as well as the preceding chapters, and complete the Challenge Activities associated.
#    
#    Given a set of text files containing synonyms for different words, complete the main program to output the synonyms for a specific word. Each text file contains synonyms for the word specified in the file’s name, and each row within the file lists the word’s synonyms that begin with the same letter, separated by a space. The program reads a word and a letter from the user and opens the text file associated with the input word. The program then stores the contents of the text file into a dictionary predefined in the program. Finally the program searches the dictionary and outputs all the synonyms that begin with the input letter, one synonym per line, or a message if no synonyms that begin with the input letter are found.
#    
#    Hints: Use the first letter of a synonym as the key when storing the synonym into the dictionary. Assume all letters are in lowercase.
#    
#    Ex: If the input of the program is:
#    
#    educate
#    c
#    the program opens the file educate.txt, which contains:
#    
#    brainwash brief
#    civilize coach cultivate
#    develop discipline drill
#    edify enlighten exercise explain
#    foster
#    improve indoctrinate inform instruct
#    mature
#    nurture
#    rear
#    school
#    train tutor
#    then the program outputs:
#    
#    civilize
#    coach
#    cultivate
#    Ex: If the input of the program is:
#    
#    educate
#    a
#    then the program outputs:
#    
#    No synonyms for educate begin with a.

synonyms = {}
word_ref = input().strip()
char_ref = input().strip()

with open(word_ref + '.txt', 'r') as file_in:
    lines = file_in.readlines()
    for line in lines:
        wordlist = []
        for word in line.split():
            wordlist.append(word)
        synonyms[word[0]] = wordlist


if char_ref not in synonyms:
    print(f'No synonyms for {word_ref} begin with {char_ref}.')
else:
    out_str = ''
    for word in synonyms[char_ref]:
        out_str += f'{word}\n'
    print(f'{out_str}', end='')
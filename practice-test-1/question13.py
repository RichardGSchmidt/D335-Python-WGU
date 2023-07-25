#    33.13 LAB: Warm up: Text analyzer & modifier
#    Instructor note:
#    The skills required for this lab are covered in Chapter 10. Strings. To successfully complete this lab, review the content of Chapter 10, as well as the preceding chapters, and complete the Challenge Activities associated.
#
#    (1) Prompt the user to enter a string of their choosing. Output the string. (1 pt)
#
#    Ex:
#
#    Enter a sentence or phrase:
#    The only thing we have to fear is fear itself.
#
#    You entered: The only thing we have to fear is fear itself.
#    (2) Complete the get_num_of_characters() function, which returns the number of characters in the user's string. We encourage you to use a for loop in this function. (2 pts)
#
#    (3) Extend the program by calling the get_num_of_characters() function and then output the returned result. (1 pt)
#
#    (4) Extend the program further by implementing the output_without_whitespace() function. output_without_whitespace() outputs the string's characters except for whitespace (spaces, tabs). Note: A tab is '\t'. Call the output_without_whitespace() function in main(). (2 pts)
#
#    Ex:
#
#    Enter a sentence or phrase: 
#    The only thing we have to fear is fear itself.
#
#    You entered: The only thing we have to fear is fear itself.
#
#    Number of characters: 46
#    String with no whitespace: Theonlythingwehavetofearisfearitself.

def get_num_of_characters(input_str):
    # note the count INCLUDES whitespace characters
    # they ask you to use a for loop, however you could simply
    # output len(input_str)
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

def output_without_whitespace(input_str):
    #output string starts empty
    out_str = ''

    # for each char in the string
    for i in input_str:
        # if the character in the in string isn't a whitespace char
        # concatenate it to the end of the out string.
        if i != ' ' and i != '\n' and i != '\n' and i != '\t':
            out_str += i
    # after the for loop return the completed out string
    return out_str


if __name__ == '__main__':
    user_input = input('Enter a sentence or phrase:\n')
    print()
    print(f'You entered: {user_input}')
    print()
    print(f'Number of characters: {get_num_of_characters(user_input)}')
    print (f'String with no whitespace: {output_without_whitespace(user_input)}')
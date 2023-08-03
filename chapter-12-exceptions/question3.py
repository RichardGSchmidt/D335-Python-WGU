#    12.9 LAB: Exceptions with lists
#   
#   Given a list of 10 names, complete the program that outputs the name specified by the list index entered by the user. Use a try block to output the name and an except block to catch any IndexError. Output the message from the exception object if an IndexError is caught. Output the first element in the list if the invalid index is negative or the last element if the invalid index is positive.
#   
#   Note: Python allows using a negative index to access a list, as long as the magnitude of the index is smaller than the size of the list.
#   
#   Ex: If the input of the program is:
#   
#   5
#   
#   the program outputs:
#   
#   Name: Jane
#   
#   Ex: If the input of the program is:
#   
#   12
#   
#   the program outputs:
#   
#   Exception! list index out of range
#   The closest name is: Johnny
#   
#   Ex: If the input of the program is:
#   
#   -2
#   
#   the program outputs:
#   
#   Name: Tyrese
#   
#   Ex: If the input of the program is:
#   
#   -15
#   
#   the program outputs:
#   
#   Exception! list index out of range
#   The closest name is: Ryley

names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

try:
    if index < -1 * len(names) or index >= len(names):
        # the index error's argument prints inside the except block
        raise IndexError('Exception! list index out of range')
    print(f'Name: {names[index]}')
except IndexError as excpt:
    # selects the closest name to requested index for output
    if index < 0:
        out_str = names[0]
    else:
        out_str = names[len(names)-1]
    # outputs the exception message and the closest name
    print(excpt)
    print(f'The closest name is: {out_str}')


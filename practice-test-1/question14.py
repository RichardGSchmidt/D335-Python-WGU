#    33.14 LAB: Palindrome
# 
#    A palindrome is a word or a phrase that is the same when read both forward and backward. Examples are: "bob," "sees," or "never odd or even" (ignoring spaces). Write a program whose input is a word or phrase, and that outputs whether the input is a palindrome.
#    
#    Ex: If the input is:
#    
#    bob
#    the output is:
#    
#    bob is a palindrome
#    Ex: If the input is:
#    
#    bobby
#    the output is:
#    
#    bobby is not a palindrome
#    Hint: Start by removing spaces. Then check if a string is equivalent to it's reverse.

user_str = input()
palindrome = True
out_str = ''
test_str = ''

# this for loop removes whitespace and assigns it to a string to be tested
for i in user_str:
    if i != ' ' and i != '\n' and i != '\t':
        test_str += i

# this tests the string going to the halfway point 
#   (not including a central value if the number of characters is odd).
#   This is done because in a palindrome you compare the opposite sides
#   against each other.  So when you have checked halfway up the string, you've
#   also checked halfway down the string.
#   (If the number of characters is odd, the central value is always considered a mirror
#   of itself, so there is never a reason to compare it to anything.)
for i in range(len(test_str)//2):

    # Index -1 is the rightmost char while Index 0 is the leftmost char.
    #   They are both the starting points as the loop moves one letter
    #   inward each itteration. If there is a mismatch, the boolean is
    #   set false and the for loop is exited.
    if test_str[0+i] != test_str[-1-i]:
        palindrome = False
        break

# This can also be done without a for loop, but is less computationally efficient:
# 
# if test_str != test_str[::-1]:
#   palindrome = False


if palindrome:
    out_str += f'{user_str} is a palindrome'
else:
    out_str += f'{user_str} is not a palindrome'

print(out_str)
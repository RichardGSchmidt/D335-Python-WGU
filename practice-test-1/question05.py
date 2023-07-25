# 33.5 LAB: Input and formatted output: Right-facing arrow
# Given input characters for an arrowhead and arrow body, print a right-facing arrow.

#Ex: If the input is:

# *
# #
# Then the output is:

#       #
# ******##
# ******###
# ******##
#       #

base_char = input()
head_char = input()

row1 = '      ' + head_char
row2 = 6 * base_char + 2 * head_char
row3 = 6 * base_char + 3 * head_char


print(row1)
print(row2)
print(row3)
print(row2)
print(row1)
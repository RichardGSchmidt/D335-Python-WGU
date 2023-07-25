# 33.6 LAB: Phone number breakdown

# Given an integer representing a 10-digit phone number, output the area code, prefix, and line number using the format (800) 555-1212.

# Ex: If the input is:

# 8005551212
# the output is:

# (800) 555-1212
# Hint: Use % to get the desired rightmost digits. Ex: The rightmost 2 digits of 572 is gotten by 572 % 100, which is 72.

# Hint: Use // to shift right by the desired amount. Ex: Shifting 572 right by 2 digits is done by 572 // 100, which yields 5. (Recall integer division discards the fraction).

# For simplicity, assume any part starts with a non-zero digit. So 0119998888 is not allowed.

phone_number = int(input())

#Solution One:  uses modulo and // as per the hints.
# commented out as it is the more convoluted solution

# area_code = phone_number // 10000000

# three = (phone_number // 10000) % 1000

# four = phone_number % 10000

# print(f'({area_code}) {three}-{four}')

# Solution Two: String Slicing
# This is the faster option. The int is converted to a string, 
# which is then sliced into the requisit components.

phone_str = str(phone_number)
print(f'({phone_str[0:3]}) {phone_str[3:6]}-{phone_str[6:]}')
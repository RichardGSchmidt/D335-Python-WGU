#33.11 LAB: Fibonacci sequence

#The Fibonacci sequence begins with 0 and then 1 follows. 
#All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. 
#Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence. 
#Any negative index values should return -1.

#Ex: If the input is: 7
#the output is: 'fibonacci(7) is 13'


#Solution:
 
def fibonacci(n):
    first = 0
    second = 1
    temp = 0

    # returns -1 if input is below 0:
    if n < 0:
        return -1
    
    # immediate returns if the index is one
    #   of the two predefined start values:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Values are starting at n = 2
    #   doing the for loop once per
    #   iteration above index 0 and 1
    #   (which are the predefined values)
    for i in range(n-1):
        # temp value to store the first value:
        temp = first

        # the first value is updated to be the original second value:
        first = second

        # the second value is then updated with the original first value
        #   added to the original second value:
        second = temp + second

    # Once the loop is complete the top most 
    #   value computed in the sequence (second) is returned:
    return second

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
#The Fibonacci sequence begins with 0 and then 1 follows. 
#All subsequent values are the sum of the previous two, ex: 0, 1, 1, 2, 3, 5, 8, 13. 
#Complete the fibonacci() function, which has an index n as parameter and returns the nth value in the sequence. 
#Any negative index values should return -1.

#Ex: If the input is: 7
#the output is: 'fibonacci(7) is 13'


def fibonacci(n):
    first = 0
    second = 1
    temp = 0
    if n < 0:
        return -1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    for i in range(n-1):
        temp = first
        first = second
        second = temp + second
    return second

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
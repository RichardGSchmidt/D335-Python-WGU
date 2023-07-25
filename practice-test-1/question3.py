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
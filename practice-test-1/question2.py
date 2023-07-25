user_input = input()

while((user_input != 'done') and (user_input != 'd') and (user_input != 'Done')):
    print(user_input[::-1])
    user_input = input()
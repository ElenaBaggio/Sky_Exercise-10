exit_option = 2

while exit_option != 'x':
    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))
    operator = input("enter the operator: ")
    if operator == '+':
        result = num1 + num2
        print(result)
        exit_option = input('press x to exit')
    elif operator == '-':
        result = num1 - num2
        print(result)
        exit_option = input('press x to exit')
    elif operator == '/':
        result = num1 / num2
        print(result)
        exit_option = input('press x to exit')
    elif operator == '*':
        result = num1 * num2
        print(result)
        exit_option = input('press x to exit')
    else:
        print('add a valid operator')






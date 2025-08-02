first_number = int(input('Enter the first number: '))
expression = input('Enter the operation (+, -, *, /): ')
second_number = int(input('Enter the second number: '))

if expression == '+':
    result = first_number + second_number
elif expression == '-':
    result = first_number - second_number
elif expression == '*':
    result = first_number * second_number
elif expression == '/':
    if second_number != 0:
        result = first_number / second_number
    else:
        result = 'Error! Division by zero.'
else:
    result = 'Invalid operator!'

print(f'{first_number} {expression} {second_number} = {result}')

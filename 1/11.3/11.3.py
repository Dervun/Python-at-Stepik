'''
Напишите простой калькулятор, который считывает с пользовательского ввода три строки:
первое число, второе число и операцию, после чего применяет операцию к введённым числам
("первое число" "операция" "второе число") и выводит результат на экран.

Поддерживаемые операции: +, -, /, *, mod, pow, div, где
mod — это взятие остатка от деления,
pow — возведение в степень,
div — целочисленное деление.

Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

Обратите внимание, что на вход программе приходят вещественные числа.
'''
#Good decision:
first = float(input())
second = float(input())
action = input()
operations = {"mod": "%", "div": "//", "pow": "**"}
try:
    print(eval("(" + str(first) + ")" + operations.get(action, action) + str(second)))
except ZeroDivisionError:
    print('Деление на 0!')

#My decision:
'''
a = float(input())
b = float(input())
operand = input()

if operand in ['/', 'mod', 'div'] and b == 0:
    print('Деление на 0!')
elif operand == '+':
    print(a + b)
elif operand == '-':
    print(a - b)
elif operand == '*':
    print(a * b)
elif operand == '/':
    print(a / b)
elif operand == 'mod':
    print(a % b)
elif operand == 'pow':
    print(a ** b)
elif operand == 'div':
    print(a // b)
else:
    print('unknown operand')
'''
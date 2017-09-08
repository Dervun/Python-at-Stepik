'''
Паша очень любит кататься на общественном транспорте, а получая билет, сразу проверяет, счастливый ли ему попался.
Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних трех цифр номера билета.

Однако Паша очень плохо считает в уме, поэтому попросил вас написать программу,
которая проверит равенство сумм и выведет "Счастливый", если суммы совпадают, и "Обычный", если суммы различны.

На вход программе подаётся строка из шести цифр.
'''
#cool decision:
n = list(map(int, list(input())))
print('Счастливый' if sum(n[:3]) == sum(n[3:]) else 'Обычный')

#my decision:
'''
number = input()

if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
    print('Счастливый')
else:
    print('Обычный')
'''
'''
Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.
'''
arr = sorted([int(input()) for i in range(3)])
print(arr[2], arr[0], arr[1], sep='\n')

#other
'''
a = input()
b = input()
c = input()

arr = sorted([a, b, c])
print(arr[2], arr[0], arr[1], sep='\n')
'''
'''
arr = sorted([int(input()), int(input()), int(input())])
print(arr[2], arr[0], arr[1], sep='\n')
'''
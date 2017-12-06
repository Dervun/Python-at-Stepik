"""Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.

Программа принимает на вход две строки одинаковой длины,
на первой строке записаны символы исходного алфавита,
на второй строке — символы конечного алфавита, после чего идёт строка,
которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре,
b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
Получаем следующие строки, которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

"""

# Считываем 4 строки в цикле
original, coding, first_string, second_string = (input() for i in range(4))

# По индексу символа из оригинала берём символ на замену из кодировки,
# для каждого символа из строки, которую нужно закодировать
print(*[coding[original.find(symbol)] for symbol in first_string], sep='')
# Аналогично, только наоборот :D
print(*[original[coding.find(symbol)] for symbol in second_string], sep='')

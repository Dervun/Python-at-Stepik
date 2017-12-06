"""
Напишите программу, которая считывает список чисел list из первой строки и число x из второй строки,
которая выводит все позиции, на которых встречается число x в переданном списке list.

Позиции нумеруются с нуля, если число x не встречается в списке, вывести строку "Отсутствует"
(без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.
"""
arr = [int(i) for i in input().split()]
wanted_value = int(input())
indexes = list(filter(lambda x: arr[x] == wanted_value, range(len(arr))))
print(*indexes if len(indexes) else "Отсутствует".split())

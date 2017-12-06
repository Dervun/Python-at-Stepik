"""
Недавно мы считали для каждого слова количество его вхождений в строку.
Но на все слова может быть не так интересно смотреть, как, например, на наиболее часто используемые.
Напишите программу, которая считывает текст из файла
(в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то,
сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.
"""
from operator import itemgetter  # Это для сортировки массива из кортежей по определённому номеру элемента в кортеже

dictionary = dict()
with open('dataset_3363_3.txt', 'r') as file:
    for line in file:
        print(line)
        for word in line.strip().lower().split():
            print(word)
            dictionary.setdefault(word, 0)
            dictionary[word] += 1

array_of_quantities = [(word, quantity) for word, quantity in dictionary.items()]
array_of_quantities = sorted(array_of_quantities, key=itemgetter(1), reverse=True)
pre_result = sorted([word for (word, quantity) in array_of_quantities if quantity == array_of_quantities[0][1]])
print(array_of_quantities)
print(pre_result)
print(pre_result[0], dictionary[pre_result[0]])

"""
Программа должна считывать одну строку со стандартного ввода и
выводить для каждого уникального слова в этой строке число его повторений (без учёта регистра) в формате "слово количество"
"""

# my decision
dictionary = dict()
for word in input().split():
    dictionary.setdefault(word.lower(), 0)
    dictionary[word.lower()] += 1

for key, value in dictionary.items():
    print(key, value)

# good decision
words = input().lower().split()
[print(word, quantity) for word, quantity in {word:words.count(word) for word in words}.items()]

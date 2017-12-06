"""
Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.
Запишите полученный текст в файл и прикрепите его, как ответ на это задание.
В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
"""
import re

result = open('result.txt', 'w')
with open('dataset_3363_2.txt', 'r') as file:
    line = file.readline().strip()
    print(line)
    code = re.split('(\d*)', line)
    print(code)
    for i in range(0, len(code) - 1, 2):
        result.write(code[i] * int(code[i + 1]))
result.close()

"""
Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2',
то есть группы одинаковых символов исходной строки заменяются на этот символ
и количество его повторений в этой позиции строки.
"""
# My decision:
originalText = input() + '$'  # End of string indicated by '$'
currentQuantity = 0
currentSymbol = originalText[0]
for c in originalText:
    if c != currentSymbol:
        print(currentSymbol, currentQuantity, sep='', end='')
        currentSymbol = c
        currentQuantity = 0
    currentQuantity += 1

# Cool decision :D
'''
import itertools
print("".join([k+str(len(list(g))) for k, g in itertools.groupby(input())]))
'''

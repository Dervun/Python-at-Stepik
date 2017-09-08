'''
Напишите программу, которая считывает с клавиатуры два числа a и b,
считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a;b],
которые делятся на 33.
'''
# My decision:
leftLimit, rightLimit = (int(input()) for _ in range(2))
totalCount = 0
totalSum = 0

for i in range(leftLimit, rightLimit + 1):
    if i % 3 == 0:
        totalCount += 1
        totalSum += i
print(totalSum / totalCount)

# Good decision:
'''
x = [x for x in range(int(input()), int(input()) + 1) if x % 3 == 0]
print(sum(x) / len(x))
'''

# Cool decision:
'''
a, b = int(input()), int(input())
a += -a % 3
b -= b % 3
print((a + b) / 2)
'''

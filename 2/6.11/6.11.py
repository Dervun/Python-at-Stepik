"""
Выведите таблицу размером n×n, заполненную числами от 1 до n^2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке.
"""
n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]

vertical_rotation = -1
horizontal_rotation = 1
current_value = 1
x = 0
y = 0
while current_value <= n ** 2:
    while (0 <= y < n) and arr[x][y] == 0:
        arr[x][y] = current_value
        current_value += 1
        y += horizontal_rotation
    y -= horizontal_rotation
    horizontal_rotation *= -1
    x += vertical_rotation
    while (0 <= x < n) and arr[x][y] == 0:
        arr[x][y] = current_value
        current_value += 1
        x += vertical_rotation
    x -= vertical_rotation
    vertical_rotation *= -1
    y += horizontal_rotation

for i in arr:
    print(*i)



# Найти наименьшее общее кратное
a = int(input())
b = int(input())

aa = a
bb = b
while aa % bb != 0:
    r = aa % bb
    aa = bb
    bb = r

print(int(a * b / bb))

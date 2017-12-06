"""
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и
выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков

Порядок вывода команд произвольный.
Sample Input:
3
Зенит;3;Спартак;1
Спартак;1;ЦСКА;1
ЦСКА;0;Зенит;2

Sample Output:
Зенит:2 2 0 0 6
ЦСКА:2 0 1 1 1
Спартак:2 0 1 1 1
"""

games = [input().split(';') for i in range(int(input()))]
table = dict()
for gamer1, score1, gamer2, score2 in games:
    score1 = int(score1)
    score2 = int(score2)
    for gamer in (gamer1, gamer2):
        table.setdefault(gamer, {'win': 0, 'draw': 0, 'defeat': 0})
    if score1 > score2:
        table[gamer1]['win'] += 1
        table[gamer2]['defeat'] += 1
    elif score1 < score2:
        table[gamer1]['defeat'] += 1
        table[gamer2]['win'] += 1
    else:
        table[gamer1]['draw'] += 1
        table[gamer2]['draw'] += 1

for gamer, results in table.items():
    print(gamer + ':' + str(sum(results.values())) + ' ' +
          str(results['win']) + ' ' +
          str(results['draw']) + ' ' +
          str(results['defeat']) + ' ' +
          str(3*results['win'] + results['draw']))

import random

###     сортировка списка серий и очистка "0-го сезона"
with open('r_l.txt') as file:
    spisok = [row.strip() for row in file]  # записываем файл в spisok
sort_spisok = []

for episode in spisok:
    # print('%s' % episode)
    if int(episode) % 10 != 0:
        sort_spisok.append(episode)     # создаем список из серий не кратных 10

sort_spisok.sort()  # сортируем новый список по порядку
with open('r_l.txt', 'w') as file:
    file.write('\n'.join(sort_spisok))  # записываем новый список в файл


###   сортировка списка просмотренных серий
with open('watched_list_0.txt') as file:
    watched_spisok = [row.strip() for row in file]
watched_spisok.sort()
with open('watched_list_0.txt', 'w') as file:
    file.write('\n'.join(watched_spisok))


print("Runned")
file.close()
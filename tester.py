import random


# spisok = list(range(11,12))
spisok = [10, 11, 12, 13]
sort_spisok = []

for episode in spisok:
    # if spisok[episode] != 0:
    sort_spisok.extend(spisok[episode])
    print('%s' % spisok[episode])

with open('r_l.txt', 'w') as file:
    file.write('\n'.join(sort_spisok))


###   сортировка списка просмотренных серий
with open('watched_list_0.txt') as file:
    watched_spisok = [row.strip() for row in file]
watched_spisok.sort()


print("Runned")
file.close()
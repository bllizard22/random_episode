import random
spisok = list(range(11,15))#250))
file = open('random_list.txt', 'w')

for item in spisok:
    if item == 1:
        file.write('%s' %item)
    else:
        file.write('\n%s' % item)

f = open('watched_list.txt', 'w')
f.close()

print('Runned')
file.close()
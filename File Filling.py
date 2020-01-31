import random
spisok = list(range(11,15))#250))
file = open('random_list.txt', 'w')

for item in spisok:
    file.write("%s\n" % item)

f = open('watched_list.txt', 'w')
f.close()

print("Runned")
file.close()
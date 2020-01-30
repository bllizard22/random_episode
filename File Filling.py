import random
spisok = list(range(10,21))
file = open('random_list.txt', 'w')

for item in spisok:
    file.write("%s\n" % item)
print("Runned")
file.close()
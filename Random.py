import random

def remove_episode(ep_index):
    print(episode)
    del spisok[ep_index]
    with open("random_list.txt", "w") as file:
        file.write("\n".join(spisok))
    return self

with open("random_list.txt") as file:
    spisok = [row.strip() for row in file]  #открываем список всех серий и записываем его в spisok
with open("watched_list.txt") as file:
    watched_spisok = [row.strip() for row in file]  #записываем список просмотренных серий в watched_list
# watched_list = open('watched_list.txt', 'a')
# random_list = open('random_list.txt', 'a')

while 1:
    print('Enter command')
    input_data = input()
    if input_data == 'run':
        flag = 0
        while flag == 0:
            episode = random.choice(spisok)
            ep_index = spisok.index(episode)
            if episode not in watched_spisok:
                watched_list = open('watched_list.txt', 'a')
                watched_list.write("\n%s" % episode)
                remove_episode(ep_index)
                watched_list.close()
                flag = 1
    elif input_data == "add":
        print('Enter episode number\n')
        input_episode = input()
        ep_index = spisok.index(input_episode)
        if episode not in watched_spisok:
            watched_list = open('watched_list.txt', 'a')
            watched_list.write("\n%s" % episode)
            print(episode)
            del spisok[ep_index]
            with open("random_list.txt", "w") as file:
                file.write("\n".join(spisok))
            watched_list.close()
            flag = 1


print("Runned")

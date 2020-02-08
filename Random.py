import random

# удаляем запись о выпавшей серии из list
# и презаписываем файл списка просмотренных эпизодов
def Remove_episode(episode):
    __ep_index = spisok.index(episode)
    del spisok[__ep_index]
    with open('random_list.txt', 'w') as file:
        file.write('\n'.join(spisok))

# добавляем выпавшую серию в список просмотренного
def Add_episode(episode):
    watched_list = open('watched_list.txt', 'a')
    if len(watched_spisok) == 0:
        watched_list.write('%s' % episode)
        print('Первая просмотренная серия!')
    else:
        watched_list.write('\n%s' % episode)
        print('Новая серия добавлена в просмотренные')
    watched_spisok.append(episode)
    watched_list.close()

def Reset_list():
    print('Непросмотренных серий не осталось')
    print('Введите reset для сброса всего списка серий')
    if input() == 'reset':
        print('Вы уверены? Если да, то введите yes')
        if input() == 'yes':
            sorted_spisok = []    # избаляемся от повторяющихся записей
            for episode in watched_spisok:
                if episode not in sorted_spisok:
                    sorted_spisok.append(episode)
            sorted_spisok.sort()    #сортируем по возрастанию
            with open('random_list.txt', 'w') as file:
                file.write('\n'.join(sorted_spisok))
            print('Готово! Список упешно сброшен')
            f = open('watched_list.txt', 'w')
            f.close()

def Return_episode(episode):
    if episode in watched_spisok:
        spisok.append(episode)
        __ep_index = spisok.index(episode)
        del spisok[__ep_index]
        with open('random_list.txt', 'w') as file:
            file.write('\n'.join(spisok))
    else:
        print('Серия не помечена как просмотренная')


with open('random_list.txt') as file:
    spisok = [row.strip() for row in file]  #открываем список всех серий и записываем его в spisok
with open('watched_list.txt') as file:
    watched_spisok = [row.strip() for row in file]  #записываем список просмотренных серий в watched_list
    
watched_spisok.sort()

while True:
    print('Введите команду "run" для выбора новой серии')
    print('Используйте "add" чтобы пометить серию как просмотренную')
    print('Команда "return" убирает пометку о просмторе с серии')
    print('Для закрытия программы введите "stop"')
    input_data = input()

    # run выбирает случайную серию из списка и проверяет
    # не находится ли она в списке просмотренного
    if input_data == 'run':
        flag = 0
        if len(spisok) == 0:
            Reset_list()
            with open('random_list.txt') as file:
                spisok = [row.strip() for row in file]
            with open('watched_list.txt') as file:
                watched_spisok = [row.strip() for row in file]
            flag = 1
        while flag == 0:
            episode = random.choice(spisok)
            ep_index = spisok.index(episode)
            if episode not in watched_spisok:
                print(episode)
                Remove_episode(episode)
                Add_episode(episode)
                flag = 1
            else:
                Remove_episode(episode)

    # add запрашивает номер серии, вносит ее в список просмотренных
    # и удаляет из основного списка
    elif input_data == 'add':
        flag_data = 1
        while flag_data != 0:
            print('Для выхода введите "0"')
            print('Введите номер серии:')
            episode = input()
            if episode != '0':
                if episode not in watched_spisok:
                    print('%s серия помечена как просмотренная' % episode)
                    Add_episode(episode)
                    Remove_episode(episode)
                else:
                    print('Эта серия уже в списке просмотренных')
            else:
                flag_data = 0

    # return удаляет серию из списка просмотренных
    # и возвращает ее в список оставшихся серий
    elif input_data == 'return':
        flag_data = 1
        while flag_data != 0:
            print('Для выхода введите "0"')
            print('Введите номер серии:')
            episode = input()
            if episode != '0':
                print('%s серия убрана из просмотренных' % episode)
                Return_episode(episode)
            else:
                flag_data = 0

    # останавливает выполнение кода
    elif input_data == 'stop':
        break

    # все прочие команды вызывают сообщение о количестве
    # оставшихся серий
    else:
        with open('random_list.txt') as file:
            spisok = [row.strip() for row in file]
        print('Осталось непросмотренных серий %s' % len(spisok))

print('Runned')

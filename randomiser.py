import random


def generate(eps):
    spisok = list(range(11,eps+11))#250))
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


class Randomiser():

    def __init__(self):
        # super(Randomiser, self).__init__()
        try:
            with open('random_list.txt') as file:
                self.rand_list = [row.strip() for row in file]  #открываем список всех серий и записываем его в rand_list
            with open('watched_list.txt') as file:
                self.watched_list = [row.strip() for row in file]  #записываем список просмотренных серий в watched_list
            return
        except FileNotFoundError:
            generate(10)
            with open('random_list.txt') as file:
                self.rand_list = [row.strip() for row in file]  #открываем список всех серий и записываем его в rand_list
            with open('watched_list.txt') as file:
                self.watched_list = [row.strip() for row in file]  #записываем список просмотренных серий в watched_list
            return


    # удаляем запись о выпавшей серии из list
    # и презаписываем файл списка просмотренных эпизодов
    def remove_episode(self, episode):
        __ep_index = self.rand_list.index(episode)
        del self.rand_list[__ep_index]
        with open('random_list.txt', 'w') as file:
            file.write('\n'.join(self.rand_list))
        return

    # добавляем выпавшую серию в список просмотренного
    def add_episode(self, episode):
        watched_list_temp = open('watched_list.txt', 'a')
        if len(self.watched_list) == 0:
            watched_list_temp.write('%s' % episode)
        else:
            watched_list_temp.write('\n%s' % episode)
        watched_list_temp.close()
        self.watched_list.append(episode)
        return

    # сбрасываем список просмотренных серий 
    def reset_list(self):
        sorted_list = []    # избаляемся от повторяющихся записей
        for episode in self.watched_list:
            if episode not in sorted_list:
                sorted_list.append(episode)
        sorted_list.sort()    #сортируем по возрастанию
        with open('random_list.txt', 'w') as file:
            file.write('\n'.join(sorted_list))
        f = open('watched_list.txt', 'w')
        f.close()
        with open('random_list.txt') as file:
            self.rand_list = [row.strip() for row in file]
        with open('watched_list.txt') as file:
            self.watched_list = [row.strip() for row in file]
        msg = 'Готово!\nСписок сброшен'
        return msg

    # помечаем серию непросмотренной
    def return_episode(self, episode):
        if episode in self.watched_list:
            self.rand_list.append(episode)
            __ep_index = self.rand_list.index(episode)
            del self.rand_list[__ep_index]
            with open('random_list.txt', 'w') as file:
                file.write('\n'.join(self.rand_list))
        return

    def clean(self):
        self.cleaned_list = []      
        for line in self.rand_list:
            if line in self.watched_list or line == '\n' or line == '':
                self.remove_episode(line)
        print ('episodes left ', len(self.rand_list))
        self.watched_list.sort()
        return f'Осталось серий:\n{len(self.rand_list)}'

    # run выбирает случайную серию из списка и проверяет
    # не находится ли она в списке просмотренного
    def run(self):
        if len(self.rand_list) == 0:
            return 'Нужно\nсбросить список', True
        flag = 0
        while flag == 0:
            episode = random.choice(self.rand_list)
            ep_index = self.rand_list.index(episode)
            if episode not in self.watched_list:
                # print(episode)
                self.remove_episode(episode)
                self.add_episode(episode)
                flag = 1
            else:
                self.remove_episode(episode)
        msg = episode
        return msg, False

        # add запрашивает номер серии, вносит ее в список просмотренных
        # и удаляет из основного списка
    def add(self, ep_input):
        episode = ep_input
        if episode not in self.watched_list:
            if episode in self.rand_list:
                msg = f'{episode} серия\nпомечена как\nпросмотренная'
                self.add_episode(episode)
                self.remove_episode(episode)
            else:
                msg = 'Такой серии\nнетв списках'
        else:
            msg = 'Эта серия уже\nв списке\nпросмотренных'
        return  msg

        # return удаляет серию из списка просмотренных
        # и возвращает ее в список оставшихся серий
    def remove(self, ep_input):
        episode = ep_input
        # if episode 
        if episode in self.watched_list:
            msg = f'{episode} серия\nубрана\nиз просмотренных'
            self.return_episode(episode)
        elif episode in self.rand_list:
            msg = 'Эту серию\nеще не смотрели'
        else:
            msg = 'Такой серии\nнет в списках'
        return msg

        # все прочие команды вызывают сообщение о количестве
        # оставшихся серий
    def ep_left(self):
        with open('random_list.txt', 'r') as file:
            self.rand_list = [row.strip() for row in file]
        return f'Осталось {len(self.rand_list)}\nнепросмотренных серий'

    def save_data(self):
        with open('rand_list.txt', 'w') as file:
            file.write('\n'.join(self.rand_list))
        with open('watched_list.txt', 'w') as file:
            file.write('\n'.join(self.watched_list))

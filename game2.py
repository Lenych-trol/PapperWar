import json
import os
import time
import random
import colorama


white_color = colorama.Fore.WHITE
green_color = colorama.Fore.GREEN
red_color = colorama.Fore.RED
blue_color = colorama.Fore.BLUE
black_color = colorama.Fore.BLACK
yellow_color = colorama.Fore.LIGHTYELLOW_EX

size_field = 0
field = []
player1_village = {
        "название": '',
        "люди": 0,
        "еды получает": 0,
        "еда в запасе": 100,
        "помысла получает": 0,
        "промысел в запасе": 100,
        "денег в запасе": 0,
        "тратит денег": 0,
        "получает денег": 0,
        "наука": 0,
        "количество защитных башен": 0,
        "количество казарм": 0,
        "жива ли столица": True
    }
player2_village = {
        "название": '',
        "люди": 0,
        "еды получает": 0,
        "еда в запасе": 100,
        "помысла получает": 0,
        "промысел в запасе": 100,
        "денег в запасе": 0,
        "тратит денег": 0,
        "получает денег": 0,
        "наука": 0,
        "количество защитных башен": 0,
        "количество казарм": 0,
        "жива ли столица": True
    }
names = ["Гоблины", "Викинги", "Эльфы", "Смурфики"]
now_turn = 'player2'

armi_persons = {
    "›": {
        "hp": {"1": 2, "2": 4, "3": 4, "4": 6, "5": 6, "6": 10},
        "damage": {"1": 1, "2": 1, "3": 2, "4": 2, "5": 3, "6": 3},
        "protection": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 1, "6": 2},
        "уклонение": {"1": 1, "2": 2, "3": 2, "4": 3, "5": 3, "6": 4},
        "цена": 20
    },
    "·": {
        "hp": {"1": 2, "2": 4, "3": 4, "4": 6, "5": 6, "6": 10},
        "damage": {"1": 1, "2": 1, "3": 2, "4": 2, "5": 3, "6": 3},
        "protection": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 1, "6": 2},
        "уклонение": {"1": 1, "2": 2, "3": 2, "4": 3, "5": 3, "6": 4},
        "цена": 5
    },
    "♦": {
        "hp": {"1": 2, "2": 4, "3": 4, "4": 6, "5": 6, "6": 10},
        "damage": {"1": 1, "2": 1, "3": 2, "4": 2, "5": 3, "6": 3},
        "protection": {"1": 0, "2": 0, "3": 0, "4": 1, "5": 1, "6": 2},
        "уклонение": {"1": 1, "2": 2, "3": 2, "4": 3, "5": 3, "6": 4},
        "цена": 30
    }
}


class ObjectPerson:
    def __init__(self, x, y, icon=' ', hp=None, damage=None,
                 protection=None, miss=None, who=None, his=None):
        self.icon = icon
        self.x = x
        self.y = y
        self.hp = hp
        self.damage = damage
        self.protection = protection
        self.miss = miss
        self.who = who
        self.his = his

    def move(self):
        new_x = get_x_position() - 1
        new_y = get_y_position() - 1
        flag = True
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if i == new_x and j == new_y:
                    flag = False
        if flag:
            print(f"{red_color}Слишком далеко...")
            time.sleep(2)
            return False
        if field[new_y][new_x].icon == ' ':
            field[new_y][new_x].icon = field[self.y][self.x].icon
            field[new_y][new_x].hp = field[self.y][self.x].hp
            field[new_y][new_x].who = field[self.y][self.x].who
            field[new_y][new_x].damage = field[self.y][self.x].damage
            field[new_y][new_x].protection = field[self.y][self.x].protection
            field[new_y][new_x].miss = field[self.y][self.x].miss
            field[self.y][self.x].icon = ' '
            field[self.y][self.x].hp = None
            field[self.y][self.x].who = None
            field[self.y][self.x].damage = None
            field[self.y][self.x].protection = None
            field[self.y][self.x].miss = None
            return True
        else:
            loading = ["\\", "|", "/", "-"] * 4
            for stick in loading:
                os.system("cls")
                print(f'{blue_color}Клетка занята. Откат действия {stick}{white_color}')
                time.sleep(0.25)
            return False

    def delete_object(self):
        if self.icon == '*':
            if self.his == "player1":
                player1_village["жива ли столица"] = False
            elif self.his == 'player2':
                player2_village["жива ли столица"] = False
        if self.his == "player1":
            if self.icon == '▒':
                player1_village["еды получает"] -= 10
                player1_village["люди"] += 1
                player1_village["получает денег"] += 1
            elif self.icon == '$':
                player1_village["получает денег"] -= 1
                player1_village["люди"] += 1
            elif self.icon == '⌂':
                player1_village["помысла получает"] -= 10
                player1_village["люди"] += 1
                player1_village["получает денег"] += 1
            elif self.icon == '?':
                player1_village["наука"] -= 1
                player1_village["люди"] += 1
                player1_village["получает денег"] += 1
            elif self.icon == '▲':
                player1_village["количество казарм"] -= 1
                player1_village["люди"] += 1
                player1_village["получает денег"] += 1
            elif self.icon == '╖':
                player1_village["количество защитных башен"] -= 1
                player1_village["люди"] += 1
                player1_village["получает денег"] += 1
        elif self.his == 'player2':
            if self.icon == '▒':
                player2_village["еды получает"] -= 10
                player2_village["люди"] += 1
                player2_village["получает денег"] += 1
            elif self.icon == '$':
                player2_village["получает денег"] -= 1
                player2_village["люди"] += 1
            elif self.icon == '⌂':
                player2_village["помысла получает"] -= 10
                player2_village["люди"] += 1
                player2_village["получает денег"] += 1
            elif self.icon == '?':
                player2_village["наука"] -= 1
                player2_village["люди"] += 1
                player2_village["получает денег"] += 1
            elif self.icon == '▲':
                player2_village["количество казарм"] -= 1
                player2_village["люди"] += 1
                player2_village["получает денег"] += 1
            elif self.icon == '╖':
                player2_village["количество защитных башен"] -= 1
                player2_village["люди"] += 1
                player2_village["получает денег"] += 1
        self.icon = ' '
        self.hp = None
        self.damage = None
        self.protection = None
        self.miss = None
        self.who = None

    def attack(self, enemy):
        if enemy.icon == ' ':
            print(f"{blue_color}Клетка пуста...{white_color}")
            time.sleep(2)
            return False
        if enemy.who == self.who:
            print(f"{red_color}Это принадлежит нам!{white_color}")
            time.sleep(2)
            return False
        if not enemy.icon in armi_persons.keys():
            enemy.delete_object()
            return True
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                if field[j][i] == enemy:
                    if self.hp <= 0:
                        self.delete_object()
                    elif enemy.hp <= 0:
                        enemy.delete_object()
                    else:
                        damage = self.damage - enemy.protection
                        if damage < 0:
                            damage = 0
                        if random.randint(1, 7) <= enemy.miss:
                            pass
                        else:
                            enemy.hp -= damage
                        enemy.attack(self)
                    return True
        print(f"{blue_color}Далекоо{white_color}")
        return False


def clear() -> None: os.system("cls")


def set_size_field():
    global size_field
    clear()
    size = input(f"{blue_color}Введите размер поля\n{green_color}1 - малый(15 клеток)"
                 f"\n{yellow_color}2 - средний(25 клеток)\n{red_color}3 - большой(35 клеток)\n{white_color}")
    if size == '1':
        size_field = 15
    elif size == '2':
        size_field = 25
    elif size == '3':
        size_field = 35
    else:
        print(f"{red_color}Введенно некорректное действие.{white_color}")
        time.sleep(2)
        set_size_field()


def create_field():
    global field, size_field
    for i in range(size_field):
        field.append([])
        for j in range(size_field):
            field[i].append(ObjectPerson(j, i))


def get_x_position() -> int:
    try:
        x = int(input(f"{blue_color}Введите координату по x: {white_color}"))
        if 1 > x or x > size_field:
            print(f"{red_color}Должно быть введено число от 1 до {size_field}.{white_color}")
            x = get_x_position()
    except ValueError:
        print(f"{red_color}Должно быть введено целое число.{white_color}")
        x = get_x_position()
    return x


def get_y_position() -> int:
    try:
        y = int(input(f"{blue_color}Введите координату по y: {white_color}"))
        if 1 > y or y > size_field:
            print(f"{red_color}Должно быть введено число от 1 до {size_field}.{white_color}")
            y = get_y_position()
    except ValueError:
        print(f"{red_color}Должно быть введено целое число.{white_color}")
        y = get_y_position()
    return y


def create_object_person(it_x: int, y: int, icon: str, who: str):
    global field
    if field[y][it_x].icon != ' ':
        loading = ["\\", "|", "/", "-"] * 4
        for stick in loading:
            os.system("cls")
            print(f'{blue_color}Клетка занята. Откат действия {stick}{white_color}')
            time.sleep(0.25)
        return False
    if field[y][it_x].his != who:
        loading = ["\\", "|", "/", "-"] * 4
        for stick in loading:
            os.system("cls")
            print(f'{blue_color}Это не наша территория. Откат действия {stick}{white_color}')
            time.sleep(0.25)
        return False
    if icon in armi_persons.keys():
        if who == 'player1':
            if player1_village["наука"] <= 0:
                loading = ["\\", "|", "/", "-"] * 4
                for stick in loading:
                    os.system("cls")
                    print(f'{blue_color}У вас мало науки. Откат действия {stick}{white_color}')
                    time.sleep(0.25)
                return False
            if player1_village["денег в запасе"] < armi_persons[icon]['цена']:
                loading = ["\\", "|", "/", "-"] * 4
                for stick in loading:
                    os.system("cls")
                    print(f'{blue_color}У вас мало денег, нужно: {armi_persons[icon]["цена"]}.'
                          f' Откат действия {stick}{white_color}')
                    time.sleep(0.25)
                return False
            field[y][it_x].icon = icon
            field[y][it_x].hp = armi_persons[icon]['hp'][str(player1_village['наука'])]
            field[y][it_x].damage = armi_persons[icon]['damage'][str(player1_village['наука'])]
            field[y][it_x].protection = armi_persons[icon]['protection'][str(player1_village['наука'])]
            field[y][it_x].miss = armi_persons[icon]['уклонение'][str(player1_village['наука'])]
            field[y][it_x].who = who
        elif who == 'player2':
            if player2_village["наука"] <= 0:
                loading = ["\\", "|", "/", "-"] * 4
                for stick in loading:
                    os.system("cls")
                    print(f'{blue_color}У вас мало науки. Откат действия {stick}{white_color}')
                    time.sleep(0.25)
                return False
            if player2_village["денег в запасе"] < armi_persons[icon]['цена']:
                loading = ["\\", "|", "/", "-"] * 4
                for stick in loading:
                    os.system("cls")
                    print(f'{blue_color}У вас мало денег, нужно: {armi_persons[icon]["цена"]}.'
                          f' Откат действия {stick}{white_color}')
                    time.sleep(0.25)
                return False
            field[y][it_x].icon = icon
            field[y][it_x].hp = armi_persons[icon]['hp'][str(player2_village['наука'])]
            field[y][it_x].damage = armi_persons[icon]['damage'][str(player2_village['наука'])]
            field[y][it_x].protection = armi_persons[icon]['protection'][str(player2_village['наука'])]
            field[y][it_x].miss = armi_persons[icon]['уклонение'][str(player2_village['наука'])]
            field[y][it_x].who = who
    else:
        field[y][it_x].icon = icon
        field[y][it_x].hp = 50
        field[y][it_x].who = who
        if who == 'player1':
            if icon == '▒':
                player1_village["еды получает"] += 10
                player1_village["люди"] -= 1
                player1_village["получает денег"] -= 1
            elif icon == '$':
                player1_village["получает денег"] += 2
                player1_village["люди"] -= 1
                player1_village["получает денег"] -= 1
            elif icon == '⌂':
                player1_village["помысла получает"] += 10
                player1_village["люди"] -= 1
                player1_village["получает денег"] -= 1
            elif icon == '?':
                player1_village["наука"] += 1
                player1_village["люди"] -= 1
                player1_village["получает денег"] -= 1
            elif icon == '▲':
                player1_village["количество казарм"] += 1
                player1_village["люди"] -= 1
                player1_village["получает денег"] -= 1
            elif icon == '╖':
                player1_village["количество защитных башен"] += 1
                player1_village["люди"] -= 1
                player1_village["получает денег"] -= 1
        elif who == 'player2':
            if icon == '▒':
                player2_village["еды получает"] += 10
                player2_village["люди"] -= 1
                player2_village["получает денег"] -= 1
            elif icon == '$':
                player2_village["получает денег"] += 2
                player2_village["люди"] -= 1
                player2_village["получает денег"] -= 1
            elif icon == '⌂':
                player2_village["помысла получает"] += 10
                player2_village["люди"] -= 1
                player2_village["получает денег"] -= 1
            elif icon == '?':
                player2_village["наука"] += 1
                player2_village["люди"] -= 1
                player2_village["получает денег"] -= 1
            elif icon == '▲':
                player2_village["количество казарм"] += 1
                player2_village["люди"] -= 1
                player2_village["получает денег"] -= 1
            elif icon == '╖':
                player2_village["количество защитных башен"] += 1
                player2_village["люди"] -= 1
                player2_village["получает денег"] -= 1
    return True


def create_villages():
    print(f"{blue_color}Создание деревень.{white_color}")
    print_field()
    print(f"{blue_color}Игрок 1 выберите место для вашей деревни.{white_color}")
    x = get_x_position() - 1
    y = get_y_position() - 1
    for i in range(x - 2, x + 3):
        for j in range(y - 2, y + 3):
            if 0 <= j < size_field and 0 <= i < size_field:
                field[i][j].his = 'player1'
                player1_village["люди"] += 1
                player1_village["получает денег"] += 1
    create_object_person(y, x, '*', 'player1')
    player1_village["люди"] -= 1
    player1_village["получает денег"] -= 1
    clear()
    player1_village["название"] = input(f"{blue_color}Игрок 1 введите название вашей деревни: {white_color}")
    print_field()
    print(f"{blue_color}Игрок 2 выберите место для вашей деревни.{white_color}")
    while 1:
        x = get_x_position() - 1
        y = get_y_position() - 1
        flag = 0
        for i in range(x - 2, x + 3):
            for j in range(y - 2, y + 3):
                if 0 <= j < size_field and 0 <= i < size_field:
                    if field[j][i].his == "player1":
                        flag = 1
        if flag != 1:
            break
        print(f"{red_color}Слишком близко к другой деревне!{white_color}")
    for i in range(x - 2, x + 3):
        for j in range(y - 2, y + 3):
            if 0 <= j < size_field and 0 <= i < size_field:
                field[j][i].his = 'player2'
                player2_village["люди"] += 1
                player2_village["получает денег"] += 1
    create_object_person(x, y, '*', 'player2')
    player2_village["люди"] -= 1
    player2_village["получает денег"] -= 1
    player2_village["название"] = input(f"{blue_color}Игрок 2 введите название вашей деревни: {white_color}")
    clear()
# ♪(alt + 13) - дружелюбная столица    |  ♫(alt + 14) - вражеская столица  |  ♥(alt + 15) - наша столица
# ▒(alt + 177) - ферма                 |  $(alt + 36) - шахта              |  ⌂(alt + 127) - производство
# ?(alt + 63) - лаборатория            |  ▲(alt + 30) - казарма            |  ╖(alt + 183) - крепость
# ·(alt + 250) - воин                  |  ♦(alt + 4) - маг                 |  ›(alt + 0155) - лучник


def print_field():
    global field
    print(end='   ')
    for i in range(size_field):
        if i + 1 < 10:
            print(i + 1, end='  ')
        else:
            print(i + 1, end=' ')
    print()
    for i in range(size_field):
        if i+1<10:
            print(i+1, end=' ')
        else:
            print(i + 1, end='')
        for j in range(size_field):
            if field[i][j].his == None:
                if field[i][j].who == None:
                    print(f"[{field[i][j].icon}]", end='')
                elif field[i][j].who == "player1":
                    print(f"[{green_color}{field[i][j].icon}{white_color}]", end='')
                elif field[i][j].who == "player2":
                    print(f"[{red_color}{field[i][j].icon}{white_color}]", end='')
            elif field[i][j].his == 'player1':
                if field[i][j].who == None:
                    print(f"{green_color}[{white_color}{field[i][j].icon}{green_color}]{white_color}", end='')
                elif field[i][j].who == "player1":
                    print(f"{green_color}[{green_color}{field[i][j].icon}{green_color}]{white_color}", end='')
                elif field[i][j].who == "player2":
                    print(f"{green_color}[{red_color}{field[i][j].icon}{green_color}]{white_color}", end='')
            elif field[i][j].his == 'player2':
                if field[i][j].who == None:
                    print(f"{red_color}[{white_color}{field[i][j].icon}{red_color}]{white_color}", end='')
                elif field[i][j].who == "player1":
                    print(f"{red_color}[{green_color}{field[i][j].icon}{red_color}]{white_color}", end='')
                elif field[i][j].who == "player2":
                    print(f"{red_color}[{red_color}{field[i][j].icon}{red_color}]{white_color}", end='')
        print()


def use_unin():
    for i in range(size_field):
        for j in range(size_field):
            if field[i][j].icon in armi_persons.keys() and field[i][j].who == now_turn:
                print(f"{blue_color}Выберите вашего юнита.")
                x = get_x_position() - 1
                y = get_y_position() - 1
                if field[y][x].icon in armi_persons.keys() and field[y][x].who == now_turn:
                    while 1:
                        a = input(f"{blue_color}Что сделать с войном\n"
                                  f"0 - вернуться к выбору действий\n"
                                  f"1 - переместить юнита(на одну клетку)\n"
                                  f"2 - посмотреть информацию о нём\n"
                                  f"3 - возвысить уровень или отхилить(только рядом с казармой)\n"
                                  f"4 - атаковать вражеского юнита{white_color}\n"
                                  f"Ваше действие: ")
                        if a == '0':
                            return 0
                        elif a == '1':
                            if field[y][x].move():
                                return True
                        elif a == '2':
                            print(f"{blue_color}Инфа:\n"
                                  f"здоровье - {field[y][x].hp}\n"
                                  f"урон - {field[y][x].damage}\n"
                                  f"защита - {field[y][x].protection}\n"
                                  f"шанс увернуться - {field[y][x].miss}")
                            input(f"{white_color}Нажмите Enter что бы подолжить.{white_color}")
                        elif a == '3':
                            for k in range(x - 1, x + 2):
                                for l in range(y - 1, y + 2):
                                    if field[l][k].icon == '▲' and field[l][k].who == now_turn:
                                        if now_turn == 'player1':
                                            field[y][x].hp = armi_persons[field[y][x].icon]['hp'][
                                                str(player1_village['наука'])]
                                            field[y][x].damage = armi_persons[field[y][x].icon]['damage'][
                                                str(player1_village['наука'])]
                                            field[y][x].protection = armi_persons[field[y][x].icon]['protection'][
                                                str(player1_village['наука'])]
                                            field[y][x].miss = armi_persons[field[y][x].icon]['уклонение'][
                                                str(player1_village['наука'])]
                                        elif now_turn == 'player2':
                                            field[y][x].hp = armi_persons[field[y][x].icon]['hp'][
                                                str(player2_village['наука'])]
                                            field[y][x].damage = armi_persons[field[y][x].icon]['damage'][
                                                str(player2_village['наука'])]
                                            field[y][x].protection = armi_persons[field[y][x].icon]['protection'][
                                                str(player2_village['наука'])]
                                            field[y][x].miss = armi_persons[field[y][x].icon]['уклонение'][
                                                str(player2_village['наука'])]
                                        return True
                            print(f"{red_color}Казарма слишком далеко...{white_color}")
                            time.sleep(2)
                            return False
                        elif a == '4':
                            for o in range(x - 1, x + 2):
                                for f in range(y - 1, y + 2):
                                    if 0 <= o < size_field and 0 <= f < size_field:
                                        if field[f][o].icon != ' ' and field[f][o].who != now_turn:
                                            x1 = get_x_position() - 1
                                            y1 = get_y_position() - 1
                                            if field[y][x].attack(field[y1][x1]):
                                                return True
                                            else:
                                                return False
    return False


def create_colony():
    print(f"{blue_color}Введите где построить колонию(колония 3х3) она"
          f" должна быть вплотную к поселению{white_color}")
    x = get_x_position() - 1
    y = get_y_position() - 1
    if now_turn == 'player1':
        if field[y][x].his == 'player2':
            print(f"{red_color}Эта территория занята.{white_color}")
            time.sleep(2)
            return False
    for i in range(x - 2, x + 3):
        for j in range(y - 2, y + 3):
            if 0 <= j < size_field and 0 <= i < size_field:
                if field[j][i].his == now_turn:
                    for k in range(x - 1, x + 2):
                        for p in range(y - 1, y + 2):
                            if 0 <= k < size_field and 0 <= p < size_field:
                                if field[p][k].his == None:
                                    field[p][k].his = now_turn
                                    if now_turn == 'player1':
                                        player1_village["люди"] += 1
                                    elif now_turn == 'player2':
                                        player2_village["люди"] += 1
                    return True
    print(f'{red_color}Слишком далеко...{white_color}')
    time.sleep(2)
    return False


def destroy():
    x = get_x_position() - 1
    y = get_y_position() - 1
    if field[y][x].icon == ' ':
        print(f"{red_color}Эта клетка пуста...{white_color}")
        return False
    if field[y][x].who != now_turn:
        print(f"{red_color}Эта клетка не наша...{white_color}")
        return False
    field[y][x].delete_object()
    return True


def show_info():
    if now_turn == 'player1':
        for i in player1_village.keys():
            print(f"{blue_color}{i} = {player1_village[i]}")
    elif now_turn == 'player2':
        for i in player2_village.keys():
            print(f"{blue_color}{i} = {player2_village[i]}")
    input(f"{white_color}Нажмите Enter что бы подолжить.{white_color}")

while 1:
    yes_or_no = input(f"{blue_color}Хотите загрузить последнее сохранение?\n1 - да\n2 - нет\n{white_color}")
    if yes_or_no == '2':
        set_size_field()
        create_field()
        create_villages()
        break
    elif yes_or_no == '1':
        with open('saves', 'r', encoding='utf-8') as f:
            ac = json.load(f)
        size_field = ac['size_field']
        field = ac['field']
        now_turn = ac[now_turn]
        player2_village = ac['player2_village']
        player1_village = ac['player1_village']
        break
    else:
        print(f'{red_color}Действие не распознано{white_color}')
cloc = False
while player2_village["жива ли столица"] and player1_village["жива ли столица"]:
    if cloc:
        break
    if now_turn == 'player1':
        player1_village["денег в запасе"] += player1_village["получает денег"] - player1_village["тратит денег"]
        player1_village["промысел в запасе"] += player1_village["помысла получает"] - player1_village["люди"]
        player1_village["еда в запасе"] += player1_village["еды получает"] - player1_village["люди"]
        if player1_village["еда в запасе"] < 0:
            print(f"Игрок 1, ваше поселение умерло с голода. Игрок 2 победил.")
            time.sleep(3)
            break
        if player1_village["промысел в запасе"] < 0:
            print(f"Игрок 1, ваше поселение умерло с голода. Игрок 2 победил.")
            time.sleep(3)
            break
        now_turn = 'player2'
    else:
        player2_village["денег в запасе"] += player2_village["получает денег"] - player2_village["тратит денег"]
        player2_village["промысел в запасе"] += player2_village["помысла получает"] - player2_village["люди"]
        player2_village["еда в запасе"] += player2_village["еды получает"] - player2_village["люди"]
        now_turn = 'player1'
        if player2_village["еда в запасе"] < 0:
            print(f"Игрок 1, ваше поселение умерло с голода. Игрок 2 победил.")
            time.sleep(3)
            break
        if player1_village["промысел в запасе"] < 0:
            print(f"Игрок 1, ваше поселение умерло с голода. Игрок 2 победил.")
            time.sleep(3)
            break
    while 1:
        clear()
        print_field()
        a = input(f"Доступные действия {now_turn}:\n"
                  f"0 - информация о поселении\n"
                  f"1 - построить здание\\создать юнита\n"
                  f"2 - построить колонию\n"
                  f"3 - управлять юнитом\n"
                  f"4 - разрушить здание\n"
                  f"10 - сохранить и выйти\n"
                  f"ваше действие: ")
        if a == '0':
            clear()
            show_info()
        elif a == '1':
            flag = False
            while 1:
                clear()
                print_field()
                house = input(f"{blue_color}Выберите что построить\n"
                              f"0 - назад\n"
                              f"1 - ▒ (ферма)\n"
                              f"2 - $ (шахта)\n"
                              f"3 - ⌂ (фабрика)\n"
                              f"4 - ▲ (казарма)\n"
                              f"5 - ╖ (башня)\n"
                              f"6 - ? (лаборатория)\n"
                              f"7 - · (воин)\n"
                              f"8 - ♦ (маг)\n"
                              f"9 - › (лучник)\n"
                              f"Ваш выбор: ")
                if house == '0':
                    break
                elif house == '1':
                    if create_object_person(get_x_position()-1, get_y_position()-1, '▒', now_turn):
                        flag = True
                        break
                elif house == '2':
                    if create_object_person(get_x_position()-1, get_y_position()-1, '$', now_turn):
                        flag = True
                        break
                elif house == '3':
                    if create_object_person(get_x_position()-1, get_y_position()-1, '⌂', now_turn):
                        flag = True
                        break
                elif house == '4':
                    if create_object_person(get_x_position()-1, get_y_position()-1, '▲', now_turn):
                        flag = True
                        break
                elif house == '5':
                    if create_object_person(get_x_position()-1, get_y_position()-1, '╖', now_turn):
                        flag = True
                        break
                elif house == '6':
                    if create_object_person(get_x_position()-1, get_y_position()-1, '?', now_turn):
                        flag = True
                        break
                elif house == '7':
                    if create_object_person(get_x_position()-1, get_y_position()-1, '·', now_turn):
                        flag = True
                        break
                elif house == '8':
                    if create_object_person(get_x_position()-1, get_y_position()-1, '♦', now_turn):
                        flag = True
                        break
                elif house == '9':
                    if create_object_person(get_x_position()-1, get_y_position()-1, '›', now_turn):
                        flag = True
                        break
                else:
                    print(f"{red_color}Введенно некорректное действие.")
                    time.sleep(2)
            if flag:
                break
        elif a == '2':
            while 1:
                clear()
                print_field()
                if create_colony():
                    break
            break
        elif a == '3':
            flag = False
            while 1:
                b = use_unin()
                if b == 0:
                    break
                elif b == True:
                    flag = True
                    break
            if flag:
                break
        elif a == '4':
            flag = False
            while 1:
                if destroy():
                    flag = True
                    break
            if flag:
                break
        elif a == '10':
            save = {}
            save['player1_village'] = player1_village
            save['player2_village'] = player2_village
            save['now_turn'] = now_turn
            save['field'] = []
            for i in range(size_field):
                save['field'].append([])
                for j in range(size_field):
                    save['field'][i].append({
                        'icon': field[j][i].icon,
                        'x': field[j][i].x,
                        'y': field[j][i].y,
                        'hp': field[j][i].hp,
                        'damage': field[j][i].damage,
                        'protection': field[j][i].protection,
                        'miss': field[j][i].miss,
                        'who': field[j][i].who,
                        'his': field[j][i].his
                    })
            save['size_field'] = size_field
            print(save)
            with open("saves.json", "w", encoding="utf-8") as file:
                json.dump(save, file)
            cloc = True
            break



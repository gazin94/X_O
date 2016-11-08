from os import system
char = '*'


class Field:

    """
    Клас роботи з полем
    """
    def __init__(self, size_f=3):
        self.field = []
        self.size = size_f
        self.actions = size_f**2

    def set(self):
        """
        Функція генерує поле з 3 списків
        :return:
        """
        for dummy_i in range(self.size):
            self.field.append(list(char*3))

    def get(self):
        return self.field

    def print(self):
        """
        Відображає поле як 3 ряди з елементів "-"
        :return:
        """
        for string in range(len(self.field)):
            print(self.field[string])
        print("\033[1;33m Actions: {0}\033[0m".format(self.actions))

    def change(self, x, y, value):
        while x > 2:
            print(">3")
            x = get_int('x')-1

        while y > 2:
            print(">3")
            y = get_int('y') - 1

        while self.field[y][x] != char:
            print("\033[31m Non free item\033[0m")

            x = get_int('x') - 1
            while x > 2:
                print(">3")
                x = get_int('x') - 1

            y = get_int('y') - 1
            while x > 2:
                print(">3")
                y = get_int('y') - 1

        self.field[y][x] = value

    def get_actions(self, field):
        self.actions = 0
        for dummy_i in range(len(field)):
            for dummy_j in range(len(field[dummy_i])):
                sub_lst = field[dummy_i]
                if char == sub_lst[dummy_j]:
                    self.actions += 1
        return self.actions


class Player:
    def __init__(self, name, char):
        self.name = name
        self.char = char

    def get_name(self):
        return self.name

    def get_char(self):
        return self.char


def winner(name):
    print("\033[1;32m Winner {0}\033[0m".format(name))


def who_winner(char, list, name):
    # !!!!!!FIX!!!!!!
    # OPA INDUS STYLE!
    # Diagonals
    if list[0][0] == char and list[1][1] == char and list[2][2] == char:
        winner(name)
        print(1)
        return 0
    elif list[0][2] == char and list[1][1] == char and list[2][0] == char:
        winner(name)
        print(2)
        return 0
    # rows
    elif list[0][0] == char and list[0][1] == char and list[0][2] == char:
        winner(name)
        print(3)
        return 0
    elif list[1][0] == char and list[1][1] == char and list[1][2] == char:
        winner(name)
        print(4)
        return 0
    elif list[2][0] == char and list[2][1] == char and list[2][2] == char:
        winner(name)
        print(5)
        return 0
    # cols
    elif list[0][0] == char and list[1][0] == char and list[2][0] == char:
        winner(name)
        print(6)
        return 0
    elif list[1][0] == char and list[1][1] == char and list[1][2] == char:
        winner(name)
        return 0
        print(7)
    elif list[2][0] == char and list[2][1] == char and list[2][2] == char:
        winner(name)
        print(8)
        return 0
    # return 1


def get_int(get):
    """
    Вводить тіки ціле чило і нічого іншого
    :param get:
    :return:
    """
    while True:
        try:
            number = int(input("\033[36m get {0}: \033[0m".format(get)))
            break
        except ValueError:
            print("\033[36m Enter value\033[0m")
    return number

while True:
    # Input data
    system('clear')
    print('\033[1;32mPlayer 1\033[0m')
    player1 = Player(input('\033[36m  Enter name: \033[0m'), input('\033[32m Enter your char: \033[0m'))
    print('\033[1;32mPlayer 2\033[0m')
    player2 = Player(input('\033[36m  Enter name: \033[0m'), input('\033[32m Enter your char: \033[0m'))
    # Перевірка на однакві імена
    while player1.get_name() == player2.get_name():
        print("\033[31m Related input information \033[0m")

        print('\033[1;32mPlayer 1\033[0m')
        player1 = Player(input('\033[36m  Enter name: \033[0m'), input('\033[32m Enter your char: \033[0m'))
        print('\033[1;32mPlayer 2\033[0m')
        player2 = Player(input('\033[36m  Enter name: \033[0m'), input('\033[32m Enter your char: \033[0m'))

    # size = 0
    # while True:
    #     try:
    #         size = int(input('Enter field size: '))
    #         break
    #     except ValueError:
    #         print("Enter value")

    field = Field()
    # Generating
    field.set()
    while True:
        system('clear')
        b_field = field.get()

        # Player 1
        if field.get_actions(b_field) == 0:
            print('\033[31m No actions!\033[0m')
            field.print()
            break
        print("\033[1;33m player:{0} char:{1}\033[0m".format(player1.get_name(), player1.get_char(),))
        field.print()
        field.change(get_int('x') - 1, get_int('y') - 1, player1.get_char())
        system('clear')
        field.print()

        if who_winner(player1.get_char(), b_field, player1.get_name()) == 0:
            break
        elif who_winner(player2.get_char(), b_field, player2.get_name()) == 0:
            break

        system('clear')
        # Player 2
        if field.get_actions(b_field) == 0:
            print('\033[31m No actions!\033[0m')
            break
        print("\033[1;33m player:{0} char:{1}\033[0m".format(player2.get_name(),player2.get_char()))
        field.print()
        field.change(get_int('x') - 1, get_int('y') - 1, player2.get_char())
        system('clear')

        field.print()

        if who_winner(player1.get_char(), b_field, player1.get_name()) == 0:
                break
        elif who_winner(player2.get_char(), b_field, player2.get_name()) == 0:
            break

    if input("\033[33m Start new game? Yes/No: \033[0m") != 'Yes':
        break

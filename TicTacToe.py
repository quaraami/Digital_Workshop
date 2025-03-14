import os
 
 
class Cell:  # 1. Класс, который описывает одну клетку поля:
    #  Клетка, у которой есть значения
    def __init__(self, num):
        self.num = num  # номер клетки
        self.symbol = ' '  # занята она или нет
 
    def __str__(self):
        return self.symbol
 
 
class Board:  # 2. Класс, который описывает поле игры.
    #  Класс поля, который создаёт у себя экземпляры клетки и поле игры
    def __init__(self, size: int = 3):
        self.size = size
        self.cells = [Cell(cell_number) for cell_number in range(1, self.size * self.size + 1)]
 
    def display(self):
        # Метод создает таблицу игрового поля
        size = self.size
        cprint('    | ', suffix='')
        for alpha in range(size):
            cprint(chr(ord('A') + alpha), color_code=alpha + 1, suffix=' ')
            cprint('|', suffix=' ')
        print()
        for row in range(size):
            num = row + 1
            cprint('-'*(size * 5 + 1), suffix='')
            cprint('-')
            cprint(f'  {num}', color_code=num, suffix=' ')
            out = '| '
            for col in range(size):
                out += f'{self.cells[row * size + col]} | '
            cprint(out)
        cprint('-'*(size * 5 + 1), suffix='')
        cprint('-')
 
    def update(self, cell_num, symbol):
        if self.cells[cell_num - 1].symbol == ' ':
            self.cells[cell_num - 1].symbol = symbol
            return True
        else:
            return False
 
    def end_game(self):
        size = self.size
        for index in range(size):
 
            # проверка горизонталей
            first_in_row = self.cells[index * size].symbol
            if first_in_row != ' ':
                for col in range(1, size):
                    if self.cells[index * size + col].symbol != first_in_row:
                        break
                else:
                    return True
 
            # проверка вертикалей
            first_in_col = self.cells[index].symbol
            if first_in_col != ' ':
                for row in range(size, size**2, size):
                    if self.cells[index + row].symbol != first_in_col:
                        break
                else:
                    return True
 
        # проверка правой диагонали
        if self.cells[0].symbol != ' ':
            for diagonal_item in range(size + 1, size**2, size + 1):
                if self.cells[diagonal_item].symbol != self.cells[0].symbol:
                    break
            else:
                return True
 
        # проверка левой диагонали
        start_index = size - 1
        if self.cells[start_index].symbol != ' ':
            for diagonal_item in range(start_index*2, size*size - start_index, start_index):
                if self.cells[diagonal_item].symbol != self.cells[start_index].symbol:
                    break
            else:
                return True
 
        # проверка наличия пустых ячеек
        for cell in self.cells:
            if cell.symbol == ' ':
                return False
        return None
 
 
class Player:  # 3. Класс, который описывает поведение игрока:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0
 
    def get_move(self):
        return cinput(f'{self.name.capitalize()}, введите номер ячейки: ', 3)
 
 
class Game:  # 4. Класс, который управляет ходом игры:
    # Класс «Игры» содержит атрибуты:
    # состояние игры,
    # игроки,
    # поле.
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player
        while True:
            try:
                self.board_size = int(cinput('Введите размер поля: '))
            except ValueError:
                cprint('Ошибка! Размер доски необходимо указывать целыми числами.', 1)
            else:
                break
        self.board = Board(self.board_size)
        self.current_player = first_player
 
    def make_a_move(self):
        """
        Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле,
        проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
        :return: Bool.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        cprint(f'\nХодит игрок {self.current_player.name.capitalize()}:\n', 4)
        self.board.display()
        size = self.board.size
        while True:
            try:
                user_choice = self.current_player.get_move().upper()
                number = user_choice[1:]
                alpha = user_choice[0]
                if number.isnumeric() and alpha.isalpha():
                    row = int(number) - 1
                    col = ord(alpha) - ord('A')
                else:
                    raise ValueError
                if col < size and 0 <= row < size:
                    cell_num = 1 + col + row * size
                    if not self.board.update(cell_num, self.current_player.symbol):
                        raise RuntimeError
                else:
                    raise IndexError
            except IndexError:
                cprint('Ошибка! Введенные координаты указывают на несуществующую ячейку.', 1)
                continue
            except ValueError:
                cprint('Ошибка! Введенные координаты должны быть в формате <буква><число>.', 1)
                continue
            except RuntimeError:
                cprint('Эта ячейка недоступна! Попробуйте другую.', 1)
                continue
            else:
                break
 
        if self.board.end_game():
            os.system('cls' if os.name == 'nt' else 'clear')
            cprint(f'\nПобедил игрок {self.current_player.name}!\n', 6)
            self.board.display()
            self.current_player.score += 1
            return True
        elif self.board.end_game() is None:
            os.system('cls' if os.name == 'nt' else 'clear')
            cprint('Ничья!')
            self.board.display()
            return True
 
        if self.current_player == self.first_player:
            self.current_player = self.second_player
        else:
            self.current_player = self.first_player
 
        return False
 
    def play_one_game(self):
        """
        Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков
        или ничьей. Если игра завершена, метод возвращает True, иначе False.
        :return: Bool.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
        cinput('\nНовая игра!')
        self.board = Board(self.board_size)
        self.current_player = self.first_player
        while not self.board.end_game():
            if self.make_a_move():
                return True
        else:
            return False
 
    def main_game(self):
        """
        Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать
        играть. После каждой игры выводится текущий счёт игроков.
        :return: None
        """
        while True:
            self.play_one_game()
            cprint('Очки:')
            cprint(f'{self.first_player.name} : {self.first_player.score}', 5)
            cprint(f'{self.second_player.name} : {self.second_player.score}', 4)
            if cinput('\nХотите сыграть еще? (Да/Нет): ').lower() != 'да':
                break
        print('Игра окончена!')
 
 
def cprint(data: any, color_code: int = 2, suffix: str = '\n') -> None:
    print(f'\u001b[3{color_code}m', end='')
    print(data, end=suffix)
 
 
def cinput(data: any, color_code: int = 2) -> str:
    print(f'\u001b[3{color_code}m', end='')
    return input(data)
 
 
if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    player_first = Player(cinput('Введите имя первого игрока [крестики]: ', 5), 'x')
    player_second = Player(cinput('Введите имя второго игрока [нолики]: ', 4), 'o')
    core = Game(player_first, player_second)
    core.main_game()
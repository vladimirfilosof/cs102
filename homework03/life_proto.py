import random
import typing as tp

import pygame
from pygame.locals import *
import time

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток
        self.grid = self.create_grid(True)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.grid = self.get_next_generation()
#            time.sleep(1)
            self.draw_grid()
            self.draw_lines()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        return [ 
                    [ int(randomize) and random.randint(0,1) for j in range(self.cell_width) ]  
                    for i in range(self.cell_height) 
                ]


    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for y in range(self.cell_height):
            for x in range(self.cell_width):
                pygame.draw.rect(self.screen, pygame.Color('green') if self.grid[y][x] else pygame.Color('white'),
                        pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))


    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """

        neighbours = []

        for i in range(cell[0] - 1, cell[0] + 2):
            if i < 0 or i >= len(self.grid):
                continue

            for j in range(cell[1] - 1, cell[1] + 2):
                if (i == cell[0] and j == cell[1]) or j < 0 or j >= len(self.grid[i]):
                    continue
    
                neighbours.append(self.grid[i][j])

        return neighbours
        

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        return [
                    [
                        1 if (self.grid[i][j] == 1 and 2 <= sum( self.get_neighbours((i,j)) ) <= 3) 
                        or (self.grid[i][j] == 0 and sum( self.get_neighbours((i,j)) ) == 3) else 0 
                    for j in range(self.cell_width) ] 
                for i in range(self.cell_height)]


if __name__ == "__main__":
    g = GameOfLife()
    g.run()


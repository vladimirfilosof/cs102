import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations or float("inf")
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        return [
            [int(randomize) and random.randint(0, 1) for j in range(self.cols)]
            for i in range(self.rows)
        ]

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []

        for i in range(cell[0] - 1, cell[0] + 2):
            if i < 0 or i >= len(self.curr_generation):
                continue

            for j in range(cell[1] - 1, cell[1] + 2):
                if (i == cell[0] and j == cell[1]) or j < 0 or j >= len(self.curr_generation[i]):
                    continue

                neighbours.append(self.curr_generation[i][j])

        return neighbours

    def get_next_generation(self) -> Grid:
        return [
            [
                1
                if (self.curr_generation[i][j] == 1 and 2 <= sum(self.get_neighbours((i, j))) <= 3)
                or (self.curr_generation[i][j] == 0 and sum(self.get_neighbours((i, j))) == 3)
                else 0
                for j in range(self.cols)
            ]
            for i in range(self.rows)
        ]

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return self.generations <= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        for i in range(len(self.curr_generation)):
            for j in range(len(self.curr_generation[i])):
                if self.curr_generation[i][j] != self.prev_generation[i][j]:
                    return True

        return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        f = open(filename, "r")
        grid: Grid = []
        for line in f:
            grid.append([int(i) for i in line[:-1]])
        f.close()
        life = GameOfLife((len(grid), len(grid[0])))
        life.curr_generation = grid
        return life

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        f = open(filename, "w")
        for row in self.curr_generation:
            for i in row:
                f.write(str(i))

            f.write("\n")

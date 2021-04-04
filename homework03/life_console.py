import curses
import curses.ascii
import time

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """ Отобразить рамку. """
        for i in range(self.life.rows + 1):
            try:
                screen.addch(i, 0, "|")
            except:
                pass

            try:
                screen.addch(i, self.life.cols + 1, "|")
            except:
                pass

        for i in range(self.life.cols + 2):
            try:
                screen.addch(0, i, "-")
            except:
                pass

            try:
                screen.addch(self.life.rows + 1, i, "-")
            except:
                pass

    def draw_grid(self, screen) -> None:
        """ Отобразить состояние клеток. """
        for i in range(len(self.life.curr_generation)):
            for j in range(len(self.life.curr_generation[i])):
                try:
                    if self.life.curr_generation[i][j]:
                        screen.addch(i + 1, j + 1, "*")
                    else:
                        screen.addch(i + 1, j + 1, " ")

                except:
                    pass

    def run(self) -> None:
        curses.initscr()
        screen = curses.newwin(self.life.rows + 2, self.life.cols + 2, 0, 0)
        screen.clear()
        curses.noecho()
        curses.cbreak()
        screen.keypad(True)
        screen.nodelay(True)

        self.draw_borders(screen)

        pause = False
        key = 0
        while (
            key != curses.ascii.ESC
            and self.life.is_changing
            and self.life.is_max_generations_exceeded
        ):
            self.draw_grid(screen)
            screen.refresh()

            prevKey = key
            event = screen.getch()
            key = key if event == -1 else event

            if key == curses.ascii.SP:
                key = -1
                while key != curses.ascii.SP:
                    key = screen.getch()
                key = prevKey
                continue

            if key == curses.ascii.SP:
                pause = not pause

            self.life.step()

        curses.nocbreak()
        screen.keypad(False)
        curses.echo()
        curses.endwin()


if __name__ == "__main__":
    clife = Console(GameOfLife((30, 70)))
    clife.run()

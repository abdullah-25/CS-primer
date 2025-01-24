import os
import random
import time

WIDTH, HEIGHT, ITERATIONS = 20, 20, 50


def count_neighbors(grid, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = (x + dx) % WIDTH, (y + dy) % HEIGHT
                if grid[ny][nx]:
                    count += 1
        return count



def apply_rules(cell, neighbor_count):
        if cell:
            return 2 <= neighbor_count <= 3
        else:
            return neighbor_count == 3
        

def next_state(self):
        new_cells = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
        for y in range(HEIGHT):
            for x in range(WIDTH):
                cell = cells[y][x]
                neighbor_count = count_neighbors(cells, x, y)
                new_cells[y][x] =  apply_rules(cell, neighbor_count)
        return new_cells

if __name__ == "__main__":
    """
    game = GameOfLife()
    game.initialize_random()
    game.run()
    """
    cells = [[random.random() < 0.3 for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for _ in range(ITERATIONS):
        os.system ('clear')
        # TODO  simplify this loop
        for y in range(HEIGHT):
            for x in range(WIDTH):
                print('■' if cells[y][x] else '□', end='')
            print()
        print()

        cells = next_state(cells)



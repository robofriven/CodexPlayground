import random
import time
import os

WIDTH = 50
HEIGHT = 50


def create_grid():
    """Return a HEIGHT x WIDTH grid of random 0s and 1s."""
    return [[random.randint(0, 1) for _ in range(WIDTH)] for _ in range(HEIGHT)]


def display(grid):
    """Clear the screen and display the grid."""
    os.system("clear")  # Works on Unix
    for row in grid:
        print("".join("#" if cell else "." for cell in row))


def step(grid):
    """Compute the next generation of the grid."""
    new_grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            live_neighbors = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dy == 0 and dx == 0:
                        continue
                    ny = (y + dy) % HEIGHT
                    nx = (x + dx) % WIDTH
                    live_neighbors += grid[ny][nx]
            if grid[y][x] == 1 and live_neighbors in (2, 3):
                new_grid[y][x] = 1
            elif grid[y][x] == 0 and live_neighbors == 3:
                new_grid[y][x] = 1
    return new_grid


def main():
    grid = create_grid()
    try:
        while True:
            display(grid)
            grid = step(grid)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")


if __name__ == "__main__":
    main()

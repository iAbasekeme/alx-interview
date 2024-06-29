#!/usr/bin/python3
"""A module that contains the island perimeter grid
"""


def island_perimeter(grid):
    """A function that returns the perimeter of the island described in grid
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Each land cell starts with 4 possible perimeter sides
                perimeter += 4

                # Check all 4 possible neighbors (up, down, left, right)
                if r > 0 and grid[r - 1][c] == 1:  # Up
                    perimeter -= 1
                if r < rows - 1 and grid[r + 1][c] == 1:  # Down
                    perimeter -= 1
                if c > 0 and grid[r][c - 1] == 1:  # Left
                    perimeter -= 1
                if c < cols - 1 and grid[r][c + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter

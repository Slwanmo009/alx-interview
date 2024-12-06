#!/usr/bin/python3
"""
Module that contains the function to calculate the perimeter of an island in a grid.
"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island represented in the grid.

    Args:
        grid (list of list of ints): A grid of integers where 0 represents water
                                      and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # Check above
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check below
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter

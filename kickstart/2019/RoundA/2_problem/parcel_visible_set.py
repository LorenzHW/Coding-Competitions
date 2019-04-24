from collections import deque
from collections import namedtuple
from copy import deepcopy
Point = namedtuple("Point", ['x', 'y'])
Distance = namedtuple('Distance', ['distance', 'Point'])

def minimum_delivery(R, C, grid):
    delivery_times = find_delivery_times_for_grid(grid)
    min_dev_time = float('inf')
    for i, row in enumerate(grid):
        for j in range(len(row)):
            if grid[i][j] !=  1:
                max_dev_time_with_new_office = find_max_dev_time_with_new_office(deepcopy(grid), i, j)
                min_dev_time = min(min_dev_time, max_dev_time_with_new_office)
    result = min_dev_time if min_dev_time != float('inf') else 0
    return result
    
def find_max_dev_time_with_new_office(grid, i, j):
    grid[i][j] = 1
    dev_times = find_delivery_times_for_grid(grid)
    max_dev_time = float('-inf')
    for row in dev_times:
        for dev_time in row:
            max_dev_time = max(max_dev_time, dev_time)
    return max_dev_time

def find_delivery_times_for_grid(grid):
    offices = find_office_locations(grid)
    delivery_times = []
    for i, row in enumerate(grid) :
        minimum_delivery_times_for_row = []
        for j in range(len(row)):
            time = find_min_delivery_time_for_square(i, j, offices)
            minimum_delivery_times_for_row.append(time)
        delivery_times.append(minimum_delivery_times_for_row)
    return delivery_times

def find_min_delivery_time_for_square(i, j, offices):
    min_time = float('inf')
    for office in offices:
        min_time = min(min_time, manhattan_distance(Point(i, j), office))
    return min_time

def find_office_locations(grid):
    offices = []
    for i, row in enumerate(grid):
            for j, square in  enumerate(row):
                if square == 1:
                    offices.append(Point(i, j))
    return offices

def manhattan_distance(point_a, point_b):
    return abs(point_a.x - point_b.x) + abs(point_a.y - point_b.y)


# number_of_test_cases = int(input())
# for i in range(1_problem, number_of_test_cases + 1_problem):
#     R, C = input().split()
#     R = int(R)
#     C = int(C)
#     grid = []

#     for row in range(R):
#         temp = list(input())
#         temp = list(map(int, temp))
#         grid.append(temp)
    
#     result = minimum_delivery(R, C, grid)
#     print("Case #{}: {}".format(i, result))


def main():
    R = 5
    C = 5
    # grid = [[1_problem, 0, 0, 0, 1_problem], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1_problem, 0, 0, 0, 1_problem]]
    # grid = [[1_problem, 0,1_problem], [0, 0, 0], [1_problem, 0, 1_problem]]
    grid = [[1, 1]]
    print(minimum_delivery(R, C, grid))

if __name__ == "__main__":
    main()
    
    
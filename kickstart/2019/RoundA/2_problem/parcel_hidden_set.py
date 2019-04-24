from collections import deque
from collections import namedtuple
from copy import deepcopy
from collections import deque
Point = namedtuple("Point", ('x', 'y', 'delivery_time'))

def minimum_delivery(R, C, grid):
    offices = find_office_locations(grid)
    dev_times_to_square = shortest_path_to_square_from_office(R, C, offices)
    max_dev_time = get_max_dev_time(R, C, dev_times_to_square)

    results = []
    for K in reversed(range(0, max_dev_time)):
        all_squares_with_dev_time_bigger_k = []
        for i in range(R):
            for j in range(C):
                if dev_times_to_square[i][j] > K:
                    all_squares_with_dev_time_bigger_k.append(Point(i, j, None))

        offices = find_office_locations(grid)
        new_office = min_total_distance(grid, all_squares_with_dev_time_bigger_k)
        offices.append(new_office)
        new_dev_times_to_square = shortest_path_to_square_from_office(R, C, offices)
        new_max_dev_time = get_max_dev_time(R, C, new_dev_times_to_square)    
        results.append(new_max_dev_time)
    if results:
        return min(results)
    else:
        return 0


def get_max_dev_time(R, C, grid):
    max_dev_time = float('-inf')
    for i in range(R):
        for j in range(C):
            max_dev_time = max(max_dev_time, grid[i][j])
    return max_dev_time


def min_total_distance(grid, points):
    cols, rows = [], []

    for point in points:
        cols.append(point.y)
        rows.append(point.x)
    cols.sort()
    rows.sort()

    rows_median_idx = len(rows) // 2
    cols_median_idx = len(cols) // 2
    
    x = Point(rows[rows_median_idx], cols[cols_median_idx], 0)
    return x

def shortest_path_to_square_from_office(R, C, offices):
    # Multiple source BFS
    neighbours = [Point(0, 1, None), Point(0, -1, None), Point(1, 0, None), Point(-1, 0, None)]
    grid = [[None for c in range(C)] for r in range(R)]
    points_to_visit = deque(offices)
    explored = set()

    while points_to_visit:
        point = points_to_visit.popleft()

        if (point.x, point.y) not in explored:
            explored.add((point.x, point.y))
            grid[point.x][point.y] = point.delivery_time

            for n in neighbours:
                next_point = Point(point.x + n.x, point.y + n.y, point.delivery_time + 1)
                good = all([0 <= next_point.x < R, 0 <= next_point.y < C])
                if good:
                    points_to_visit.append(next_point)
    return grid


def find_office_locations(grid):
    offices = []
    for i, row in enumerate(grid):
            for j, square in  enumerate(row):
                if square == 1:
                    offices.append(Point(i, j, 0))
    return offices

def manhattan_distance(point_a, point_b):
    return max(abs(point_a.x + point_a.y - (point_b.x + point_b.y)), abs(point_a.x - point_a.y - (point_b.x - point_b.y)))
    # return abs(point_a.x - point_b.x) + abs(point_a.y - point_b.y)


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
    grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1]]
    # grid = [[1_problem, 0,1_problem], [0, 0, 0], [1_problem, 0, 1_problem]]
    # grid = [[1_problem, 1_problem]]
    R = len(grid)
    C = len(grid[0])
    print(minimum_delivery(R, C, grid))

if __name__ == "__main__":
    main()
    
    
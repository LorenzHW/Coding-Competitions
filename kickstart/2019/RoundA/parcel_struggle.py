from collections import deque
from collections import namedtuple
from copy import deepcopy
Point = namedtuple("Point", ['x', 'y'])
Distance = namedtuple('Distance', ['distance', 'Point'])

def minimum_delivery_struggle(R, C, grid):
    delivery_offices_coordinates = []

    for i, row in enumerate(grid) :
        for j, square in  enumerate(row):
            if square == 1:
                delivery_offices_coordinates.append(Point(i, j))

    new_office = get_coordinates_of_max_manhattan_distance(grid, delivery_offices_coordinates)
    if new_office:
        delivery_offices_coordinates.append(new_office.Point)
        grid[new_office.Point.x][new_office.Point.y] = 1
        next_office = get_coordinates_of_max_manhattan_distance(grid, delivery_offices_coordinates, second_call=True)
        if next_office:
            return next_office.distance
        else:
            return 0
    else:
        return 0
    

def get_coordinates_of_max_manhattan_distance(grid, delivery_offices_coordinates, second_call=False):
    
    min_distances = []

    for i, row in enumerate(grid) :
        for j, square in  enumerate(row):
            current_point = Point(i, j)

            if square != 1:
                min_distance = float('inf')
                for office in delivery_offices_coordinates:
                    min_distance = min(min_distance, manhattan_distance(current_point, office)) 
                min_distances.append(Distance(min_distance, current_point)) 
    
    if min_distances:
        min_distances.sort(key=lambda val: val.distance)

        options = [x for x in min_distances if x.distance == min_distances[-1].distance]

        if len(options) == 1 or second_call:
            return min_distances[-1]
        else:
            optimal_office = find_optimal_office(options)
            return optimal_office
    else:
        return None


def find_optimal_office(options):
    inbetween_distances = []
    for o in options:
        
        max_distance = float('-inf')
        for o2 in options:
            max_distance = max(max_distance, manhattan_distance(o.Point, o2.Point)) 
        inbetween_distances.append(Distance(max_distance, o.Point))
    inbetween_distances.sort(key=lambda val: val.distance)
    return inbetween_distances[0]
    

def manhattan_distance(point_a, point_b):
    return abs(point_a.x - point_b.x) + abs(point_a.y - point_b.y)


number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    R, C = input().split()
    R = int(R)
    C = int(C)
    grid = []

    for row in range(R):
        temp = list(input())
        temp = list(map(int, temp))
        grid.append(temp)
    
    result = minimum_delivery_struggle(R, C, grid)
    print("Case #{}: {}".format(i, result))


def main():
    R = 5
    C = 5
    # grid = [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1]]
    # grid = [[1, 0,1], [0, 0, 0], [1, 0, 1]]
    grid = [[1, 1]]
    print(minimum_delivery_struggle(R, C, grid))

if __name__ == "__main__":
    main()
    
    
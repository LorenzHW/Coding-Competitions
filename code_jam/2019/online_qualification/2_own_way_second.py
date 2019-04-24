
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

def walk_maze(N, lydias_way):
    lydias_location = Point(0, 0)
    lydias_last_step = lydias_way[-1]
    go_east_as_far_as_possible = True if lydias_last_step == "E" else False

    my_location = Point(0,0)
    my_way = []

    for lydias_step in lydias_way:
        if lydias_location.x == my_location.x and lydias_location.y == my_location.y:
            if lydias_step == "E":
                my_location = Point(my_location.x + 1, my_location.y)
                my_way.append("S")
            else:
                my_location = Point(my_location.x, my_location.y + 1)
                my_way.append("E")
        else:
            if go_east_as_far_as_possible:
                # We have to approach the last cell from above (north)
                if my_location.y + 1 <= N - 1:
                    my_location = Point(my_location.x, my_location.y + 1)
                    my_way.append("E")
                else:
                    my_location = Point(my_location.x + 1, my_location.y)
                    my_way.append("S")
            else:
                # We have to approach the last cell from left (west)
                if my_location.x + 1 <= N - 1:
                    my_location = Point(my_location.x + 1, my_location.y)
                    my_way.append("S")
                else:
                    my_location = Point(my_location.x, my_location.y + 1)
                    my_way.append("E")
        lydias_location = update_lydias_location(lydias_location, lydias_step)

    res = ''.join(my_way)
    return res

def update_lydias_location(prev_location, move):
    if move == "E":
        lydias_location = Point(prev_location.x, prev_location.y + 1)
    else:
        lydias_location = Point(prev_location.x + 1, prev_location.y)
    return lydias_location

number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N = int(input())
    lydias_way = str(input())

    res = walk_maze(N, lydias_way)
    print("Case #{}: {}".format(i, res))

# def main():
#     N = 5
#     lydias_way = "SEEEESSS"
#     print(walk_maze(N, lydias_way))

# if __name__ == "__main__":
#     main()
    
    
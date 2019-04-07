
from collections import namedtuple
import sys
# sys.setrecursionlimit(10000)

Point = namedtuple("Point", ["x", "y"])
Move = namedtuple("Move", ["Point", "Direction"])

def own_way(N, lydias_way):
    lydias_moves = compute_lydias_moves(lydias_way)
    # Primitve types (e.g. boolean) are not found in the scope of the recursive function
    # see: https://stackoverflow.com/a/13277359/6743087
    solution_found = [False]

    def solve_maze(current_moves):
        move = current_moves[-1]
        move_is_valid = check_if_move_is_valid(N, move, lydias_moves)
        location = move.Point
        
        if ((location.x == N - 1 and location.y == N - 2 and move.Direction == "E") or (location.x == N - 2 and location.y == N - 1 and move.Direction == "S")) and move_is_valid:
            solution_found[-1] = True
            results.append(current_moves)
            return
        
        if move_is_valid and not solution_found[-1]:
            if move.Direction == "S":
                new_location = Point(location.x + 1, location.y)
            elif move.Direction == "E":
                new_location = Point(location.x, location.y + 1)

            go_south = Move(new_location, "S")
            go_east = Move(new_location, "E")
            solve_maze(current_moves + [go_south])
            solve_maze(current_moves + [go_east])
    
    results = []
    start_south = Move(Point(0, 0), "S")
    start_east = Move(Point(0, 0), "E")
    solve_maze([start_east])
    solve_maze([start_south])
    
    if len(results) > 0:
        moves = results[-1]
        directions = [move.Direction for move in moves]
        res = ''.join(directions)
        return res
    else:
        return "S"


def check_if_move_is_valid(N, move, lydias_moves):
    location = move.Point

    if (location.x, location.y) in lydias_moves:
        if lydias_moves[(location.x, location.y)].Direction == move.Direction:
            # Lydia made that move already
            return False

    if location.x > N - 1 or location.y > N - 1 :
        # Outside of maze
        return False
    # Move is valid
    return True



def compute_lydias_moves(lydias_way):
    location = Point(0, 0)
    lydias_moves = {}
    for direction in lydias_way:
        move = Move(location, direction)
        lydias_moves[(location.x, location.y)] = move
        
        if direction == "S":
            location = Point(location.x + 1, location.y)
        else:
            location = Point(location.x, location.y + 1)
    return lydias_moves

number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N = int(input())
    lydias_way = str(input())

    res = own_way(N, lydias_way)
    print("Case #{}: {}".format(i, res))


# def main():
#     N = 5
#     lydias_way = "EESSSESE"
#     print(own_way(N, lydias_way))

# if __name__ == "__main__":
#     main()
    
    
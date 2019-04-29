def get_best(vals):
    if len(vals) == 0:
        return 0
    coords = list(vals.keys())
    coords.sort()
    best = 0
    best_score = 0
    cur_score = 0
    for coord in coords:
        # cur_score: number of ppl interested in coord
        cur_score += vals[coord]
        if cur_score > best_score:
            best_score = cur_score
            best = coord
    return best


def inc(dic, key, v):
    if key not in dic:
        dic[key] = 0
    dic[key] += v


def solve(Q, persons):
    xs = {}
    ys = {}

    for p in persons:
        x, y, d = p[0], p[1], p[2]
        if d == "E":
            inc(xs, x + 1, 1)
        elif d == "W":
            inc(xs, x, -1)
        elif d == "N":
            inc(ys, y + 1, 1)
        elif d == "S":
            inc(ys, y, -1)

    x = get_best(xs)
    y = get_best(ys)

    return x, y


number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    p, q = list(map(int, input().split()))

    persons = []
    for _ in range(p):
        x, y, d = input().split()
        x, y = int(x), int(y)
        persons.append((x, y, d))

    res = solve(q, persons)
    print("Case #{}: {} {}".format(i, res[0], res[1]))


def main():
    persons = [(0, 3, "N"), (0, 3, "N"), (0, 4, "N"), (0, 5, "S"), (0, 5, "S"), (0, 8, "S"),
               (1, 5, "W"), (0, 2, "S")]
    persons = [(0, 3, "N"), (0, 3, "N"), (0, 4, "N"), (0, 5, "S")]

    # persons = [(2, 4, "N"), (2, 6, "S"), (1, 5, "E"), (3, 5, "W")]
    #
    # persons = [(5, 5, "N")]
    print(solve(10, persons))


if __name__ == "__main__":
    main()

import functools


class Stone:
    def __init__(self, time, energy, lose):
        self.time = time
        self.energy = energy
        self.lose = lose


def maximize_energy(n, stone_values):
    stones = []
    for val in stone_values:
        stones.append(Stone(val[0], val[1], val[2]))

    stones.sort(key=lambda stone: stone.time / stone.lose if stone.lose != 0 else float('inf'))

    max_time = functools.reduce(lambda max_time, stone: max_time + stone.time, stones, 0)
    num_stones = len(stone_values)
    cache = [[None] * num_stones for _ in range(max_time)]

    def choose_stones(time, stone_idx):
        cur_stn = stones[stone_idx]

        if stone_idx == num_stones - 1:
            cache[time][stone_idx] = max(0, cur_stn.energy - (cur_stn.lose * time))
            return cache[time][stone_idx]

        if cache[time][stone_idx] is None:
            stone_energy = max(0, cur_stn.energy - (cur_stn.lose * time))

            take_stone = choose_stones(time + cur_stn.time, stone_idx + 1) + stone_energy
            dont_take_stone = choose_stones(time, stone_idx + 1)
            cache[time][stone_idx] = max(take_stone, dont_take_stone)
        return cache[time][stone_idx]

    max_energy = choose_stones(0, 0)
    return max_energy


number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N = input()
    N = int(N)

    s_v = []
    for _ in range(N):
        si, ei, li = input().split()
        si = int(si)
        ei = int(ei)
        li = int(li)
        s_v.append((si, ei, li))
    result = maximize_energy(N, s_v)
    print("Case #{}: {}".format(i, result))

# def main():
#     N = 3
#     stone_values = [(10, 4, 1000), (10, 3, 1000), (10, 8, 1000)]
#     print(maximize_energy(N, stone_values))
#
#
# if __name__ == "__main__":
#     main()

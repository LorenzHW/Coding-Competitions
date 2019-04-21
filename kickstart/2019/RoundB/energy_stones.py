class Stone:
    def __init__(self, time, energy, lose):
        self.time = time
        self.energy = energy
        self.lose = lose


def maximize_energy(N, stone_values):
    all_stones = set()
    for s, e, l in stone_values:
        all_stones.add(Stone(s, e, l))

    energies = []

    def eat(current_stone, other_stones, current_energy):
        other_stones = update_other_stones(other_stones, current_stone)
        for stone in other_stones:
            os = get_other_stones(stone, other_stones)
            eat(stone, os, current_energy + stone.energy)

        if not other_stones:
            energies.append(current_energy)

    for s in all_stones:
        others = get_other_stones(s, all_stones)
        eat(s, others, s.energy)

    energies.sort()
    max_energy = energies[-1]
    return max_energy


def update_other_stones(other_stones, current_stone):
    for stone in other_stones:
        stone.energy -= (stone.lose * current_stone.time)

    new_stones = set()
    for stone in other_stones:
        if stone.energy >= 0:
            new_stones.add(stone)
    return new_stones


def get_other_stones(current_stone, all_stones):
    new_stones = set()
    for stone in all_stones:
        if stone != current_stone:
            new_stones.add(Stone(stone.time, stone.energy, stone.lose))
    return new_stones


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

# if __name__ == "__main__":
#     # N = 7
#     # stone_values = [(20, 10, 1), (5, 30, 5), (100, 30, 1), (5, 80, 60)]
#     # N = 3
#     # stone_values = [(10, 4, 1000), (10, 3, 1000), (10, 8, 1000)]
#
#     N = 2
#     stone_values = [(12, 300, 50), (5, 200, 0)]
#     #     #   # stone_values = [(10, 4, 1000)]
#     print(maximize_energy(N, stone_values))

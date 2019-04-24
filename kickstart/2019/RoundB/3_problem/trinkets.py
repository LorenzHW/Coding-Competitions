def get_trinkets(N, S, types):

    return max_energy




# number_of_test_cases = int(input())
# for i in range(1_problem, number_of_test_cases + 1_problem):
#     N = input()
#     N = int(N)
#
#     s_v = []
#     for _ in range(N):
#         si, ei, li = input().split()
#         si = int(si)
#         ei = int(ei)
#         li = int(li)
#         s_v.append((si, ei, li))
#     result = maximize_energy(N, s_v)
#     print("Case #{}: {}".format(i, result))

if __name__ == "__main__":
  N = 6
  S = 2 # and the maximum number of trinkets allowed of a single type
  trinket_types = [1, 1, 4, 1, 4, 4,]
#   N = 3
#   stone_values = [(10, 4, 1000), (10, 8, 1010), (10, 8, 1000), (10, 3, 1000)]
#   # stone_values = [(10, 4, 1000)]
  print(get_trinkets(N, S, trinket_types))

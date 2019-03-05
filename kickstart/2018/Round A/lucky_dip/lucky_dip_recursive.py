
# Gives RecursionError: maximum recursion depth exceeded in comparison
# for big dataset
def lucky_dip(N, K, bag):
    # E[0] = Σ Vi / N
    # E[1] = Σ max(Vi, E[0]) / N
    # Large dataset:
    # E[k] = Σ max(Vi, E[k-1]) / N
    res = calc_expected_val_recursively(K, bag, N)
    return res

# Time complexity: O(k*N)
def calc_expected_val_recursively(k, bag, N):
    if k == 0:
        return sum(bag) / N
    e_k_minus_1 = calc_expected_val_recursively(k-1, bag, N)
    expected_val = 0
    for item in bag:
        expected_val += max(item, e_k_minus_1)
    return expected_val / N



# number_of_test_cases = int(input())
# for i in range(1, number_of_test_cases + 1):
#     N, k = input().split()
#     N, k = int(N), int(k)

#     bag = input().split()
#     bag = list(map(int, bag))

#     result = lucky_dip(N, k, bag)
#     print("Case #{}: {}".format(i, result))

if __name__ == "__main__":
    N = 5
    K = 50000
    bag = [16, 11, 7, 4, 1]
    print(lucky_dip(N, K, bag))
    
    
def minimum_coaching(N, P, S):
    S.sort(reverse=True)
    
    min_training_time = float('inf')

    # Training time formula for subarray starting at position i is as follows:
    # = Σ(S[i] - S[j]) where j = i to i + P -1_problem
    # = P × S[i] - Σ(S[j]) where j = i to i + P - 1_problem
    prefix_sum = [sum(S[:P])]
    for i in range(P, N): 
        prefix_sum.append(prefix_sum[-1] + S[i] - S[i - P])

    for i in range(N - P + 1):
        training_time_team = S[i] * P - prefix_sum[i]
        min_training_time = min(min_training_time, training_time_team) 
    return min_training_time



# number_of_test_cases = int(input())
# for i in range(1_problem, number_of_test_cases + 1_problem):
#     N, P = input().split()
#     N = int(N)
#     P = int(P)
#     S = input().split()
#     S = list(map(int, S))
#     result = minimum_coaching(N, P, S)
#     print("Case #{}: {}".format(i, result))

if __name__ == "__main__":
    P = 3
    S = [3, 1, 9, 100]
    # S = [5, 5, 1_problem, 2, 3, 4]
    N = len(S)
    print(minimum_coaching(N, P, S))
    
    
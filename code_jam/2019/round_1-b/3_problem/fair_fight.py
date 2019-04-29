def solve(k, charles_skill, delilas_skill):
    charles = generate_cont_subarrays(charles_skill)
    delila = generate_cont_subarrays(delilas_skill)

    pairs = 0
    for i in range(len(charles)):
        charles_sword_skill = max(charles[i])
        delilas_sword_skill = max(delila[i])

        if abs(charles_sword_skill - delilas_sword_skill) <= k:
            pairs += 1
    return pairs


def generate_cont_subarrays(array):
    sub_arrays = []
    for windows_size in range(1, len(array) + 1):
        for i in range(len(array) - windows_size + 1):
            sub_arrays.append(array[i:i + windows_size])
    return sub_arrays


number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    _, k = list(map(int, input().split()))
    c_skills = list(map(int, input().split()))
    d_skills = list(map(int, input().split()))

    res = solve(k, c_skills, d_skills)
    print("Case #{}: {}".format(i, res))


def main():
    k = 2
    charles_skill = [1, 2, 3, 4, 5]
    delilas_skill = [5, 5, 5, 5, 10]
    print(solve(k, charles_skill, delilas_skill))


if __name__ == "__main__":
    main()

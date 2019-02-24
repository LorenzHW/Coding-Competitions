import functools


# def calc_max_beauty_score(beauty_score, number_of_sections):
#     beauty_score_list = [int(value) for value in beauty_score]

#     if (number_of_sections % 2) == 0:
#         sections_to_paint = len(beauty_score_list) // 2
#     else:
#         sections_to_paint = len(beauty_score_list) // 2
#         sections_to_paint += 1

#     max_beauty_score = functools.reduce(lambda acc, val: acc + val, beauty_score_list[:sections_to_paint], 0)

#     cur_beauty_score = max_beauty_score
#     for i in range(sections_to_paint, len(beauty_score_list)):
#         cur_beauty_score += beauty_score_list[i]
#         cur_beauty_score -= beauty_score_list[i - sections_to_paint]
#         max_beauty_score = max(max_beauty_score, cur_beauty_score) 
#     return max_beauty_score


# number_of_test_cases = int(input())

# for i in range(1, number_of_test_cases + 1):
#     number_of_sections = int(input())
#     beauty_score = input()

#     max_beauty_score = calc_max_beauty_score(beauty_score, number_of_sections)
#     print("Case #{}: {}".format(i, max_beauty_score))

# if __name__ == "__main__":
#     EXPECTED_OUTPUT = ['Case #1: 6', 'Case #2: 31']
#     N = [4, 10]
#     BEAUTY_SCORES = ['1332', '1029384756']
#     output = calc_max_beauty_score(BEAUTY_SCORES[1], N[1])
#     pass


def solve(N, A):
    # print "Input:", N, A
    B = [0] * (N + 1)
    for i in range(1, N + 1):
        B[i] = B[i - 1] + A[i - 1]
    res = 0
    half = (N + 1) // 2
    for i in range(N):
        if i + half <= N:
            res = max(res, B[i + half] - B[i])
    return res


def main(bs, N):

    # T = int(input().strip())
    for i in range(1):
        # N = int(input().strip())
        A = list(map(int, bs))
        res = solve(N, A)
        out = "Case #%d: %s\n" % (i + 1, res)
        # print out
        # fo.write(out)


if __name__ == "__main__":
    EXPECTED_OUTPUT = ['Case #1: 6', 'Case #2: 31']
    N = [4, 10]
    BEAUTY_SCORES = ['1332', '1029384756']
    output = main(BEAUTY_SCORES[1], N[1])
    pass

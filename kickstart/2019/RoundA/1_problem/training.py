from collections import deque


def minimum_coaching(N, P, S):
    S.sort()
    current_team = deque(S[:P]) 
    res = hours_of_coaching(current_team)

    for skill in S[P:]:
        current_team.append(skill)
        current_team.popleft()
        
        time_needed = hours_of_coaching(current_team)
        if time_needed < res:
            res = time_needed
    return res

# student_skills is of size P and is sorted
def hours_of_coaching(student_skills):
    max_skill = student_skills[-1]
    hours_of_coaching = 0

    for skill in student_skills:
        hours_of_coaching += max_skill - skill
    return hours_of_coaching


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
    N = 4
    P = 3
    S = [3, 1, 9, 100]
    print(minimum_coaching(N, P, S))
    
    
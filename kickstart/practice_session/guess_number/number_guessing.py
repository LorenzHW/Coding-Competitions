number_of_test_cases = int(input())

for test_case in range(number_of_test_cases):
    intervall = input().split()
    lower_bound = int(intervall[0])
    upper_bound = int(intervall[1])
    number_of_tries = int(input())

    judge_response = None
    i = 0
    while i < number_of_tries:
        guess = (lower_bound + upper_bound) // 2
        print(guess)
        judge_response = input()
        if judge_response == 'TOO_SMALL':
            lower_bound = guess + 1
        elif judge_response == 'TOO_BIG':
            upper_bound = guess
        elif judge_response == 'CORRECT':
            break
        i += 1


def forgone_solution(N):
    A = [int(c) for c in str(N - 1)]
    B = [1]
    while True:
        res = add(A, B)
        if not number_has_4(A) and not number_has_4(B):
            return list_to_int(A), list_to_int(B)
        A = remove_4(A)
        B = get_complement(N, A)

def get_complement(N, number_as_list):
    i = list_to_int(number_as_list)
    complement = N - i
    complement_list = [int(c) for c in str(complement)]
    return complement_list


def remove_4(number_as_list, going_down=None):
    for i, integer in enumerate(number_as_list):
        if integer == 4:
            number_as_list[i] = 3
    return number_as_list

def list_to_int(number_as_list):
    number_as_list = ''.join(map(str, number_as_list))
    return int(number_as_list)

def add(A, B):
    A = list_to_int(A)
    B = list_to_int(B)
    return A + B


def number_has_4(number):
    for c in str(number):
        if c == '4':
            return True
    return False

number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N = int(input())

    a, b = forgone_solution(N)
    print("Case #{}: {} {}".format(i, a, b))


# def main():
#     N = 4444
#     print(forgone_solution(N))

# if __name__ == "__main__":
#     main()
    
    
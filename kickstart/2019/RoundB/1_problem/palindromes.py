import string


def palindromes(N, Q, input_string, L_Rs):
    prefix_sum_arrays = create_prefix_sum_array_for_every_letter(input_string)

    number_or_palindromes = 0
    for l_r in L_Rs:
        l = l_r[0] - 1
        r = l_r[1] - 1
        number_or_palindromes += is_palindrome(l, r, prefix_sum_arrays)
    return number_or_palindromes


def is_palindrome(l, r, prefix_sum_arrays):
    chars = {}
    for letter in string.ascii_uppercase:
        ps_array = prefix_sum_arrays.get(letter)
        if l > 0:
            chars[letter] = (ps_array[r] - ps_array[l - 1]) % 2
        else:
            chars[letter] = (ps_array[r]) % 2

    counter = 0
    for k, v in chars.items():
        if v == 1:
            counter += 1

        if counter == 2:
            return False
    return True


def create_prefix_sum_array_for_every_letter(input_string):
    prefix_sum_arrays = {}
    for letter in string.ascii_uppercase:
        arr = []
        counter = 0
        for c in input_string:
            if c == letter:
                counter += 1
            arr.append(counter)
        prefix_sum_arrays[letter] = arr
    return prefix_sum_arrays


# number_of_test_cases = int(input())
# for i in range(1_problem, number_of_test_cases + 1_problem):
#     N, Q = input().split()
#     N = int(N)
#     Q = int(Q)
#
#     str_inp = input()
#     L_Rs = []
#     for _ in range(Q):
#       l, r = input().split()
#       l = int(l)
#       r = int(r)
#       L_Rs.append((l, r))
#     result = palindromes(N, Q, str_inp, L_Rs)
#     print("Case #{}: {}".format(i, result))

if __name__ == "__main__":
    N = 7
    Q = 5
    input_str = "ABAACCA"
    L_Rs = [(3, 6), (4, 4), (2, 5), (6, 7), (3, 7)]
    print(palindromes(N, Q, input_str, L_Rs))

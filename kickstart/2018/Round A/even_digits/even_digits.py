def get_all_even_digits(N):
    N_as_str = str(N)
    N_as_list = [int(c) for c in N_as_str]
    
    first_odd_idx = None
    for i, number in enumerate(N_as_list):
        if number % 2 != 0:
            first_odd_idx = i
            break
    
    # No odd integer
    if first_odd_idx is None:
        return 0

    next_lower_as_list = get_next_lower_beautiful_int(N_as_list.copy(), first_odd_idx)
    next_upper_as_list = get_next_upper_beautiful_int(N_as_list.copy(), first_odd_idx)
    
    s = list(map(str, next_lower_as_list))
    next_lower = int(''.join(s))

    s = list(map(str, next_upper_as_list))
    next_upper = int(''.join(s))
    number_of_plus_button_pushes = next_upper - N
    number_of_minus_button_pushes = N - next_lower

    return min(number_of_plus_button_pushes, number_of_minus_button_pushes)

def get_next_lower_beautiful_int(N_as_list, first_odd_idx):
    for i in range(first_odd_idx + 1, len(N_as_list)):
        N_as_list[i] = 8
    
    N_as_list[first_odd_idx] = N_as_list[first_odd_idx] - 1    
    return N_as_list


def get_next_upper_beautiful_int(N_as_list, first_odd_idx):
    for i in range(first_odd_idx + 1, len(N_as_list)):
        N_as_list[i] = 0

    N_as_list[first_odd_idx] += 1
    if N_as_list[first_odd_idx] == 10:
        N_as_list[first_odd_idx] = 0
        carry = True
    else:
        carry = False

    # Example: 88 9714
    # Next number: 200 0000
    for i in reversed(range(0, first_odd_idx)):
        if carry:
            N_as_list[i] += 2

            if N_as_list[i] == 10:
                N_as_list[i] = 0
                carry = True
    
    # Example: 88 9714
    # Next number: 200 0000
    # First number was an 8 --> Add 2 and swap
    if carry:
        N_as_list.append(2)
        N_as_list[0], N_as_list[-1] = N_as_list[-1], N_as_list[0]

    return N_as_list

number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N = int(input())

    result = get_all_even_digits(N)
    print("Case #{}: {}".format(i, result))

# if __name__ == "__main__":
#     print(get_all_even_digits(42))
    
    

def no_nine(F, L):
    res = get_valid_numbers(L) - get_valid_numbers(F) + 1
    return int(res)

    
    
def get_valid_numbers(number):
    number_as_list = [int(c) for c in str(number)]
    last_number = number_as_list[-1]
    c = get_c(number_as_list)

    
    res = 8*c/9
    res += check_last_couple_of_digits(number, last_number)
    return res

def get_c(number_as_list):
    # See analysis to know what c is
    number_as_list[-1] = 0

    num_digits_without_nine = 0
    for i, num in enumerate(reversed(number_as_list)):
        num_digits_without_nine += num * 9**i

    return num_digits_without_nine
    

def check_last_couple_of_digits(number, last_number):
    valid_digits = 0
    last_digits = number - last_number
    while last_digits <= number:
        if last_digits % 9 != 0 and '9' not in str(last_digits):
            valid_digits += 1
        last_digits += 1
    return valid_digits

number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    F, L = input().split()
    F, L = int(F), int(L)

    result = no_nine(F, L)
    print("Case #{}: {}".format(i, result))

if __name__ == "__main__":
    F = 88
    L = 102
    print(no_nine(F, L))
    
    
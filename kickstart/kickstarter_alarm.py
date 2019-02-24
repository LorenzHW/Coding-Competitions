import functools

MODULO = 1000000007

def calc_power_for_alarm(parameters):
    parameters = parameters.split()
    config_array = create_config_array(parameters)
    N = parameters[0]
    K = parameters[1]
    POWER = 0
    i_power = 0


    for i in range(1, N+1):
        power_sum(i, K)
    



def power_sum(i, K):
    if i == 1:
        return K
    first_power = power_increase(i, K+1)-1
    second_pwer = power_increase(i-1, MODULO - 2)
    return (( first_power * second_pwer  + MODULO - 1 ) % MODULO);

def power_increase(X, N):
    if N == 0:
        return 1
    if N == 1:
        return X
    res = power_increase(X, N//2)



def create_config_array(parameters):
    parameters = [int(val) for val in parameters]

    N = parameters[0]
    K = parameters[1]
    x_1 = parameters[2]
    y_1 = parameters[3]
    C = parameters[4]
    D = parameters[5]
    E_1 = parameters[6]
    E_2 = parameters[7]
    F = parameters[8]

    config_array = [(x_1 + y_1) % F]
    x_old = x_1
    y_old = y_1
    for i in range(1, N):
        x_i = calculate_x_i(C, x_old, D, y_old, E_1, F)
        y_i = calculate_y_i(D, x_old, C, y_old, E_2, F)

        config_array.append((x_i + y_i) % F)
        x_old = x_i
        y_old = y_i
    return config_array

def calculate_x_i(C, x_old, D, y_old, E_1, F):
    x = (C * x_old + D * y_old + E_1) % F
    return x

def calculate_y_i(D, x_old, C, y_old, E_2, F):
    y = (D * x_old + C * y_old + E_2) % F
    return y




# number_of_test_cases = int(input())
# for i in range(1, number_of_test_cases + 1):
#     number_of_sections = int(input())
#     beauty_score = input()

#     max_beauty_score = calc_max_beauty_score(beauty_score, number_of_sections)
#     print("Case #{}: {}".format(i, max_beauty_score))

if __name__ == "__main__":
    EXPECTED_OUTPUT = ['Case #1: 6', 'Case #2: 31']
    PARAMETERS = ['2 3 1 2 1 2 1 1 9']
    output = calc_power_for_alarm(PARAMETERS[0])
    pass
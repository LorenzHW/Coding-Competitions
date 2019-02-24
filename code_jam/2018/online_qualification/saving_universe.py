def save_universe(shield, program):
    program = list(map(str, program))
    shield = int(shield)

    dmg = check_dmg(program)
    modified_program = program
    number_of_hacks = 0
    while dmg > shield:
        modified_program = hack_program_once(modified_program)
        if modified_program != -1:
            dmg = check_dmg(modified_program)
            number_of_hacks += 1
        else:
            return 'IMPOSSIBLE'
    return str(number_of_hacks)
        

def hack_program_once(program):
    # remove all 'C' at the end
    highest_c_instr_idx = None
    for i in range(1, len(program)):
        if program[i] == 'S' and program[i - 1] == 'C':
            highest_c_instr_idx = i - 1

    # swap:
    if highest_c_instr_idx is not None:
        program[highest_c_instr_idx], program[highest_c_instr_idx + 1] = program[highest_c_instr_idx + 1], program[highest_c_instr_idx]
        return program
    else:
        return -1


def check_dmg(program):
    current_beam = 1
    dmg = 0
    for instruction in program:
        if instruction == 'S':
            dmg += current_beam
        elif instruction == 'C':
            current_beam *= 2
    return dmg

number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    shield, program = input().split()
    res = save_universe(shield, program)
    print("Case #{}: {}".format(i, res))


# if __name__ == "__main__":
#     SHIELD = ['3']
#     PROGRAMS = ['CSCSS']
#     save_universe(SHIELD[0], PROGRAMS[0])
    
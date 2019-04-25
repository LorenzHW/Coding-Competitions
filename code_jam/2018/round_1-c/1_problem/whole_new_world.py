def whole_new_world(N, L, words):
    letters_lists = [[] for _ in range(L)]
    for i in range(N):
        for j in range(L):
            s = letters_lists[j]
            s.append(words[i][j])

    words = set(words)

    def generate_word(current_word, letters_lists_idx):
        if len(current_word) == L:
            current_word = ''.join(current_word)
            if current_word not in words:
                return current_word
            else:
                return None

        letter_list = letters_lists[letters_lists_idx]

        for letter in letter_list:
            word = generate_word(current_word + [letter], letters_lists_idx + 1)
            if word:
                return word

    word = generate_word([], 0)
    if word:
        return word
    else:
        return '-'


number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N, L = input().split()
    N, L = int(N), int(L)

    words = []
    for _ in range(N):
        words.append(input())

    res = whole_new_world(N, L, words)
    print("Case #{}: {}".format(i, res))

def main():
    N = 3
    L = 4
    words = ["AA", "AB", "BA", "BB"]
    # words = ["A", "B", "C", "D"]
    words = ["CAKE", "TORN", "SHOW"]
    # words = ["WW", "AA", "SS", "DD"]
    print(whole_new_world(N, L, words))


if __name__ == "__main__":
    main()

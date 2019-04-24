from trie import TrieNode, add


def rhyme(N, words):
    root = TrieNode('*')

    for w in words:
        w = w[::-1]
        add(root, w)

    def calc_minimum_num_of_unpaired_words(node):
        """
        Calculates the minimum number of unpaired words for each node.
        :param node: The current node.
        :return: Number of unpaired words at that node.
        """
        if len(node.children) == 0:
            # Got leave --> word ends here
            return 1

        r = sum(calc_minimum_num_of_unpaired_words(c) for c in node.children)
        if node.word_finished:
            # Word finishes --> got a new word here
            r += 1
        if node.char != '*' and r >= 2:
            # If we have more than two words, we can pair them and remove
            # them.
            r = r - 2
        return r

    fv_root = calc_minimum_num_of_unpaired_words(root)
    result = N - fv_root
    return result


# number_of_test_cases = int(input())
# for i in range(1, number_of_test_cases + 1):
#     N = int(input())
#
#     words = []
#     for _ in range(N):
#         words.append(input())
#
#     res = rhyme(N, words)
#     print("Case #{}: {}".format(i, res))
#

def main():
    N = 2
    words = ["JAM", "HAM", ]

    # N = 3
    # words = ["TARPOR", "PROL", "TARPRO"]
    print(rhyme(N, words))


if __name__ == "__main__":
    main()

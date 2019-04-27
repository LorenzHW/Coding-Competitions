from collections import defaultdict


def find_different_suffix(grouped):
    """
    Checks whether two different suffixes exist
    If so, the prefixes of those suffixes are returned
    :param grouped: splitted words
    :return: Prefixes of different suffixes if they exist otherwise none
    """
    items = list(grouped.items())
    prefix, suffixes = items[0]
    for other_prefix, other_suffixes in items[1:]:
        if suffixes != other_suffixes:
            return prefix, other_prefix
    return None, None


def diff(set1, set2):
    """
    Checks if the suffix of set1 is in set2
    :param set1: set of suffixes
    :param set2: set of suffixes
    :return: A suffix that is in set2 but not in set1
    """
    for suffix in set2:
        if suffix not in set1:
            return suffix


def generate_word(grouped):
    prefix, other_prefix = find_different_suffix(grouped)
    if prefix is None:
        # All suffixes are the same --> not possible to to generate a different word
        return None

    # Ok, so we know a different suffix exists. Does it exist in
    # grouped[other_prefix]
    other_suffix = diff(grouped[prefix], grouped[other_prefix])
    if other_suffix:
        return prefix + other_suffix

    # Looks like it does not. So it has to exist in grouped[prefix]
    other_suffix = diff(grouped[other_prefix], grouped[prefix])
    return other_prefix + other_suffix


def whole_new_world(L, words):
    words = set(words)

    for i in range(1, L):
        grouped = defaultdict(set)
        for word in words:
            grouped[word[:i]].add(word[i:])
        w = generate_word(grouped)
        if w is not None:
            return w
    return "-"


number_of_test_cases = int(input())
for i in range(1, number_of_test_cases + 1):
    N, L = input().split()
    N, L = int(N), int(L)

    words = []
    for _ in range(N):
        words.append(input())

    res = whole_new_world(L, words)
    print("Case #{}: {}".format(i, res))


def main():
    L = 2
    words = ["AA", "AB", "BA", "BB"]

    # L = 1
    # words = ["A", "B", "C", "D"]
    #
    # L = 4
    # words = ["CAKE", "TORN", "SHOW"]
    #
    # L = 2
    # words = ["WW", "AA", "SS", "DD"]
    #
    # L = 7
    # words = ["HELPIAM", "TRAPPED", "INSIDEA", "CODEJAM", "FACTORY"]
    #
    # L = 2
    # words = ["TT", "TT"]

    print(whole_new_world(L, words))


if __name__ == "__main__":
    main()

from collections import defaultdict


def find_different_suffix(grouped):
    items = grouped.items()
    (prefix, suffixes) = items[0]
    for other_prefix, other_suffixes in items[1:]:
        if suffixes != other_suffixes:
            return (prefix, other_prefix)
    return (None, None)


def diff(set1, set2):
    for v in set2:
        if v not in set1:
            return v
    return None


def generate_word(grouped):
    if len(grouped) <= 1:
        return None
    (prefix, other_prefix) = find_different_suffix(grouped)
    if prefix is None:
        return None
    suffix_only_in_other = diff(grouped[prefix], grouped[other_prefix])
    if suffix_only_in_other is not None:
        return prefix + suffix_only_in_other

    suffix_only_in_this = diff(grouped[other_prefix], grouped[prefix])
    return other_prefix + suffix_only_in_this


def solve(words, L):
    for split in range(1, L):
        grouped = defaultdict(set)
        for word in words:
            grouped[word[:split]].add(word[split:])
        word = generate_word(grouped)
        if word is not None:
            return word
    return "-"

def main():
    N = 3
    L = 4
    # words = ["AA", "AB", "BA", "BB"]
    # words = ["A", "B", "C", "D"]
    words = ["CAKE", "TORN", "SHOW"]
    # words = ["WW", "AA", "SS", "DD"]
    print(solve(words, L))


if __name__ == "__main__":
    main()

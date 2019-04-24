from typing import Tuple


class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.
        self.word_finished = False
        # How many times does this character appear in the addition proccess
        self.counter = 1


def add(root, word: str):
    """
    Adding a word in the trie structure.
    """

    node = root
    for char in word:
        found_in_child = False
        # Search for the character in the children of present 'node'
        for child in node.children:
            if child.char == char:
                # We found it, increase the counter by 1 to keep track that another word has it as
                # well.
                child.counter += 1
                # And point the node to the child that contains this char
                node = child
                found_in_child = True
                break

        # We did not find it --> add a new child
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            # And then point node to the new child
            node = new_node

    node.word_finished = True


def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Check and return
      1. If the prefix exsists in any of the words we added so far
      2. If yes then how may words actually have the prefix
    """
    node = root
    if not root.children:
        return False, 0

    for char in prefix:
        char_not_found = True
        # Search through all the children of the present 'node'
        for child in node.children:
            if child.char == char:
                # Found char existing in the child
                char_not_found = False
                # Assign node as the child containing the char and break
                node = child
                break
        # Return False if we did not find a char.
        if char_not_found:
            return False, 0

    # True indicates that we found the prefix. Counter indicates how many words have that prefix
    return True, node.counter


if __name__ == "__main__":
    root = TrieNode('*')
    add(root, "hackathon")
    add(root, 'hack')

    print(find_prefix(root, 'hac'))
    print(find_prefix(root, 'hacka'))
    print(find_prefix(root, 'hackathon'))
    print(find_prefix(root, 'ha'))
    print(find_prefix(root, 'hammer'))
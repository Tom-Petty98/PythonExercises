class Trie:
    def search_level(self, current_level, current_prefix, words):
        if self.end_symbol in current_level:
            words.append(current_prefix)

        sorted_dict = dict(sorted(current_level.items()))
        for key in sorted_dict.keys():
            if key != self.end_symbol:              
                words = self.search_level(current_level[key], current_prefix + key, words)

        return words

    def words_with_prefix(self, prefix):
        matches = []
        current_level = self.root

        for char in prefix:
            if char not in current_level:
                return []
            current_level = current_level[char]

        return self.search_level(current_level, prefix, matches)

    # don't touch below this line

    def __init__(self):
        self.root = {}
        self.end_symbol = "*"

    def add(self, word):
        current_level = self.root
        for letter in word:
            if letter not in current_level:
                current_level[letter] = {}
            current_level = current_level[letter]
        current_level[self.end_symbol] = True

import json
from runtest import run_tests

run_cases = [
    (["dev", "devops", "designer", "director"], "de", ["dev", "devops", "designer"]),
    (["manager", "intern"], "z", []),
    (["cto", "cfo", "coo", "ceo"], "c", ["cto", "cfo", "coo", "ceo"]),
]

submit_cases = run_cases + [
    (
        ["developer", "designer", "devops", "director"],
        "de",
        ["developer", "designer", "devops"],
    ),
]


def test(words, prefix, expected_matches):
    print("---------------------------------")
    print("Trie:")
    trie = Trie()
    for word in words:
        trie.add(word)
    print(json.dumps(trie.root, sort_keys=True, indent=2))
    print(f'Words with prefix: "{prefix}":')
    print(f"Expecting: {sorted(expected_matches)}")
    try:
        actual = trie.words_with_prefix(prefix)
        print(f"Actual: {actual}")
        if (actual) == sorted(expected_matches):
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


run_tests(submit_cases, test)
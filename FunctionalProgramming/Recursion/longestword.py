from runtest import run_tests

def find_longest_word(document, longest_word=""):
    # Base case: If the document is empty, return the longest word
    if not document:
        return longest_word

    first_space = document.find(" ")
    if first_space == -1:  # No spaces found, meaning there's only one word left
        first_word = document
        rest = ""
    else:
        first_word = document[:first_space]
        rest = document[first_space + 1:]  # Remove the first word and the space

    if len(first_word) > len(longest_word):
        longest_word = first_word

    return find_longest_word(rest, longest_word)

run_cases = [
    ("Either that wallpaper goes, or I do.", "wallpaper"),
    (
        "Then I die happy",
        "happy",
    ),
    (
        "Et tu, Brute?",
        "Brute?",
    ),
]

submit_cases = run_cases + [
    (
        "",
        "",
    ),
    (
        " ",
        "",
    ),
    (
        "Let us cross over the river and rest under the shade of the trees",
        "cross",
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: '{input1}'")
    print(f"Expecting: '{expected_output}'")
    result = find_longest_word(input1)
    print(f"Actual: '{result}'")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


run_tests(submit_cases, test)
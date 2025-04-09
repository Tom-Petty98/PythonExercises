from functools import reduce

def lineator(line_length):
    def lineate(document):
        words = document.split()

        def add_word_to_lines(lines, word):
            if not lines:
                return [word,]
            current_line = lines[-1]
            if len(current_line) + len(word) + 1 > line_length:
                lines.append(word)
            else:
                lines[-1] = current_line + " " + word
            return lines

        return reduce(add_word_to_lines, words, [])

    return lineate

run_cases = [
    (
        10,
        "Autobots roll out! The Autobots are always ready for battle.",
        [
            "Autobots",
            "roll out!",
            "The",
            "Autobots",
            "are always",
            "ready for",
            "battle.",
        ],
    ),
    (
        20,
        "Optimus Prime is the leader of the Autobots. Megatron is the archenemy of the Autobots.",
        [
            "Optimus Prime is the",
            "leader of the",
            "Autobots. Megatron",
            "is the archenemy of",
            "the Autobots.",
        ],
    ),
    (
        30,
        "Autobots often disguise themselves as vehicles on Earth. The Autobots protect humanity from the Decepticons.",
        [
            "Autobots often disguise",
            "themselves as vehicles on",
            "Earth. The Autobots protect",
            "humanity from the Decepticons.",
        ],
    ),
]


submit_cases = run_cases + [
    (
        0,
        "",
        [],
    ),
    (
        0,
        "Cybertron is the home planet of the Autobots.",
        ["Cybertron", "is", "the", "home", "planet", "of", "the", "Autobots."],
    ),
    (
        90,
        "Bumblebee transforms into a yellow Camaro. Ratchet is the medical officer for the Autobots.",
        [
            "Bumblebee transforms into a yellow Camaro. Ratchet is the medical officer for the",
            "Autobots.",
        ],
    ),
]


def test(line_length, document, expected_output):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * line_length: {line_length}")
    print(f" * document: {document}")
    print(f"Expecting: {expected_output}")
    result = lineator(line_length)(document)
    print(f"   Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
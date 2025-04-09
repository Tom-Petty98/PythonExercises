from functools import reduce


def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"

    return tagger


def create_accumulator(tagger):
    def accumulate(items):
        return reduce(lambda acc, item: acc + tagger(item), items, "")

    return accumulate


tag_data = create_tagger("td")
tag_header = create_tagger("th")
tag_row = create_tagger("tr")
tag_table = create_tagger("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)


# don't touch above this line


def create_html_table(data_rows):
    rows = accumulate_rows(map(accumulate_data_cells, data_rows))

    def create_table_headers(headers):
        nonlocal rows
        header = tag_row(accumulate_headers(headers))
        table = header + rows
        return tag_table(table)

    return create_table_headers


run_cases = [
    (
        [
            ["Scooby Doo", "Lassie"],
            ["Blue", "Wishbone"],
        ],
        ["Cartoon TV Dogs", "Real TV Dogs"],
        "<table><tr><th>Cartoon TV Dogs</th><th>Real TV Dogs</th></tr><tr><td>Scooby Doo</td><td>Lassie</td></tr><tr><td>Blue</td><td>Wishbone</td></tr></table>",
    ),
]

submit_cases = run_cases + [
    (
        [
            ["Garfield", "Salem"],
            ["Tom", "Mr. Bigglesworth"],
        ],
        ["Cartoon TV Cats", "Real TV Cats"],
        "<table><tr><th>Cartoon TV Cats</th><th>Real TV Cats</th></tr><tr><td>Garfield</td><td>Salem</td></tr><tr><td>Tom</td><td>Mr. Bigglesworth</td></tr></table>",
    ),
]


def test(data_rows, headers, expected_output):
    print("---------------------------------")
    print(f"Data Rows: {data_rows}")
    print(f"Headers: {headers}")
    print(f"Expecting:\n{expected_output}")
    result = create_html_table(data_rows)(headers)
    print(f"Actual:\n{result}")
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

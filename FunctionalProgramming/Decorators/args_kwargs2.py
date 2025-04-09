from runtest import run_tests

#example
def log_call_count(func_to_decorate):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Called {count} times")
        # The * and ** syntax unpacks the arguments
        # and passes them to the decorated function
        return func_to_decorate(*args, **kwargs)

    return wrapper

#=======================================================================================

def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        args_list = list(map(convert_md_to_txt, args))

        for k in kwargs:
            kwargs[k] = convert_md_to_txt(kwargs[k])
            
        #their solution with no loop
        # def kwarg_item_to_txt(item_tuple):
        #     key, value = item_tuple
        #     return (key, convert_md_to_txt(value))

        # converted_kwargs = dict(map(kwarg_item_to_txt, kwargs.items()))    
        return func(*args_list, **kwargs)

    return wrapper


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)


@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""  First: {first_doc}
  Second: {second_doc}"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""  Title: {title}
  Body: {body}
  Conclusion: {conclusion}"""

run_cases = [
    (
        ("# We like to play it all", "## Welcome to Tally Hall"),
        {},
        concat,
        """  First: We like to play it all
  Second: Welcome to Tally Hall""",
    ),
    (
        set(),
        {
            "title": "Why Python is Great",
            "body": "Maybe it isn't",
            "conclusion": "## That's why Python is great!",
        },
        format_as_essay,
        """  Title: Why Python is Great
  Body: Maybe it isn't
  Conclusion: That's why Python is great!""",
    ),
]

submit_cases = run_cases + [
    (
        ("# Boots' grocery list", "Salmon, gems, arcanum crystals"),
        {
            "conclusion": "## Don't forget!",
        },
        format_as_essay,
        """  Title: Boots' grocery list
  Body: Salmon, gems, arcanum crystals
  Conclusion: Don't forget!""",
    ),
]


def test(args, kwargs, func, expected_output):
    print("---------------------------------")
    print(f"Positional Arguments:")
    for arg in args:
        print(f" * {arg}")
    print(f"Keyword Arguments:")
    for key, value in kwargs.items():
        print(f" * {key}: {value}")
    print(f"Expecting:")
    print(expected_output)
    try:
        result = func(*args, **kwargs)
    except Exception as error:
        result = f"Error: {error}"
    print(f"Actual:")
    print(result)
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


run_tests(submit_cases, test)
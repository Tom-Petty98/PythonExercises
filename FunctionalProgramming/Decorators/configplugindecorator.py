from runtest import run_tests

def configure_plugin_decorator(func):
    
    def wrapper(*args):
        kwargs = dict(args)
        return func(**kwargs)

    return wrapper

@configure_plugin_decorator
def configure_backups(path="~/backups", prefix="copy_", extension=".txt"):
    return {
        "path": path,
        "prefix": prefix,
        "extension": extension,
    }


@configure_plugin_decorator
def configure_login(user=None, password=None, token=None):
    return {
        "user": user,
        "password": password,
        "token": token,
    }


run_cases = [
    (
        configure_backups,
        [
            ("path", "~/documents"),
            ("extension", ".md"),
        ],
        {
            "path": "~/documents",
            "prefix": "copy_",
            "extension": ".md",
        },
    ),
    (
        configure_login,
        [
            ("user", "goku_fanatic"),
            ("password", "kakarot1989"),
        ],
        {
            "user": "goku_fanatic",
            "password": "kakarot1989",
            "token": None,
        },
    ),
]

submit_cases = run_cases + [
    (
        configure_backups,
        [
            ("path", "~/workspace/backups"),
            ("prefix", "backup_"),
        ],
        {
            "path": "~/workspace/backups",
            "prefix": "backup_",
            "extension": ".txt",
        },
    ),
    (
        configure_login,
        [
            ("user", "john_q_sample"),
            ("password", "p@$$w0rd"),
            ("token", "a09adc-0914sf-012la9-fa3sa0-2342ra"),
        ],
        {
            "user": "john_q_sample",
            "password": "p@$$w0rd",
            "token": "a09adc-0914sf-012la9-fa3sa0-2342ra",
        },
    ),
]


def test(func, args, expected_output):
    print("---------------------------------")
    print(f"Function: {func.__name__}")
    print("Positional Arguments:")
    for arg in args:
        print(f" * {arg}")
    print(f"Expecting:")
    print(expected_output)
    result = func(*args)
    print(f"Actual:")
    print(result)
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


run_tests(submit_cases, test)
def new_resizer(max_width, max_height):
    def set_min_size(min_width = 0, min_height = 0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        # def resize_image(width, height):
        #     if width < min_width:
        #         width = min_width
        #     elif width > max_width:
        #         width = max_width
        #     if height < min_height:
        #         height = min_height
        #     elif height > max_height:
        #         height = max_height
            
        #     return width, height 

        #their solution
        def resize_image(width, height):
            new_width = max(min_width, min(width, max_width))
            new_height = max(min_height, min(height, max_height))
            return new_width, new_height

        return resize_image
    return set_min_size

def new_resizer(max_width, max_height):
    def set_min_size(min_width=0, min_height=0):
        if min_width > max_width or min_height > max_height:
            raise Exception("minimum size cannot exceed maximum size")

        def resize_image(width, height):
            new_width = max(min_width, min(width, max_width))
            new_height = max(min_height, min(height, max_height))
            return new_width, new_height

        return resize_image

    return set_min_size

run_cases = [
    (
        (1920, 1080),
        (800, 600),
        [
            (
                (2560, 1440),
                (1920, 1080),
            ),
            (
                (500, 400),
                (800, 600),
            ),
            (
                (1600, 1000),
                (1600, 1000),
            ),
            (
                (800, 600),
                (800, 600),
            ),
            (
                (1920, 1080),
                (1920, 1080),
            ),
        ],
        None,
    ),
    (
        (1200, 800),
        (1600, 800),
        [],
        "minimum size cannot exceed maximum size",
    ),
    (
        (1600, 800),
        (1200, 1200),
        [],
        "minimum size cannot exceed maximum size",
    ),
]

submit_cases = run_cases + [
    (
        (1600, 1200),
        (1200, 800),
        [
            (
                (1601, 799),
                (1600, 800),
            ),
            (
                (1199, 1201),
                (1200, 1200),
            ),
        ],
        None,
    ),
    (
        (600, 600),
        (600, 600),
        [
            (
                (601, 601),
                (600, 600),
            ),
            (
                (599, 599),
                (600, 600),
            ),
        ],
        None,
    ),
    (
        (100, 100),
        (),
        [
            (
                (200, 200),
                (100, 100),
            ),
            (
                (0, 0),
                (0, 0),
            ),
        ],
        None,
    ),
]


def test(max_size, min_size, image_sizes, expected_error):
    print("---------------------------------")
    print(f"Max Size:  {max_size}")
    if min_size:
        print(f"Min Size:  {min_size}")
    try:
        resize_image = new_resizer(*max_size)(*min_size)
    except Exception as e:
        print(f"Expected Error: {expected_error}")
        print(f"  Actual Error: {str(e)}")
        if str(e) == expected_error:
            print("Pass")
            return True
        print("Fail")
        return False
    if expected_error is not None:
        print(f"Expected Error: {expected_error}")
        print("Fail")
        return False
    print("Resizing Images...")
    failed = False
    for size in image_sizes:
        result = resize_image(*size[0])
        print(f" * Image Size: {size[0]}")
        print(f" *   Expected: {size[1]}")
        print(f" *     Actual: {result}")
        if result == size[1]:
            print("Pass")
        else:
            print("Fail")
            print(result)
            print(size[1])
            failed = True
    passed = not failed
    return passed


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
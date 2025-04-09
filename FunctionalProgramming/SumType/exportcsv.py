from runtest import run_tests
from enum import Enum

class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4

#=============================================================================================
# My solution
def get_csv_status2(status, data):
    match (status):
        case (CSVExportStatus.PENDING):
            a = []
            for item in data:
                a.append(list(map(str, item)))
            return ("Pending...", a)
            #return ("Pending...", list(map(str, map(lambda item: item, data))))
        case (CSVExportStatus.PROCESSING):
            return ("Processing...", "\n".join(list(map(lambda items: ",".join(items), data))))
        case (CSVExportStatus.SUCCESS):
            return ("Success!", data)
        case (CSVExportStatus.FAILURE):
            result = get_csv_status2(CSVExportStatus.PENDING, data)
            result = get_csv_status2(CSVExportStatus.PROCESSING, result[1])
            return ("Unknown error, retrying...", result[1])
        case _:
            raise Exception("unknown export status")
        

#Their solution

def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            return prepare(data)
        case CSVExportStatus.PROCESSING:
            return process(data)
        case CSVExportStatus.SUCCESS:
            return handle_success(data)
        case CSVExportStatus.FAILURE:
            return handle_failure(data)
        case _:
            raise Exception("unknown export status")


def prepare(data):
    processed_data = list(map(lambda lst: list(map(lambda s: str(s), lst)), data))
    return "Pending...", processed_data


def process(prepared_data):
    processed_data = "\n".join(map(lambda lst: ",".join(lst), prepared_data))
    return "Processing...", processed_data


def handle_success(processed_data):
    return "Success!", processed_data


def handle_failure(data):
    _, processed_data = process(prepare(data)[1])
    return "Unknown error, retrying...", processed_data


try:
    (
        CSVExportStatus.PENDING
        and CSVExportStatus.PROCESSING
        and CSVExportStatus.SUCCESS
        and CSVExportStatus.FAILURE
    )
except Exception as error:
    print(f"Error: Missing attribute {error} from enum")

    class CSVExportStatus(Enum):
        PENDING = None
        PROCESSING = None
        SUCCESS = None
        FAILURE = None


run_cases = [
    (
        CSVExportStatus.PENDING,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Pending...",
            [
                ["Customer ID", "Billed", "Paid"],
                ["1", "100", "100"],
                ["2", "400", "99"],
                ["3", "50", "25"],
            ],
        ),
    ),
    (
        CSVExportStatus.PROCESSING,
        [
            ["Customer ID", "Billed", "Paid"],
            ["1", "100", "100"],
            ["2", "400", "99"],
            ["3", "50", "25"],
        ],
        (
            "Processing...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.SUCCESS,
        "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        (
            "Success!",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
    (
        CSVExportStatus.FAILURE,
        [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ],
        (
            "Unknown error, retrying...",
            "Customer ID,Billed,Paid\n1,100,100\n2,400,99\n3,50,25",
        ),
    ),
]

submit_cases = run_cases + [
    (
        CSVExportStatus.PENDING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Pending...",
            [
                ["Card Name", "Condition", "Value"],
                ["Sparky Mouse", "Fair", "100"],
                ["Moist Turtle", "Good", "200"],
                ["Burning Lizard", "Very Good", "1000"],
                ["Mossy Frog", "Poor", "10"],
            ],
        ),
    ),
    (
        CSVExportStatus.PROCESSING,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", "100"],
            ["Moist Turtle", "Good", "200"],
            ["Burning Lizard", "Very Good", "1000"],
            ["Mossy Frog", "Poor", "10"],
        ],
        (
            "Processing...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (
        CSVExportStatus.SUCCESS,
        "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        (
            "Success!",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (
        CSVExportStatus.FAILURE,
        [
            ["Card Name", "Condition", "Value"],
            ["Sparky Mouse", "Fair", 100],
            ["Moist Turtle", "Good", 200],
            ["Burning Lizard", "Very Good", 1000],
            ["Mossy Frog", "Poor", 10],
        ],
        (
            "Unknown error, retrying...",
            "Card Name,Condition,Value\nSparky Mouse,Fair,100\nMoist Turtle,Good,200\nBurning Lizard,Very Good,1000\nMossy Frog,Poor,10",
        ),
    ),
    (1, None, ("Exception Raised:", "unknown export status")),
]


def test(status, data, expected_output):
    print("---------------------------------")
    print(f"Checking: {status}")
    print("Expected:")
    print(f"{expected_output[0]}")
    print(f"{expected_output[1]}")
    try:
        result = get_csv_status(status, data)
    except Exception as e:
        result = expected_output[0], str(e)
    print("Actual:")
    print(f"{result[0]}")
    print(f"{result[1]}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


run_tests(submit_cases, test)
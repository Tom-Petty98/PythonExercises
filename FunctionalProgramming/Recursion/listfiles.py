from runtest import run_tests

def list_files(parent_directory, current_filepath=""):
    file_paths = []

    for item in parent_directory:
        path = current_filepath + "/" + item
        if parent_directory[item] == None:
            file_paths.append(path)
        else:
            file_paths.extend(list_files(parent_directory[item], path))

    return file_paths


run_cases = [
    (
        {
            "Documents": {
                "Proposal.docx": None,
                "Report": {"AnnualReport.pdf": None, "Financials.xlsx": None},
            },
            "Downloads": {"picture1.jpg": None, "picture2.jpg": None},
        },
        [
            "/Documents/Proposal.docx",
            "/Documents/Report/AnnualReport.pdf",
            "/Documents/Report/Financials.xlsx",
            "/Downloads/picture1.jpg",
            "/Downloads/picture2.jpg",
        ],
    )
]

submit_cases = run_cases + [
    ({}, []),
    (
        {
            "Work": {
                "ProjectA": {
                    "Documentation": {"README.md": None, "GUIDE.md": None},
                    "Source": {"main.py": None, "util.py": None},
                },
                "ProjectB": {"Presentation.pptx": None},
            }
        },
        [
            "/Work/ProjectA/Documentation/GUIDE.md",
            "/Work/ProjectA/Documentation/README.md",
            "/Work/ProjectA/Source/main.py",
            "/Work/ProjectA/Source/util.py",
            "/Work/ProjectB/Presentation.pptx",
        ],
    ),
    (
        {
            "Music": {
                "Pop": {"song1.mp3": None},
                "Classical": {"Beethoven": {"symphony9.mp3": None}},
            }
        },
        ["/Music/Classical/Beethoven/symphony9.mp3", "/Music/Pop/song1.mp3"],
    ),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    print(f"Expecting:")
    for output in expected_output:
        print(f"    {output}")
    try:
        result = sorted(list_files(input1))
        print(f"Actual:")
        for res in result:
            print(f"    {res}")
    except Exception as e:
        result = e
        print(f"Error: {e}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False




run_tests(submit_cases, test)
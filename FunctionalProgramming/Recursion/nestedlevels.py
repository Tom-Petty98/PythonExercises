from runtest import run_tests
#failed attempt.
# def count_nested_levels(nested_documents, target_document_id, level=1):

#     for document_id in nested_documents:
#         if document_id == target_document_id:
#             return level
#         else:
#             count_nested_levels(nested_documents[document_id], target_document_id, level + 1)

#     return -1

#answer
def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        if document_id == target_document_id:
            return level
        found_level = count_nested_levels(
            nested_documents[document_id], target_document_id, level + 1
        )
        if found_level != -1:
            return found_level
        
    return -1


run_cases = [
    #({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 2, 2),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 9, 4),
]

submit_cases = run_cases + [
    #({}, 1, -1),
    ({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 5, 4),
    #({1: {2: {3: {}, 4: {5: {}}}, 6: {}, 7: {8: {9: {10: {}}}}}}, 20, -1),
]


def test(input1, input2, expected_output):
    print("---------------------------------")
    print(f"Input tree: {input1}")
    print(f"Input document id: {input2}")
    print(f"Expecting: {expected_output}")
    result = count_nested_levels(input1, input2)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


run_tests(submit_cases, test)
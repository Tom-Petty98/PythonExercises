class HashMap:
    def insert(self, key, value):
        self.resize()       
        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    def resize(self):
        if len(self.hashmap) == 0:
            self.hashmap = [None]
            return
        if self.current_load() < 0.05:
            return
   
        # Rehash all existing elements
        old_hashmap = self.hashmap
        self.hashmap = [None] * (len(old_hashmap) * 10)

        for kvp in old_hashmap:
            if kvp is not None:
                index = self.key_to_index(kvp[0])
                self.hashmap[index] = (kvp[0], kvp[1])
            

    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        # filled_slots = 0
        # for slot in self.hashmap:
        #     if slot is not None:
        #         filled_slots += 1
        filled_slots = sum(1 for entry in self.hashmap if entry is not None)
        return filled_slots / len(self.hashmap)

    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
    

from runtest import run_tests

run_cases = [
    (
        [
            ("Billy Beane", 1),
            ("Peter Brand", 2),
            ("Art Howe", 3),
            ("Scott Hatteberg", 4),
            ("David Justice", 5),
            ("Ron Washington", 6),
            ("Paul DePodesta", 7),
        ],
        [
            (1.0, 1),
            (0.2, 10),
            (0.03, 100),
            (0.04, 100),
            (0.05, 100),
            (0.006, 1000),
            (0.007, 1000),
        ],
    )
]

submit_cases = run_cases + [
    (
        [
            ("Billy Beane", 1),
            ("Peter Brand", 2),
            ("Art Howe", 3),
            ("Scott Hatteberg", 4),
            ("David Justice", 5),
            ("Ron Washington", 6),
            ("Paul DePodesta", 7),
            ("Chad Bradford", 8),
        ],
        [
            (1.0, 1),
            (0.2, 10),
            (0.03, 100),
            (0.04, 100),
            (0.05, 100),
            (0.006, 1000),
            (0.007, 1000),
            (0.008, 1000),
        ],
    )
]



def test(items, expected_outputs):
    hm = HashMap(0)
    print("=====================================")
    actual = []
    for i, item in enumerate(items):
        key = item[0]
        val = item[1]
        expected_load = expected_outputs[i][0]
        expected_size = expected_outputs[i][1]
        print(f"insert({key}, {val})")
        try:
            hm.insert(key, val)
            print(f"Expect Load: {expected_load}")
            print(f"Actual Load: {hm.current_load()}")
            print(f"Expect Size: {expected_size}")
            print(f"Actual Size: {len(hm.hashmap)}")
            print("---------------------------------")
            actual.append((hm.current_load(), len(hm.hashmap)))
        except Exception as e:
            print(f"Error: {e}")
            print("Fail")
    print("=====================================")
    if actual == expected_outputs:
        print("Pass")
        return True
    print("Fail")
    return False

run_tests(submit_cases, test)
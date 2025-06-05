# graph = [[True] * 5] * 5

# graph[1][4] = False
# graph[4][1] = False

# print(graph)

# graph2 = [[True] * 5 for _ in range(5)]

# graph2[1][4] = False
# graph2[4][1] = False

# print(graph2)


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set([v])
        else:
            self.graph[u].add(v)

        if v not in self.graph:
            self.graph[v] = set([u])
        else:
            self.graph[v].add(u)

        
    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False
    

from runtest import run_tests

run_cases = [
    (
        [
            (0, 1),
            (2, 0),
        ],
        (
            [
                (1, 0),
                (1, 2),
                (2, 0),
            ],
            [True, False, True],
        ),
    ),
    (
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ],
        (
            [
                (0, 1),
                (1, 2),
                (0, 4),
                (2, 5),
                (5, 0),
            ],
            [True, True, False, False, False],
        ),
    ),
]
submit_cases = run_cases + [
    (
        [
            (0, 1),
            (2, 4),
            (2, 1),
            (3, 1),
            (4, 5),
        ],
        (
            [
                (5, 4),
                (1, 5),
                (0, 4),
                (2, 5),
                (1, 3),
            ],
            [True, False, False, False, True],
        ),
    ),
]


def test(edges_to_add, edges_to_check):
    print("=================================")
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("---------------------------------")
    try:
        actual = []
        for i, edge in enumerate(edges_to_check[0]):
            exists = graph.edge_exists(edge[0], edge[1])
            actual.append(exists)
            print(f"{edge} exists:")
            print(f" - Expecting: {edges_to_check[1][i]}")
            print(f" - Actual: {exists}")
        if actual == edges_to_check[1]:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False
    
run_tests(submit_cases, test)
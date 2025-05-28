from RBTree import *
from user import *

def test(num_users):
    users = get_users(num_users)
    tree = RBTree()
    for user in users:
        tree.insert(user)

    print_tree(tree)



def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    print("\n".join(lines))


def format_tree_string(node, lines, level=0):
    if node.val is not None:
        format_tree_string(node.right, lines, level + 1)
        lines.append(
            " " * 4 * level
            + "> "
            + str(node.val)
            + " "
            + ("[red]" if node.red else "[black]")
        )
        format_tree_string(node.left, lines, level + 1)

test(10)
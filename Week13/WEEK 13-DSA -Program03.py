class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def height(root):
    """Recursively calculates tree height (0 for empty tree, 1 for single node)."""
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


def count_unique_nodes(root):
    """Recursively counts all unique nodes in the tree."""
    if root is None:
        return 0
    return 1 + count_unique_nodes(root.left) + count_unique_nod1es(root.right)


def count_leaf_nodes(root):
    """Recursively counts leaf nodes (nodes with no left or right child)."""
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


def preorder(root):
    return [] if root is None else [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    return [] if root is None else inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    return [] if root is None else postorder(root.left) + postorder(root.right) + [root.value]


def read_values():
    """Validates user input, limits to 100 items, and prompts retry on error."""
    while True:
        raw_input = input("Enter space-separated integers (or press Enter for empty tree): ").strip()
        if not raw_input:
            return []
        tokens = raw_input.split()
        if len(tokens) > 100:
            print("Error: Input limit is 100 numbers. Please enter fewer numbers.\n")
            continue
        try:
            return [int(t) for t in tokens]
        except ValueError:
            print("Invalid input detected! Please enter valid integers only.\n")


if __name__ == "__main__":
    values = read_values()
    root = None
    for v in values:
        root = insert(root, v)

    print("\n--- Tree Analysis Results ---")
    print("Preorder Traversal  :", preorder(root))
    print("Inorder Traversal   :", inorder(root))
    print("Postorder Traversal :", postorder(root))
    print("Unique Node Count   :", count_unique_nodes(root))
    print("Leaf Node Count     :", count_leaf_nodes(root))
    print("Tree Height         :", height(root))
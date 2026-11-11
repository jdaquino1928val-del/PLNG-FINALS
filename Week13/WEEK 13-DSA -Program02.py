class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Recursively inserts unique values into the BST."""
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    # Equal values are ignored (duplicates omitted)
    return root


def build_bst(values):
    """Builds a BST from an input sequence of values."""
    root = None
    for val in values:
        root = insert(root, val)
    return root


def preorder(root):
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


def read_user_input():
    while True:
        raw_input = input("Enter integer elements for BST separated by space: ").strip()
        if not raw_input:
            return []
        try:
            return [int(x) for x in raw_input.split()]
        except ValueError:
            print("Invalid sequence! Enter numbers only.\n")


if __name__ == "__main__":
    user_values = read_user_input()
    print("\nOriginal Insertion Order:", user_values)
    
    tree_root = build_bst(user_values)

    print("Preorder Traversal  :", preorder(tree_root))
    print("Inorder Traversal   :", inorder(tree_root))
    print("Postorder Traversal :", postorder(tree_root))
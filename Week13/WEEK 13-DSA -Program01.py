class Node:
    """Class representing a single node in a binary tree."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Recursively inserts a value into the binary tree."""
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root


def preorder(root):
    """Preorder traversal: Root -> Left -> Right."""
    if root is None:
        return []
    return [root.value] + preorder(root.left) + preorder(root.right)


def inorder(root):
    """Inorder traversal: Left -> Root -> Right."""
    if root is None:
        return []
    return inorder(root.left) + [root.value] + inorder(root.right)


def postorder(root):
    """Postorder traversal: Left -> Right -> Root."""
    if root is None:
        return []
    return postorder(root.left) + postorder(root.right) + [root.value]


def get_user_elements():
    """Prompts user to enter space-separated integers with input validation."""
    while True:
        raw = input("Enter elements separated by spaces (e.g., 10 5 15 2 7 12 20): ").strip()
        if not raw:
            return []
        try:
            return [int(x) for x in raw.split()]
        except ValueError:
            print("Invalid input! Please enter valid integers only.\n")


if __name__ == "__main__":
    elements = get_user_elements()
    
    root = None
    for val in elements:
        root = insert(root, val)

    print("\n--- Traversal Results ---")
    print("Preorder Traversal  :", preorder(root))
    print("Inorder Traversal   :", inorder(root))
    print("Postorder Traversal :", postorder(root))
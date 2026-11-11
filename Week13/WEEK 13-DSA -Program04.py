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


def search(root, key):
    """Recursively searches for key in the BST."""
    if root is None or root.value == key:
        return root
    if key < root.value:
        return search(root.left, key)
    return search(root.right, key)


def subtree_count(root):
    """Recursively counts nodes in a subtree."""
    if root is None:
        return 0
    return 1 + subtree_count(root.left) + subtree_count(root.right)


def subtree_sum(root):
    """Recursively sums all node values in a subtree."""
    if root is None:
        return 0
    return root.value + subtree_sum(root.left) + subtree_sum(root.right)


def inorder(root):
    return [] if root is None else inorder(root.left) + [root.value] + inorder(root.right)


def preorder(root):
    return [] if root is None else [root.value] + preorder(root.left) + preorder(root.right)


def postorder(root):
    return [] if root is None else postorder(root.left) + postorder(root.right) + [root.value]


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Invalid input! Please enter a single integer.")


if __name__ == "__main__":
    raw = input("Enter space-separated integers to build tree: ").strip()
    values = [int(x) for x in raw.split()] if raw else []
    
    root = None
    for v in values:
        root = insert(root, v)

    print("\nFull Tree Inorder Traversal:", inorder(root))
    
    search_key = get_integer_input("Enter search key: ")
    target_node = search(root, search_key)

    if target_node:
        print(f"\n--- Subtree Analysis for Key ({search_key}) ---")
        print("Subtree Preorder  :", preorder(target_node))
        print("Subtree Inorder   :", inorder(target_node))
        print("Subtree Postorder :", postorder(target_node))
        print("Subtree Node Count:", subtree_count(target_node))
        print("Subtree Sum       :", subtree_sum(target_node))
    else:
        print("Value not found")
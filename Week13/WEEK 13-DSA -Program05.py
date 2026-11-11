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


def mirror_copy(root):
    """Recursively creates a new mirrored tree with left and right children swapped."""
    if root is None:
        return None
    new_node = Node(root.value)
    new_node.left = mirror_copy(root.right)
    new_node.right = mirror_copy(root.left)
    return new_node


def inorder(root):
    return [] if root is None else inorder(root.left) + [root.value] + inorder(root.right)


def preorder(root):
    return [] if root is None else [root.value] + preorder(root.left) + preorder(root.right)


def postorder(root):
    return [] if root is None else postorder(root.left) + postorder(root.right) + [root.value]


if __name__ == "__main__":
    raw_input = input("Enter space-separated integers for tree: ").strip()
    data = [int(x) for x in raw_input.split()] if raw_input else []
    
    original_root = None
    for item in data:
        original_root = insert(original_root, item)

    mirrored_root = mirror_copy(original_root)

    orig_inorder = inorder(original_root)
    mirrored_inorder = inorder(mirrored_root)

    print("\n--- Traversal Comparisons ---")
    print("Original Preorder  :", preorder(original_root))
    print("Original Inorder   :", orig_inorder)
    print("Original Postorder :", postorder(original_root))
    print("-" * 35)
    print("Mirrored Preorder  :", preorder(mirrored_root))
    print("Mirrored Inorder   :", mirrored_inorder)
    print("Mirrored Postorder :", postorder(mirrored_root))
    print("-" * 35)
    print("Is Mirrored Inorder equal to Reversed Original Inorder?", 
          mirrored_inorder == list(reversed(orig_inorder)))
    print("Are Roots Independent Objects?", original_root is not mirrored_root)
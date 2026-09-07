"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    if root:
        # Traverse the left subtree
        inOrder(root.left)
        # Print the current node's value followed by a space
        print(root.info, end=" ")
        # Traverse the right subtree
        inOrder(root.right)

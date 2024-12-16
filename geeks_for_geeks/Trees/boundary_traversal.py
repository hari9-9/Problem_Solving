class Solution:
    def leftT(self, root, left):
        if not root:
            return
        # Add only if it's not a leaf
        if root.left or root.right:
            left.append(root.data)
        # Traverse left child first, if it exists, otherwise traverse the right child
        if root.left:
            self.leftT(root.left, left)
        elif root.right:
            self.leftT(root.right, left)

    def leafT(self, root, leaf):
        if not root:
            return
        # Add to leaf if it's a leaf node
        if not root.left and not root.right:
            leaf.append(root.data)
            return
        # Recurse on both subtrees
        self.leafT(root.left, leaf)
        self.leafT(root.right, leaf)

    def rightT(self, root, right):
        if not root:
            return
        # Traverse right child first, if it exists, otherwise traverse the left child
        if root.right:
            self.rightT(root.right, right)
        elif root.left:
            self.rightT(root.left, right)
        # Add only if it's not a leaf
        if root.left or root.right:
            right.append(root.data)

    def boundaryTraversal(self, root):
        if not root:
            return []

        left = []
        leaf = []
        right = []

        # Add the root node (only if it's not a leaf)
        if root.left or root.right:
            result = [root.data]
        else:
            result = [root.data]

        # Handle left boundary
        if root.left:
            self.leftT(root.left, left)

        # Handle leaf nodes
        self.leafT(root, leaf)

        # Handle right boundary
        if root.right:
            self.rightT(root.right, right)

        # Combine the results
        result += left + leaf + right[::-1]
        return result

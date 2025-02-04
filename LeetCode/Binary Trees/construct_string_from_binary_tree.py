class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        ans = []
        self.preorder_traversal(root, ans)
        return "".join(ans)

    def preorder_traversal(self, node: Optional[TreeNode], ans: List[str]):
        if not node:
            return

        ans.append(str(node.val))
        if node.left or node.right:
            ans.append("(")
            self.preorder_traversal(node.left, ans)
            ans.append(")")
        if node.right:
            ans.append("(")
            self.preorder_traversal(node.right, ans)
            ans.append(")")

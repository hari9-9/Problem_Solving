'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def solve(self, root, curr_sum, curr_len, result):
        if not root:
            return

        # Update the current path sum and length
        curr_sum += root.data

        # If it's a leaf node, check the path conditions
        if not root.left and not root.right:
            if curr_len > result[0]:  # If the current path is longer
                result[0] = curr_len
                result[1] = curr_sum
            elif curr_len == result[0]:  # If the path length is the same, maximize the sum
                result[1] = max(result[1], curr_sum)
            return

        # Recur for left and right subtrees
        self.solve(root.left, curr_sum, curr_len + 1, result)
        self.solve(root.right, curr_sum, curr_len + 1, result)

    def sumOfLongRootToLeafPath(self, root):
        if not root:
            return 0

        # result[0] stores max_len, result[1] stores max_sum
        result = [0, float('-inf')]  # Initialize max_len and max_sum
        self.solve(root, 0, 0, result)
        return result[1]
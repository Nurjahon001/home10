class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def dfs(node, depth):
            if not node.left and not node.right:
                return depth
            left_depth = float('inf')
            right_depth = float('inf')
            if node.left:
                left_depth = dfs(node.left, depth + 1)
            if node.right:
                right_depth = dfs(node.right, depth + 1)
            return min(left_depth, right_depth)

        return dfs(root, 1)
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

solution = Solution()
print(solution.minDepth(root1))
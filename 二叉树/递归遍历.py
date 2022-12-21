class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 前序遍历-递归-LC144_二叉树的前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 保存结果
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            result.append(root.val)  # 前序
            traversal(root.left)  # 左
            traversal(root.right)  # 右

        traversal(root)
        return result


# 中序遍历-递归-LC94_二叉树的中序遍历
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)  # 左
            result.append(root.val)  # 中序
            traversal(root.right)  # 右

        traversal(root)
        return result


# 后序遍历-递归-LC145_二叉树的后序遍历
class Solution2:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)  # 左
            traversal(root.right)  # 右
            result.append(root.val)  # 后序

        traversal(root)
        return result
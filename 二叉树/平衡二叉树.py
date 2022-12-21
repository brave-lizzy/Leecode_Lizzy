#   题目：给定一个二叉树，判断是否是高度平衡的二叉树
#   definition：一个二叉树每个结点的左右子树高度差的绝对值不超过1

#   递归法
class solution:
    def isBalanced(self,root):
        if self.get_height(root) != -1:
            return True
        else:
            return False

    def get_height(self, root):
        if not root:
            return 0
        if (left_height := self.get_height(root.left)) == -1:
            return -1
        if (right_height := self.get_height(root.right)) == -1:
            return -1
        if abs(left_height-right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)

# 迭代法
class solution1:
    def isBalanced(self, root):
        if not root:
            return 0
        height = {}
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(None)
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            else:
                real_node = stack.pop()
                left, right = height.get(real_node.left, 0),height.get(real_node.right)
                if abs(left - right) > 1:
                    return False
                height[real_node] = 1+ max(left, right)
            return True

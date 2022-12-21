from collections import deque
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node .left:
                stack.append(node.left)
        return result
    # 前序遍历思想：中左右；先添加根节点,然后将右节点和左节点先后入栈里面；

    def Middle(self, root):
        if not root: return []
        stack = []
        result = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result

    def hou(self, root):
        if not root: return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]

    def cengxu(self, root):
        if not root:return[]
        que = deque([root])
        result=[]
        while deque:
            cur = que.popleft()
            result.append(cur.val)
            if cur.left:
                result.append(cur.left)
            if cur.right:
                result.append(cur.right)


        
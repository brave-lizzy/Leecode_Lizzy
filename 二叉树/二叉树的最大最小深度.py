# 最大深度
# 递归法
class solution:
    def maxdepth(self, root):
        return self.getdepth(root)

    def getdepth(self, node):
        if not node:return 0
        leftdepth = self.getdepth(node.left)
        rightdepth = self.getdepth(node.right)
        depth = max(leftdepth, rightdepth)+1
        return depth

#精简版递归法
class solution1:
    def maxdepth(self, root):
        return 1+max(self.maxdepth(root.left), self.maxdepth(root.right))

#迭代法
import collections
class solution2:
    def maxdepth(self, root):
        if not root:return 0
        depth = 0
        queue = collections.deque()
        queue.append(root)
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
s = solution2()
s.maxdepth(root=[1,2,3,4,5,None,None,None,None])

#最小深度
# 只有当左右孩子都为空的时候，才说明遍历的最低点了。如果其中一个孩子为空则不是最低点

#   递归法（DFS，深度优先搜索）
class solution3():
    def mindepth(self,root):
        if not root:return 0
        if not root.left and not root.right:return 1
        leftdepth = self.mindepth(root.left)
        rightdepth = self.mindepth(root.right)
        depth = min(leftdepth,rightdepth)+1
        return depth

#   层序遍历(BFS,广度优先搜索）
class solution4():
    def mindepth(self,root):
        if not root:return 0
        que = collections.deque([root])
        depth = 1
        while que:
            n = len(que)
            depth += 1
            for _ in range(n):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                if not cur.left and not cur.right:
                    return depth
'''
  不理解的地方：为什么que传入root之后里面只有头结点的值，即len(que)在二叉树中
  只是1或2,在一次for循环之后输出一层的值。
  例如：输入[12,5,15,null,null,14,16]
       输出[[12],[5,15],[14,16]]
'''

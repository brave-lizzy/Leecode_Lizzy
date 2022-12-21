#与最大深度最小深度类似代码
import collections
'''
完全二叉树的重要特征:
有n个结点的完全二叉树，层数(深度)为log2(n+1)
如何找双亲结点，左孩子结点，右孩子结点?
（1）当前结点编号为m，双亲节点为m/2;
（2）当前结点编号为m，如果有左孩子结点，编号就为2m;
（3）当前结点编号为m，如果有右孩子结点，编号就位2m+1;
'''
#   递归法
class solution:
    def getNodesNum(self, root):
        if not root:return 0
        left = self.getNodesNum(root.left)
        right = self.getNodesNum(root.right)
        nums = left+right+1
        return nums
#   迭代法
class Solurion1:
    def getNodeNum(self,root):
        queue = collections.deque()
        if root:
            queue.append((root))
        result = 0
        while queue:
            size = len(queue)

            for _ in range(size):
                cur = queue.popleft()
                result += 1
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return result

#   利用完全二叉树的性质求节点数
class Solution2:
    def getNodeNum(self,root):
        if not root:return 0
        left = root.left
        right = root.right
        leftDepth = 0
        rightDepth = 0
        while left:
            left = left.left
            leftDepth += 1
        while right:
            right = right.right
            rightDepth += 1
        if leftDepth == rightDepth:
            return 2**leftDepth-1
        return self.getNodeNum(root.left)+self.getNodeNum(root.right)+1

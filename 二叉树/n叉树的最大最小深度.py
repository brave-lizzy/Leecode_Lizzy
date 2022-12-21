#n叉树的最大深度、递归法
class solution:
    def maxdepth(self, root):
        if not root:return 0
        depth=0
        for i in range(len(root.children)):
            depth = 1+max(depth,self.maxdepth(root.children[i]))
        return depth

# 迭代法/层序遍历
import collections
class solution1:
    def maxdepth(self,root):
        queue = collections.deque()
        if not root:return 0
        queue.append((root))
        depth = 0
        while queue:
            size = len(queue)
            depth+=1
            for _ in range(size):
                node = queue.popleft()
                for j in range(len(node.chileren)):
                    if node.chileren[j]:
                        queue.append(node.children[j])
        return depth

# 栈模拟后序遍历
class solution2:
    def maxdepth(self,root):
        st = []
        if root:
            st.append(root)
        depth = 0
        result = 0
        while st:
            node = st.pop()
            if node != None:
                st.append(node)
                st.append(None)
                depth += 1
                for i in range(len(node.children)):
                    if node.children[i]:
                        st.append(node.children[i])
            else:
                node =
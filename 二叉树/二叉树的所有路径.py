#   题目：所有根节点到子节点的路径数目和每条路径的内容

#   递归法
class num_path():
    def getpath(self, root):
        if not root: return 0
        num = 0
        self.getpath(root.left)
        num += 1
        self.getpath(root.right)
        return num

#   迭代法
class num_path2():
    def getpath2(self, root):
        stack = [root]
        num = 0
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append()
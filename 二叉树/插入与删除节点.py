class Solution:
    def deleteNode(selfself, root, key):
        if not root:return root
        p = root
        last = None
        while p:
            if p.val==key:
                if p.right:
                    if p.left:
                        node = p.right
                        while node.left:
                            node = node.left
                        node.left = p.left
                    right = p.right
                else:
                    
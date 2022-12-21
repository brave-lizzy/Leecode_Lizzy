class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        path = []
        def backtracking(n, k, startidx):
            if len(path) == k:
                result.append(path[:])
                return

            # 剪枝， 最后k - len(path)个节点直接构造结果，无需递归
            last_startidx = n - (k - len(path)) + 1
            result.append(path + [idx for idx in range(last_startidx, n + 1)])

            for x in range(startidx, last_startidx):
                path.append(x)
                backtracking(n, k, x + 1)  # 递归
                path.pop()  # 回溯

        backtracking(n, k, 1)
        return result

class Solution1:
    def combine(self, n: int, k: int):
        res=[]  #存放符合条件结果的集合
        path=[]  #用来存放符合条件结果
        def backtrack(n,k,startIndex):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(startIndex,n-(k-len(path))+2):  #优化的地方
                path.append(i)  #处理节点
                backtrack(n,k,i+1)  #递归
                path.pop()  #回溯，撤销处理的节点
        backtrack(n,k,1)
        return res

solution = Solution1()
solution.combine(4,2)

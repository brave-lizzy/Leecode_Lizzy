#简易爬楼梯，一次只能爬1or2台阶
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            tmp=dp[0]+dp[1]
            dp[0]=dp[1]
            dp[1]=tmp
        return dp[1]
# S = Solution()
# value = S.climbStairs(4)
# print(value)


#爬楼梯每一层需要不同的代价
class Solution2:
    def minCostClimbingStairs(self, cost) -> int:
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return min(dp[len(cost) - 1], dp[len(cost) - 2])

So = Solution2()
value = So.minCostClimbingStairs([1, 100, 1, 1, 1,100])
print(value)
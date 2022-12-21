# 209 双指针法求长度最小的子数组
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ans = n + 1
        pre = 0
        j = 0
        for i in range(n):
            while j < n and pre < target:
                pre += nums[j]
                j += 1
            if pre >= target and j - i < ans:
                ans = j - i
            pre -= nums[i]
        return ans if ans < n + 1 else 0
Solution = Solution()
min = Solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(min)


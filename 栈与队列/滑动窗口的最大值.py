class Solution:
    def Maxsolidwindows(self, nums, k):
        if not nums: return []
        res, window = [], []
        for i , item in enumerate(nums):
            if i >= k and window[0] <= i-k:
                window.pop(0)
            while window and nums[window[-1]] < item:
                window.pop()
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])
        return res
# -*- coding: utf-8 -*-
"""
@Time    : 2022/8/10 21:49
@Author  : FJC
@File    : 2-移除链表元素-自测.py
@Software: win10  python3.7
"""
class ListNode:
    def __init__(self, val=None,next=None):
        self.val=val
        self.next = next

# 无虚拟节点
class Solution:
    def removeElements(self, head: ListNode, val):
        if head == None:
            return head
        pre = None
        cur = head  # 将游标指向head
        while cur != None:  
            if cur.val == val:  # 第一次是判断头节点cur.val是否为val，后面则判断cur.next.val是否为val
                if pre == None:
                    head = head.next
                else:
                    pre.next = cur.next
            else:
                pre = cur
            cur = cur.next
        return head

# solution=Solution()
# print(solution.removeElements(head = ListNode([1,2,6,3,4,5,6]), val = 6))
class Solution1:
    def isValid(self, s: str) -> bool:
        stack = []

        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()

        return True if not stack else False


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        return True if not stack else False

# solution = Solution2()
# solution.isValid("(){}[]")
class Solution3:
    def maxSlidingWindow(self, nums, k: int):
        if not nums:return
        window, tmp = [], []
        for i , item in enumerate(nums):
            if i >= k and window[0] <= i-k:
                window.pop(0)
            while window and nums[window[-1]] <= item:
                window.pop()
            window.append(i)
            if i >= k-1:
                tmp.append(nums[window[0]])
        return tmp
# solution = Solution3()
# solution.maxSlidingWindow([1,2,3,4,5],k=3)
import heapq


class Solution4:
    def topKFrequent(self, nums, k: int) :
        # 要统计元素出现频率
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫面所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result

solution = Solution4()
solution.topKFrequent([1,1,1,2,2,3], 3)
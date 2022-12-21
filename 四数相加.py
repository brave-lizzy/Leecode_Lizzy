#双指针法
class Solution:
    def fourSum(self, nums: [int], target: int) :

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]: continue
                p = k + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[k] + nums[p] + nums[q] > target:
                        q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target:
                        p += 1
                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        p += 1
                        q -= 1
        return res

# solution = Solution()
# res = solution.fourSum([1,1,1,-1,-6,-4, 5,3,9,4,-2], 10)


class Solution2:
    def reverseStr(self, s: str, k: int) -> str:
        """
        1. 使用range(start, end, step)来确定需要调换的初始位置
        2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
        3. 用切片整体替换，而不是一个个替换.
        """

        def reverse_substring(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text

        res = list(s)

        for cur in range(0, len(s), 2 * k):
            res[cur: cur + k] = reverse_substring(res[cur: cur + k])

        return ''.join(res)

class Solution3:
    def reverseStr(self, s: str, k: int) -> str:
        # Two pointers. Another is inside the loop.
        p = 0
        while p < len(s):
            p2 = p + k
            # Written in this could be more pythonic.
            s = s[:p] + s[p: p2][::-1] + s[p2:]
            p = p + 2 * k
        return s

class Solution4:
    def replaceSpace(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)):
            if s[i] == ' ':
                s[i] = "%20"
        return "".join(s)
# solution = Solution4()
# print(solution.replaceSpace("we are happy"))

class Solution5:
    # 1.去除多余的空格
    def trim_spaces(self, s):
        n = len(s)
        left = 0
        right = n - 1

        while left <= right and s[left] == ' ':  # 去除开头的空格
            left += 1
        while left <= right and s[right] == ' ':  # 去除结尾的空格
            right = right - 1
        tmp = []
        while left <= right:  # 去除单词中间多余的空格
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':  # 当前位置是空格，但是相邻的上一个位置不是空格，则该空格是合理的
                tmp.append(s[left])
            left += 1
        return tmp

    # 2.翻转字符数组
    def reverse_string(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None

    # 3.翻转每个单词
    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n:
            while end < n and nums[end] != ' ':
                end += 1
            self.reverse_string(nums, start, end - 1)
            start = end + 1
            end += 1
        return None

    # 4.翻转字符串里的单词
    def reverseWords(self, s):  # 测试用例："the sky is blue"
        l = self.trim_spaces(s)  # 输出：['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e'
        self.reverse_string(l, 0,
                            len(l) - 1)  # 输出：['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']
        self.reverse_each_word(l)  # 输出：['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
        return print(''.join(l))  # 输出：blue is sky the


# solution = Solution5()
# tmp = solution.reverseWords(" we are family ")


class Solution6:
    def reverseWords(self, s) :
        s = s.split(' ')
        s = s[::-1]
        s = " ".join(s)
        p , q = 0, len(s)-1
        while p<q and s[p] == " ":
            p += 1
        while p<q and s[q] == " ":
            q -= 1
        s = s[p:q+1]
        p, q = 0, len(s) - 1
        tmp = []
        while p<=q:
            if s[p] != " ":
                tmp.append(s[p])
            elif tmp[-1] != " ":
                tmp.append(s[p])
            p += 1
        return "".join(tmp)

# solution = Solution6()
# print(solution.reverseWords(" we   are family "))
# s="ancdfe"
# print(s[1:])
# // 方法一
class Solution7:
    def strStr(self, haystack: str, needle: str) -> int:
        a=len(needle)
        b=len(haystack)
        if a==0:
            return 0
        next=self.getnext(a,needle)
        p=-1
        for j in range(b):
            while p>=0 and needle[p+1]!=haystack[j]:
                p=next[p]
            if needle[p+1]==haystack[j]:
                p+=1
            if p==a-1:
                return j-a+1
        return -1

    def getnext(self,a,needle):
        next=['' for i in range(a)]
        k=-1
        next[0]=k
        for i in range(1,len(needle)):
            while (k>-1 and needle[k+1]!=needle[i]):
                k=next[k]
            if needle[k+1]==needle[i]:
                k+=1
            next[i]=k
        return next
# solution = Solution7()
# solution.strStr(haystack="aabbccdfaabbccg", needle="aabbccg")

class Solution8(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 快慢指针
        fast = slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow

# solution=Solution8()
# print(solution.removeElement([3,2,2,3],3))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution9:
    def reverseList(self, head: ListNode):
        cur = head
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        return pre
# solution=Solution9()
# solution.reverseList([1,2,3,4,5])

class Solution10:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        if nxt[-1] != -1 and len(s) % (len(s) - (nxt[-1] + 1)) == 0:
            return True
        return False

    def getNext(self, nxt, s):
        nxt[0] = -1
        j = -1
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j + 1]:
                j = nxt[j]
            if s[i] == s[j + 1]:
                j += 1
            nxt[i] = j
        return nxt
solution = Solution10()
print(solution.repeatedSubstringPattern("ababab"))
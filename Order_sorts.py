#冒泡排序， 复杂度O(n*n)
def bubble_sort(list):
    for i in range(len(list)-1):
        exchange = False
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                exchange = True
        if not exchange:
            return
# list = [9,2,3,4,1,3,9,6,5,7]
# bubble_sort(list)
# print(list)

# 选择排序 复杂度O(n）
def select_sort(list):
    new_list = []
    for i in range(len(list)):
        min_value = min(list)
        new_list.append(min_value)
        list.remove(min_value)
    return new_list

# new_list = select_sort(list)
# print(new_list)



#插入排序 时间复杂度O(n^2)/空间复杂度O(1)
def insert_sort(list):
    for i in range(1, len(list)): #i为摸到的麻将的下标
        tmp = list[i]
        j = i - 1 # 当前手里的牌下标最大的
        while list[j] > tmp and j >= 0:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = tmp
        print(list)

# List = [8, 6, 4, 9, 5, 7, 0]
# insert_sort(List)
# print(List)


from cal_time import *
# 快速排序
def _quick_sort(list, left, right):
    if left < right:
        middle = partition_sort(list, left, right)
        _quick_sort(list, left,middle-1)
        _quick_sort(list, middle+1,right)

@cal_time
def quick_sort(li):
    _quick_sort(li, 0, len(li)-1)

def partition_sort(list, left, right):
    tmp = list[left]
    while left <  right:
        while left < right and list[right] >= tmp:
            right -= 1
        list[left] = list[right]
        # print(list)
        while left < right and list[left] <= tmp:
            left += 1
        list[right] = list[left]
        # print(list)
    list[left] = tmp
    return left

List = [8 ,4, 3, 6, 9, 2, 1, 0]
partition_sort(List, 0, len(List)-1)
print(List)



# 汉诺塔问题
def hanoi(n, a, b, c):

    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from %s to %s" % (a, c))
        hanoi(n-1, b, a, c)
# hanoi(64,'A', 'B', 'C')


#顺序查找，时间复杂度O(n）
def linear_search(li, val):
    for index, v in enumerate(li):
        if v == val:
            return index
        else:
            return None


#二分查找，时间复杂度O(nlogn)
def binary_searcha(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if middle > target:
            right = middle - 1
        elif middle < target:
            left = middle + 1
        else:
            return middle
    else:
        return None


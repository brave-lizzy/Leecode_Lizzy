#单链表基本操作

class Node(object):
    '''节点'''
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList(object):
    '''单链表'''

    def __init__(self, node = None): #设置默认参数
        '''头节点，设置成私有'''
        self.__head = node

    def is_empty(self):
        '''链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        # cur游标，用来移动遍历节点
        cur = self.__head
        #count记录数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历整个链表'''
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ") #换行方式。默认python为换行，加上end=" "在python3默认为空格换行。python2默认为,隔开
            cur = cur.next

    def add(self, item):
        '''链表头部添加元素，头插法 时间复杂度O(1)'''
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''链表尾部添加元素，尾插法 时间复杂度O(n)'''
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        '''指定位置添加元素 时间复杂度O(n)，顺序表为O(n) '''
        #:param pos 从0开始
        if pos < 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                pre = pre.next
                count += 1
            #当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node


    def remove(self, item):
        '''删除节点'''
        pre = self.__head

        if pre.elem == item:
            self.__head = pre.next
        else:
            while pre.next != None:
                if pre.next.elem == item:
                    pre.next = pre.next.next
                else:
                    pre = pre.next

    def conatain(self, item):
        '''查找节点是否存在 时间复杂度O(n)'''
        cur = self.__head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False



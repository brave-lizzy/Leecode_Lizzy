class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.next = None


class HashMap(object):
    def __init__(self, table_size):
        self.items = [None] * table_size
        self.count = 0  # number of nodes in the map

    def __len__(self):
        return self.count

    def __str__(self):
        vals = []
        for item in self.items:
            temp_list = []
            while item is not None:
                temp_list.append(str(item.key))
                item = item.next
            vals.append("->".join(temp_list))
        return str(vals)

    def _hash(self, key) -> int:
        return abs(hash(key)) % len(self.items)


    def __getitem__(self, key):
        """
        查询数据
        """
        j = self._hash(key)
        node = self.items[j]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            raise KeyError('KeyError' + repr(key))
        return node

    def insert(self, key):
        """
        插入数据
        """
        try:
            self[key]
        except KeyError:
            j = self._hash(key)
            node = self.items[j]
            self.items[j] = ListNode(key)
            self.items[j].next = node
            self.count += 1

    def __delitem__(self, key):
        """
        删除数据
        """
        j = self._hash(key)
        node = self.items[j]
        if node is not None:
            if node.key == key:
                self.items[j] = node.next
                self.count -= 1
            else:
                while node.next != None:
                    pre = node
                    node = node.next
                    if node.key == key:
                        pre.next = node.next
                        self.count -= 1
                        break


if __name__ == "__main__":
    # 创建一个散列表
    hash_map = HashMap(3)
    # 插入数据
    hash_map.insert(100)
    hash_map.insert(200)
    hash_map.insert(300)
    hash_map.insert(400)
    hash_map.insert(500)
    hash_map.insert(600)
    hash_map.insert(700)
    hash_map.insert(800)
    print("内容为：", hash_map)
    print("当前数据量：", len(hash_map))
    # 查询数据
    print("搜索100是否存在：", hash_map[100].key)
    # 删除
    del hash_map[100]
    print("内容为：", hash_map)
    print("当前数据量：", len(hash_map))

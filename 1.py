class node:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = None
        self.prev = None

class nodelist:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev
        self.head = None
        self.size = 0

    def search(self, index):
        if index >= self.size or index < 0:
            return None
        i = 0
        tmp = self.head
        while i < index:
            tmp = tmp.next
            i = i + 1
        return tmp

    def insert(self, index, data):
        prev = self.search(index - 1)
        curr = self.search(index)
        if index < 0 or index > self.size:
            error = "error"
            print(error)
            return
        if index == 0:
            self.addfirst(data)
            return
        if index == self.size:
            self.addlast(data)
            return
        newnode = node(data, None, None)
        prev.next = newnode
        newnode.next = curr
        curr.prev = newnode
        self.size = self.size + 1

    def addfirst(self, data):
        newnode = node(data, None, None)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        self.size = self.size + 1

    def addlast(self, data):
        newnode = node(data, None, None)
        if self.head == None:
            self.head = newnode
        else:
            last = self.search(self.size - 1)
            last.next = newnode
            newnode.prev = last
        self.size = self.size + 1

    def deletesome(self, index):
        if index < 0 or index >= self.size:
            error = "error"
            print(error)
            return
        if index == 0:
            tmp = self.head
            self.head = tmp.next
            if self.head:
                self.head.prev = None
            self.size = self.size - 1
            return
        if index == self.size - 1:
            last = self.search(self.size - 1)
            lastprev = last.prev
            lastprev.next = None
            self.size = self.size - 1
            return
        lastone = self.search(index - 1)
        nextone = self.search(index + 1)
        lastone.next = nextone
        nextone.prev = lastone
        self.size = self.size - 1

    def display(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()

# 创建一个 nodelist 实例
nl = nodelist(None, None, None)

# 添加一些元素
nl.addfirst(10)
nl.addlast(20)
nl.addlast(30)
nl.insert(1, 15)

# 显示链表
print("链表内容:")
nl.display()

# 删除一些元素
nl.deletesome(1)
nl.deletesome(0)

# 显示链表
print("删除元素后的链表内容:")
nl.display()
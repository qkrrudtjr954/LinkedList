class LinkedList :

    class Node :
        def __init__(self, data) :
            self.data = data
            self.next = None

    def __init__(self) :
        self.head = None;
        self.tail = None;
        self.size = 0;

    def addFirst(self, data) :
        newNode = Node(data)

        # 빈리스트일 겅유
        if self.head == None :
            self.head = newNode
            self.tail = newNode
        # 빈리스트가 아닐 경우
        else :
            newNode.next = self.head
            self.head = newNode

        self.size += 1

    def addLast(self, data) :
        newNode = Node(data)

        # 빈리스트일 경우
        if self.head == None :
            self.addFirst(data)
        # 빈리스트가 아닐 경우
        else :
            self.tail.next = newNode
            self.tail = newNode
            self.size += 1

    def addNode(self, index, data) :

        if index <= 0 or self.size == 0 :
            self.addFirst(data)
        elif index >= self.size :
            self.addLast(data)
        else :
            newNode = Node(data)

            prev = self.__getNode(index-1)
            curr = self.__getNode(index)

            prev.next = newNode
            newNode.next = curr
            self.size += 1

    def removeFirst(self) :
        pass

    def removeLast(self) :
        pass

    def removeNode(self, index) :
        pass


    def get(self, index) :
        return None

    def show(self) :
        pass



    # private method
    def __getNode(self, index) :
        return None

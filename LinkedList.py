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
        newNode = self.Node(data)

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
        newNode = self.Node(data)

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
            newNode = self.Node(data)

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
        curr = self.head
        result = []

        while curr != None :
            data = curr.data
            result.append(data)
            curr = curr.next
        return result



    # private method
    def __getNode(self, index) :
        i = 0

        curr = this.head
        while i < index :
            curr = curr.next
            i+=1
            
        return curr

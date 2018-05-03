class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None


class LinkedList :
    def __init__(self) :
        self.head = None
        self.curr = None
        self.prev = None
        self.size = 0

    def add(self, index, data) :
        # 새로운 노드를 생성한다.
        newNode = Node(data)

        if self.head == None :
            # 리스트의 원소가 하나도 없을 때
            self.head = newNode
        elif index <= 0 :
            # 첫번째에 원소를 삽입할 때
            newNode.next = self.head
            self.head = newNode
        else :
            # 중간에 삽입하는 경우
            self.curr = self.head
            i = 0

            while i < index and self.curr != None :
                self.prev = self.curr
                self.curr = self.curr.next
                i += 1

            self.prev.next = newNode
            newNode.next = self.curr


    def remove(self, index) :
        removed = None
        if index <= 0 :
            # 가장 앞에 있는 원소 삭제
            removed = self.head
            self.head = self.head.next
        else :
            # 중간 and 가장 뒤에 있는 원소 삭제
            self.curr = self.head
            i = 0

            while i < index and self.curr.next != None :
                self.prev = self.curr
                self.curr = self.curr.next
                i += 1

            removed = self.curr
            self.prev.next = self.curr.next

        return removed.data

    def show(self) :
        self.curr = self.head
        result = []
        while self.curr != None :
            data = self.curr.data
            result.append(data)
            self.curr = self.curr.next
        return result

    def get(self, index) :
        pass

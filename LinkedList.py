class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList :

    def __init__(self) :
        print('LinkedList is created.')
        self.head = None
        self.curr = None
        self.prev = None
        self.size = 0

    def add(self, index, data) :
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
        pass

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


if __name__ == '__main__' :
    list = LinkedList()
    list.add(0, 'first')

import unittest
from LinkedList import LinkedList

def init_list() :
    list = LinkedList()
    list.addFirst('first1')
    list.addLast('first2')
    list.addLast('first3')
    list.addLast('first4')
    list.addLast('first5')

    return list


class RemoveFromLinkedListTest(unittest.TestCase) :
    def test_removeFromEmptyList(self) :
        list = LinkedList()
        self.assertEqual(list.removeFirst(), 'This List has any data.')
        self.assertEqual(list.removeNode(2), 'This List has any data.')

    def test_removeFirst(self) :
        list = init_list()
        self.assertEqual(list.removeFirst(), 'first1')
        self.assertEqual(list.removeFirst(), 'first2')
        self.assertEqual(list.removeFirst(), 'first3')
        self.assertEqual(list.removeFirst(), 'first4')
        self.assertEqual(list.removeFirst(), 'first5')

    def test_removeMiddle(self) :
        list = init_list()
        # 1,2,3,4,5
        self.assertEqual(list.removeNode(0), 'first1')
        # 2,3,4,5
        self.assertEqual(list.removeNode(1), 'first3')
        # 2,4,5
        self.assertEqual(list.removeNode(-10), 'first2')
        # 4,5
        self.assertEqual(list.removeNode(10), 'first5')
        # 4

    def test_removeLast(self) :
        list = init_list()
        self.assertEqual(list.removeLast(), 'first5')
        self.assertEqual(list.removeLast(), 'first4')
        self.assertEqual(list.removeLast(), 'first3')
        self.assertEqual(list.removeLast(), 'first2')
        self.assertEqual(list.removeLast(), 'first1')
        self.assertEqual(list.removeLast(), 'This List has any data.')


    def test_total(self) :
        list = init_list()
        # 1,2,3,4,5
        self.assertEqual(list.removeFirst(), 'first1')
        # 2,3,4,5
        self.assertEqual(list.removeLast(), 'first5')
        # 2,3,4
        self.assertEqual(list.removeNode(1), 'first3')
        # 2,4
        self.assertEqual(list.removeNode(10), 'first4')
        # 2
        self.assertEqual(list.removeLast(), 'first2')
        # empty
        self.assertEqual(list.removeLast(), 'This List has any data.')
        self.assertEqual(list.removeFirst(), 'This List has any data.')
        self.assertEqual(list.removeNode(1), 'This List has any data.')
if __name__ == '__main__':
    unittest.main()

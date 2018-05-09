import unittest
from LinkedList import LinkedList

class RemoveFromLinkedListTest(unittest.TestCase) :

    def setUp(self) :
        self.list = LinkedList()
        self.list.addFirst('first1')
        self.list.addLast('first2')
        self.list.addLast('first3')
        self.list.addLast('first4')
        self.list.addLast('first5')
        print('set up')

    def tearDown(self) :
        print('tearDown')

    def test_removeFromEmptyList(self) :
        list = LinkedList()
        self.assertEqual(list.removeFirst(), 'This List has any data.')
        self.assertEqual(list.removeNode(2), 'This List has any data.')

    def test_removeFirst(self) :
        self.assertEqual(self.list.removeFirst(), 'first1')
        self.assertEqual(self.list.removeFirst(), 'first2')
        self.assertEqual(self.list.removeFirst(), 'first3')
        self.assertEqual(self.list.removeFirst(), 'first4')
        self.assertEqual(self.list.removeFirst(), 'first5')

    def test_removeMiddle(self) :
        # 1,2,3,4,5
        self.assertEqual(self.list.removeNode(0), 'first1')
        # 2,3,4,5
        self.assertEqual(self.list.removeNode(1), 'first3')
        # 2,4,5
        self.assertEqual(self.list.removeNode(-10), 'first2')
        # 4,5
        self.assertEqual(self.list.removeNode(10), 'first5')
        # 4

    def test_removeLast(self) :
        print(self.list.show())
        self.assertEqual(self.list.removeLast(), 'first5')
        print(self.list.show())
        self.assertEqual(self.list.removeLast(), 'first4')
        print(self.list.show())
        self.assertEqual(self.list.removeLast(), 'first3')
        print(self.list.show())
        self.assertEqual(self.list.removeLast(), 'first2')
        print(self.list.show())
        self.assertEqual(self.list.removeLast(), 'first1')
        print(self.list.show())
        self.assertEqual(self.list.removeLast(), 'This List has any data.')


    def test_total(self) :
        # 1,2,3,4,5
        self.assertEqual(self.list.removeFirst(), 'first1')
        # 2,3,4,5
        self.assertEqual(self.list.removeLast(), 'first5')
        # 2,3,4
        self.assertEqual(self.list.removeNode(1), 'first3')
        # 2,4
        self.assertEqual(self.list.removeNode(10), 'first4')
        # 2
        self.assertEqual(self.list.removeLast(), 'first2')
        # empty
        self.assertEqual(self.list.removeLast(), 'This List has any data.')
        self.assertEqual(self.list.removeFirst(), 'This List has any data.')
        self.assertEqual(self.list.removeNode(1), 'This List has any data.')
if __name__ == '__main__':
    unittest.main()

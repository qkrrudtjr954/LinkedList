import unittest
from LinkedList import LinkedList


class AddToLinkedListTest(unittest.TestCase) :

    def test_addToHead(self) :
        list = LinkedList()
        list.addFirst('first1')
        self.assertEqual(list.show(), ['first1'])
        list.addFirst('first2')
        self.assertEqual(list.show(), ['first2', 'first1'])
        list.addFirst('first3')
        self.assertEqual(list.show(), ['first3', 'first2', 'first1'])

    def test_addToTail(self) :
        list = LinkedList()
        list.addLast('first1')
        self.assertEqual(list.show(), ['first1'])
        list.addLast('first2')
        self.assertEqual(list.show(), ['first1', 'first2'])
        list.addLast('first3')
        self.assertEqual(list.show(), ['first1', 'first2', 'first3'])


    def test_addToMiddle(self) :
        list = LinkedList()
        list.addNode(3, 'first5')
        self.assertEqual(list.show(), ['first5'])
        list.addFirst('first1')
        self.assertEqual(list.show(), ['first1', 'first5'])
        list.addNode(0, 'first2')
        self.assertEqual(list.show(), ['first2', 'first1', 'first5'])
        list.addNode(10, 'first3')
        self.assertEqual(list.show(), ['first2', 'first1', 'first5', 'first3'])
        list.addNode(-3, 'first4')
        self.assertEqual(list.show(), ['first4', 'first2', 'first1', 'first5', 'first3'])

if __name__ == '__main__':
    unittest.main()

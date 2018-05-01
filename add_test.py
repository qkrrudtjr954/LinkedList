import unittest
from LinkedList import LinkedList


class AddToLinkedListTest(unittest.TestCase) :

    def test_addToHead(self) :
        list = LinkedList()
        list.add(0, 'first1')
        list.add(0, 'first2')
        list.add(0, 'first3')
        self.assertEqual(list.show(), ['first3', 'first2', 'first1'])


    def test_addToTail(self) :
        list = LinkedList()
        list.add(0, 'first1')
        list.add(0, 'first2')
        list.add(10, 'first3')
        self.assertEqual(list.show(), ['first2', 'first1', 'first3'])

    def test_addToSpecific(self) :
        list = LinkedList()
        list.add(2, 'first1')
        list.add(0, 'first2')
        list.add(10, 'first3')
        self.assertEqual(list.show(), ['first2', 'first1', 'first3'])

if __name__ == '__main__':
    unittest.main()

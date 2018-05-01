import unittest
from LinkedList import Node, LinkedList

def init_list(self) :
    list = LinkedList()
    list.add(0, 'first0')
    list.add(1, 'first1')
    list.add(2, 'first2')
    list.add(3, 'first3')
    list.add(4, 'first4')

    return list

class RemoveFromLinkedListTest(unittest.TestCase) :

    def test_removeFromHead(self) :
        list = init_list(self)

        self.assertEqual(list.remove(0), 'first0')
        self.assertEqual(list.remove(0), 'first1')
        self.assertEqual(list.remove(0), 'first2')

        self.assertEqual(list.show(), ['first3', 'first4'])

    def test_removeFromTail(self) :
        list = init_list(self)

        self.assertEqual(list.remove(4), 'first4')
        self.assertEqual(list.remove(10), 'first3')
        self.assertEqual(list.remove(100), 'first2')
        self.assertEqual(list.show(), ['first0', 'first1'])

    def test_removeFromSpecific(self) :
        list = init_list(self)

        self.assertEqual(list.remove(1), 'first1')
        self.assertEqual(list.remove(3), 'first4')
        self.assertEqual(list.remove(2), 'first3')
        self.assertEqual(list.show(), ['first0','first2'])

if __name__ == '__main__':
    unittest.main()

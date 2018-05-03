import unittest
from LinkedList import LinkedList

class CommonLinkedListTest(unittest.TestCase) :
    def test_get(self) :
        list = LinkedList()
        list.addFirst('first1')
        list.addLast('first2')
        list.addLast('first3')
        list.addLast('first4')
        list.addLast('first5')

        self.assertEqual(list.get(0), 'first1')
        self.assertEqual(list.get(1), 'first2')
        self.assertEqual(list.get(2), 'first3')
        self.assertEqual(list.get(3), 'first4')
        self.assertEqual(list.get(4), 'first5')

        self.assertEqual(list.get(40), 'first5')
        self.assertEqual(list.get(-40), 'first1')

if __name__ == '__main__':
    unittest.main()

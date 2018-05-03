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

class CommonLinkedListTest(unittest.TestCase) :
    def test_get(self) :
        list = init_list()

        self.assertEqual(list.get(0), 'first1')
        self.assertEqual(list.get(1), 'first2')
        self.assertEqual(list.get(2), 'first3')
        self.assertEqual(list.get(3), 'first4')
        self.assertEqual(list.get(4), 'first5')

        self.assertEqual(list.get(40), 'first5')
        self.assertEqual(list.get(-40), 'first1')

    def test_has(self) :
        list = init_list()

        self.assertTrue(list.has('first1'))
        self.assertTrue(list.has('first2'))
        self.assertTrue(list.has('first3'))
        self.assertTrue(list.has('first4'))
        self.assertTrue(list.has('first5'))

        self.assertFalse(list.has('second1'))

    def test_indexOf(self) :
        list = init_list()

        self.assertEqual(list.indexOf('first1'), 0)
        self.assertEqual(list.indexOf('first2'), 1)
        self.assertEqual(list.indexOf('first3'), 2)
        self.assertEqual(list.indexOf('first4'), 3)
        self.assertEqual(list.indexOf('first5'), 4)

if __name__ == '__main__':
    unittest.main()

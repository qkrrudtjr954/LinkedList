import unittest
from LinkedList import LinkedList

class CommonLinkedListTest(unittest.TestCase) :

    def setUp(self) :
        self.list = LinkedList()
        self.list.addFirst('first1')
        self.list.addLast('first2')
        self.list.addLast('first3')
        self.list.addLast('first4')
        self.list.addLast('first5')
        print('set up')

    def tearDown(self) :
        print('tear down')

    def test_get(self) :
        self.assertEqual(self.list.get(0), 'first1')
        self.assertEqual(self.list.get(1), 'first2')
        self.assertEqual(self.list.get(2), 'first3')
        self.assertEqual(self.list.get(3), 'first4')
        self.assertEqual(self.list.get(4), 'first5')

        self.assertEqual(self.list.get(40), 'first5')
        self.assertEqual(self.list.get(-40), 'first1')

    def test_has(self) :
        self.assertTrue(self.list.has('first1'))
        self.assertTrue(self.list.has('first2'))
        self.assertTrue(self.list.has('first3'))
        self.assertTrue(self.list.has('first4'))
        self.assertTrue(self.list.has('first5'))
        self.assertFalse(self.list.has('second1'))

    def test_indexOf(self) :
        self.assertEqual(self.list.indexOf('first1'), 0)
        self.assertEqual(self.list.indexOf('first2'), 1)
        self.assertEqual(self.list.indexOf('first3'), 2)
        self.assertEqual(self.list.indexOf('first4'), 3)
        self.assertEqual(self.list.indexOf('first5'), 4)

if __name__ == '__main__':
    unittest.main()

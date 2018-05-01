import unittest
from LinkedList import Node

class LinkedListTest(unittest.TestCase) :
    def test_makeNode(self) :
        node = Node()
        self.assertEqual(node.name, 'node')

if __name__ == '__main__':
    unittest.main()

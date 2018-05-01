import unittest
from LinkedList import Node

class CommonLinkedListTest(unittest.TestCase) :
    def test_makeNode(self) :
        node = Node()
        self.assertEqual(node.name, 'node')

    def test_search(self) :
        pass

if __name__ == '__main__':
    unittest.main()

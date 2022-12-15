import unittest

from AVLTreeList import AVLTreeList


class MyTestCase(unittest.TestCase):


    def test_initialization(self):
        tree = AVLTreeList()
        self.assertTrue(tree.empty())
        self.assertEqual(0, tree.length())
        self.assertEqual(None, tree.getRoot())


    def test_insertion_and_deletion(self):  # checking length(), empty() and height while at it.
        tree = AVLTreeList()

        tree.insert(0, "meow")
        self.assertFalse(tree.empty())
        self.assertEqual(1, tree.length())
        self.assertEqual("((None), meow, (None))", str(tree))
        tree.delete(0)
        self.assertEqual(0, tree.length())
        self.assertTrue(tree.empty())
        self.assertEqual("(None)", str(tree))

        for i in range(10000):
            val = str(i)
            tree.insert(i, val)
        self.assertEqual([str(i) for i in range(10000)], tree.listToArray())
        self.assertLessEqual(13, tree.getRoot().getHeight())
        self.assertEqual(10000, tree.length())

        for i in range(9999, 4999, -1):
            tree.delete(i)
        self.assertEqual([str(i) for i in range(5000)], tree.listToArray())
        self.assertLessEqual(12, tree.getRoot().getHeight())
        self.assertEqual(5000, tree.length())

        for i in range(5000):
            if (4999 - i) % 2 == 0:
                tree.delete(4999 - i)
        self.assertEqual([str(i) for i in range(5000) if i % 2 != 0], tree.listToArray())
        self.assertLessEqual(11, tree.getRoot().getHeight())
        self.assertEqual(2500, tree.length())




if __name__ == '__main__':
    unittest.main()

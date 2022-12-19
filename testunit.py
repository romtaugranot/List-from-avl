import unittest
import random

from AVLTreeList import AVLTreeList, successor


class MyTestCase(unittest.TestCase):

    def printBF(self, node):
        if not node.isRealNode():
            return
        if node.getBF() >= 2:
            print("error")
        self.printBF(node.getRight())
        self.printBF(node.getLeft())

    def test_initialization(self):
        tree = AVLTreeList()
        self.assertTrue(tree.empty())
        self.assertEqual(0, tree.length())
        self.assertEqual(None, tree.getRoot())


    def test_insertion_and_deletion(self):  # checking length(), empty(), listToArray and height while at it.
        tree = AVLTreeList()
        self.assertEqual([], tree.listToArray())
        self.assertEqual(0, tree.length())
        tree.insert(0, "meow")
        self.assertFalse(tree.empty())
        self.assertEqual(1, tree.length())
        self.assertEqual("meow", tree.root.value)
        self.assertEqual("meow", tree.max.value)
        self.assertEqual("meow", tree.min.value)
        self.assertEqual("['meow']", str(tree.listToArray()))

        tree = AVLTreeList()

        lst = []
        for i in range(10000):
            k = random.randint(0, tree.length())
            val = str(k)
            tree.insert(k, val)

            lst.append(val)
        self.assertEqual(sorted(lst), sorted(tree.listToArray()))
        self.assertLessEqual(13, tree.getRoot().getHeight())
        self.assertEqual(10000, tree.length())
        self.printBF(tree.root)

        for i in range(9999, 4999, -1):
            tree.delete(i)
        # self.assertEqual([str(i) for i in range(5000)], tree.listToArray())
        self.assertLessEqual(12, tree.getRoot().getHeight())
        self.assertEqual(5000, tree.length())
        self.printBF(tree.root)

        for i in range(5000):
            if (4999 - i) % 2 == 0:
                tree.delete(4999 - i)
        # self.assertEqual([str(i) for i in range(5000) if i % 2 != 0], tree.listToArray())
        self.assertLessEqual(11, tree.getRoot().getHeight())
        self.assertEqual(2500, tree.length())
        self.printBF(tree.root)



    def test_first_and_last(self):
        tree = AVLTreeList()
        self.assertEqual(None, tree.first())
        self.assertEqual(None, tree.last())

        for i in range(100):
            val = str(i)
            tree.insert(i, val)

        self.assertEqual("0", tree.first())
        self.assertEqual("99", tree.last())

        tree.delete(99)
        self.assertEqual("98", tree.last())
        tree.delete(0)
        self.assertEqual("1", tree.first())

        for i in range(97, -1, -1):
            tree.delete(i)
        self.assertEqual(None, tree.first())
        self.assertEqual(None, tree.last())


    def test_permutation(self):
        tree = AVLTreeList()
        # self.assertEqual(str(tree), str(tree.permutation()))
        tree.insert(0, '0')
        # self.assertEqual(str(tree), str(tree.permutation()))
        for i in range(1, 10):
            val = str(i)
            tree.insert(i, val)
        # print(tree.permutation().listToArray())
        lst = tree.permutation().listToArray()
        lst.sort()
        self.assertEqual([str(i) for i in range(10)], lst)


    def test_sort(self):
        tree = AVLTreeList()
        # self.assertEqual(str(tree), str(tree.sort()))
        tree.insert(0, '0')
        # self.assertEqual(str(tree), str(tree.sort()))
        for i in range(1, 10):
            val = str(i)
            tree.insert(i, val)
        tree = tree.permutation()
        self.assertEqual([str(i) for i in range(10)], tree.sort().listToArray())


    def test_concat(self):
        tree1 = AVLTreeList()
        tree2 = AVLTreeList()
        r = tree1.concat(tree2)
        self.assertEqual(0, r)
        self.assertEqual(None, tree1.root.value)

        for i in range(10):
            val = str(i)
            tree2.insert(i, val)
        r = tree1.concat(tree2)
        # print(r)
        self.assertEqual([str(i) for i in range(10)], tree1.listToArray())

        tree1 = AVLTreeList()
        tree2 = AVLTreeList()
        for i in range(20):
            val = str(i)
            tree1.insert(i, val)
        for i in range(10):
            val = str(i)
            tree2.insert(i, val)
        # print(tree1.listToArray())
        # print(tree2.listToArray())
        r = tree1.concat(tree2)
        # print(r)
        self.assertEqual(sorted([str(i) for i in range(20)] + [str(i) for i in range(10)]), tree1.sort().listToArray())


    def test_search(self):
        tree = AVLTreeList()
        self.assertEqual(-1, tree.search("8"))
        for i in range(1000):
            val = str(i)
            tree.insert(i, val)
        self.assertEqual(500, tree.search("500"))
        for i in range(999, -1, -1):
            if i % 2 == 0:
                tree.delete(i)
        self.assertEqual(-1, tree.search("500"))
        self.assertEqual(249, tree.search("499"))
        for i in range(499, -1, -1):
            tree.delete(i)
        for i in range(0, 100):
            self.assertEqual(-1, tree.search(str(i)))



    def test_q1(self):
        for i in range(1, 11):
            tree = AVLTreeList()
            n = 1500 * (2 ** i)
            count = 0
            for j in range(0, n):
                k = random.randint(0, tree.length())
                count += tree.insert(k, str(k))
            print("count for i =", i, " is:", count)


if __name__ == '__main__':
    unittest.main()

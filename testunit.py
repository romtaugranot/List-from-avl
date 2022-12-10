import unittest

from AVLTreeList import AVLTreeList


class MyTestCase(unittest.TestCase):

    def test_insertion(self):
        tree = AVLTreeList()

        self.assertEqual("(None)", str(tree))

        tree.insert(0, "meow")
        self.assertEqual("((None), meow, (None))", str(tree))
        self.assertEqual(1, tree.length())

        self.assertEqual("0, 0", str(tree.getRoot().getLeft().getSize()) + ", " + str(tree.getRoot().getRight().getSize()))


        tree.insert(1, "daddy")
        self.assertEqual("((None), meow, ((None), daddy, (None)))", str(tree))

        self.assertEqual("0, 1", str(tree.getRoot().getLeft().getSize()) + ", " + str(tree.getRoot().getRight().getSize()))


        tree.insert(1, "mommy")
        tree.insert(2, "sonny")
        tree.insert(0, "dottary")
        self.assertEqual("(((None), dottary, (None)), meow, (((None), mommy, ((None), sonny, (None))), daddy, (None)))", str(tree))


    def test_retrieve(self):
        tree = AVLTreeList()
        tree.insert(0, "meow")
        tree.insert(1, "daddy")
        tree.insert(1, "mommy")
        tree.insert(2, "sonny")
        tree.insert(0, "dottary")


        self.assertEqual("dottary", str(tree.retrieve(0)))
        self.assertEqual("meow", str(tree.retrieve(1)))
        self.assertEqual("mommy", str(tree.retrieve(2)))
        self.assertEqual("sonny", str(tree.retrieve(3)))
        self.assertEqual("daddy", str(tree.retrieve(4)))


    def test_deletion(self):
        tree = AVLTreeList()
        tree.insert(0, "meow")
        tree.insert(1, "daddy")
        tree.insert(1, "mommy")
        tree.insert(2, "sonny")
        tree.insert(0, "dottary")

        self.assertEqual("5", str(tree.length()))
        tree.delete(2)  # deleted mommy
        self.assertEqual("(((None), dottary, (None)), meow, (((None), sonny, (None)), daddy, (None)))", str(tree))
        self.assertEqual("dottary", str(tree.retrieve(0)))
        self.assertEqual("meow", str(tree.retrieve(1)))
        self.assertEqual("sonny", str(tree.retrieve(2)))
        self.assertEqual("daddy", str(tree.retrieve(3)))
        self.assertEqual("4", str(tree.length()))

        tree.delete(2)  # deleted sonny
        self.assertEqual("(((None), dottary, (None)), meow, ((None), daddy, (None)))", str(tree))

        tree.insert(2, "sonny")
        tree.delete(3)  # deleted daddy
        self.assertEqual("3", str(tree.length()))
        self.assertEqual("(((None), dottary, (None)), meow, ((None), sonny, (None)))", str(tree))


    def test_first_and_last(self):
        tree = AVLTreeList()
        tree.insert(0, "meow")
        tree.insert(1, "daddy")
        tree.insert(1, "mommy")
        tree.insert(2, "sonny")
        tree.insert(0, "dottary")

        self.assertEqual("dottary", tree.first())
        self.assertEqual("daddy", tree.last())

        tree.delete(2)  # deleted mommy
        tree.delete(2)  # deleted sonny
        self.assertEqual("daddy", tree.last())

        tree.delete(2)  # deleted daddy
        self.assertEqual("meow", tree.last())

        tree.delete(0)  # deleted dottary
        self.assertEqual(tree.first(), tree.last())





if __name__ == '__main__':
    unittest.main()

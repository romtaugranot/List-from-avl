import unittest

from AVLTreeList import AVLTreeList, successor


class MyTestCase(unittest.TestCase):

    def test_insertion(self):
        print("insertion:")
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
        print(str(tree))



    def test_retrieve(self):
        print("retrieve:")
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
        print("deletion:")
        tree = AVLTreeList()
        tree.insert(0, "meow")
        print(str(tree))
        tree.insert(1, "daddy")
        print(str(tree))
        print("amount of rotations is " + str(tree.insert(1, "mommy")))
        print(str(tree))
        tree.insert(2, "sonny")
        print(str(tree))
        tree.insert(0, "dottary")
        print(str(tree))
        self.assertEqual("5", str(tree.length()))
        print("amount of rotations is " + str(tree.delete(2)))  # deleted mommy
        print(str(tree))
        self.assertEqual("dottary", str(tree.retrieve(0)))
        self.assertEqual("meow", str(tree.retrieve(1)))
        self.assertEqual("sonny", str(tree.retrieve(2)))
        self.assertEqual("daddy", str(tree.retrieve(3)))
        self.assertEqual("4", str(tree.length()))

        print("amount of rotations is " + str(tree.delete(2)))  # deleted sonny
        print(str(tree))
        tree.insert(2, "sonny")
        print(str(tree))
        tree.delete(3)  # deleted daddy
        print(str(tree))
        self.assertEqual("3", str(tree.length()))


    def test_first_and_last(self):
        print("first and last:")
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


    def test_listToArray(self):
        print("list to array:")
        tree = AVLTreeList()
        self.assertEqual("[]", str(tree.listToArray()))

        tree.insert(0, "meow")
        self.assertEqual("['meow']", str(tree.listToArray()))

        tree.insert(1, "daddy")
        tree.insert(1, "mommy")
        tree.insert(2, "sonny")
        tree.insert(0, "dottary")

        self.assertEqual("['dottary', 'meow', 'mommy', 'sonny', 'daddy']", str(tree.listToArray()))

        tree.delete(2)  # deleted mommy
        self.assertEqual("['dottary', 'meow', 'sonny', 'daddy']", str(tree.listToArray()))

        tree.delete(0)  # deleted dottary
        tree.delete(2)  # deleted daddy
        self.assertEqual("['meow', 'sonny']", str(tree.listToArray()))


    def test_permutations(self):
        print("permutations:")
        tree = AVLTreeList()
        tree.insert(0, "1")
        tree.insert(1, "2")
        tree.insert(1, "3")
        tree.insert(2, "4")
        tree.insert(0, "5")
        tree.insert(3, "6")
        tree.insert(0, "7")
        tree.insert(5, "8")
        print(tree.listToArray())
        #tree.permutation()
        #print(tree.listToArray())


    def test_search(self):
        print("search:")
        tree = AVLTreeList()
        tree.insert(0, "1")
        tree.insert(1, "2")
        tree.insert(1, "3")
        tree.insert(2, "1")
        tree.insert(0, "5")
        tree.insert(3, "6")
        tree.insert(0, "7")
        tree.insert(5, "8")
        print(tree.listToArray())

        # ['7', '5', '1', '3', '6', '8', '1', '2']
        self.assertEqual('2', str(tree.search('1')))
        self.assertEqual('-1', str(tree.search("meow")))
        tree.delete(2)
        # ['7', '5', '3', '6', '8', '1', '2']
        print(tree.listToArray())
        self.assertEqual('5', str(tree.search("1")))


if __name__ == '__main__':
    unittest.main()

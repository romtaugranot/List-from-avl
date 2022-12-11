# username - romgranot
# id1      - 325020790
# name1    - Rom Granot
# id2      - 325260362
# name2    - Ido Ben David
import random

"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node, value == None if and only if node is virtual
    """

    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        if value is None:  # node is virtual
            self.left = None
            self.right = None
            self.bf = 0
            self.height = -1
            self.size = 0
            self.min = None
            self.max = None
        else:  # node is not virtual
            if left is None:
                self.left = AVLNode(None, self)
            else:
                self.left = left
            if right is None:
                self.right = AVLNode(None, self)
            else:
                self.right = right
            self.height = max(self.left.height, self.right.height) + 1
            self.updateSize()
            self.updateBF()

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height

    """returns the size of the node's subtree

        @rtype: int
        @returns: the size of the node's subtree, 0 if the node is virtual
        """

    def getSize(self):
        return self.size

    """returns the bf

            @rtype: int
            @returns: the bf of the node, 0 if the node is virtual
            """

    def getBF(self):
        return self.bf


    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    """sets the size of the node

        @type size: int
        @param size: the size
        """

    def setSize(self, size):
        self.size = size

    """updates the height of the node according to its children"""
    def updateHeight(self):
        self.height = 1 + max(self.left.height, self.right.height)

    """updates the size of the node according to its children"""

    def updateSize(self):
        self.size = self.left.size + self.right.size + 1

    """updates the bf of the node according to its children"""

    def updateBF(self):
        self.bf = self.left.height - self.right.height


    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.value is not None

    def is_leaf(self):
        return self.isRealNode() and not self.left.isRealNode() and not self.right.isRealNode()


    """in-order representation of the tree"""

    def __repr__(self):
        if self.left is None:  # only virtual nodes have children that are None
            return "(None)"
        out = "(" + str(self.left) + ", " + str(self.value) + ", " + str(self.right) + ")"
        return out


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.size = 0
        self.root = AVLNode(None)
        self.min = self.root
        self.max = self.root

    # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.size == 0

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        return tree_select(self.root, i + 1).getValue()

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        insert_tree(self, i, AVLNode(val))
        self.size = self.root.getSize()

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        tree_delete(self, tree_select(self.getRoot(), i + 1))
        self.size = self.root.getSize()

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return self.min.getValue() if not self.empty() else None

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return self.max.getValue() if not self.empty() else None

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """


    def listToArray(self):
        return listToArray(self.root)  # the method is down below with the rest of the supporting methods.

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return self.size

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        return None

    """permute the info values of the list """

    def permutation(self):
        lst = self.listToArray()
        random.shuffle(lst)  # runtime is O(n) by the API.
        lst.append(0)
        fill_tree_in_order(self.root, lst)  # method is in the supporting methods below.


    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        return None

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        return search_tree(self.min, val)

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root if self.length() != 0 else None

    """sets the root of the node

        @type root: AVLNode
        @param root: the new root of the bst
        """

    def setRoot(self, root):
        self.root = root


    """updates the minimum / maximum of the tree"""

    def updateMinMax(self):
        self.min = minimum(self.root)
        self.max = maximum(self.root)


    """representation of the tree"""

    def __repr__(self):
        return str(self.root)

    """Rom's and Ido's functions"""


"""sorted-order method from class."""


def sorted_order(x):
    if x is not None and x.isRealNode():
        sorted_order(x.getLeft())
        print(x)
        sorted_order(x.getRight())


"""minimum method from class.
    @pre: x is not None and x.isRealNode()"""


def minimum(x):
    while x.getLeft().isRealNode():
        x = x.getLeft()
    return x


"""maximum method.
    @pre: x is not None and x.isRealNode()"""


def maximum(x):
    while x.getRight().isRealNode():
        x = x.getRight()
    return x


"""successor method from class.
    @inv: successor is None if and only if x is the largest in the tree.
    @pre: x is not None and x.isRealNode()"""


def successor(x):
    if x.getRight().isRealNode():
        return minimum(x.getRight())
    y = x.getParent()
    while y is not None and y.isRealNode() and x == y.getRight():
        x = y
        y = x.getParent()
    return y


"""predecessor method from class.
    @inv: predecessor is None if and only if x is the smallest in the tree.
    @pre: x is not None and x.isRealNode()"""


def predecessor(x):
    if x.getLeft().isRealNode() is not None:
        return maximum(x.getLeft())
    y = x.getParent()
    while y is not None and y.isRealNode() and x == y.getLeft():
        x = y
        y = x.getParent()
    return y


"""tree-select from class.
    @pre: x is not None and x.isRealNode()
    @pre: 0 <= k <= x.getSize()"""


def tree_select(x, k):
    r = x.getLeft().getSize() + 1
    if k == r:
        return x
    elif k < r:
        return tree_select(x.getLeft(), k)
    else:
        return tree_select(x.getRight(), k - r)


"""tree-rank from class.
    @pre: x is not None and x.isRealNode()"""


def tree_rank(x):
    r = x.getLeft().getSize() + 1
    y = x
    while y is not None and y.isRealNode():
        if y.getParent() is not None and y.getParent().isRealNode() and y == y.getParent().getRight():
            r = r + y.getParent().getLeft().getSize() + 1
        y = y.getParent()
    return r


"""updates all the size fields from z up to the root
    this method is used to help insertion / deletion / rotation etc.
    @pre: z is not None and z.isRealNode()
    @pre: shift is an integer, can be negative."""


def update_sizes_up_to_root(z, shift):
    y = z.parent
    while y is not None and y.isRealNode():
        y.setSize(y.getSize() + shift)
        y = y.getParent()


"""insert-tree from the powerpoint representation
    @pre: bst is not None
    @pre:z is not None and z.isRealNode()
    @pre: 0 <= i < bst's size"""


def insert_tree(bst, i, z):
    if i == 0:
        if bst.getRoot() is None or not bst.getRoot().isRealNode():
            bst.setRoot(z)
            return
        else:
            y = minimum(bst.getRoot())
            y.setLeft(z)
            z.setParent(y)
    elif i == bst.length():
        y = maximum(bst.getRoot())
        y.setRight(z)
        z.setParent(y)
    else:
        x = tree_select(bst.getRoot(), i + 1)
        if not x.left.isRealNode():
            x.setLeft(z)
            z.setParent(x)
        else:
            y = predecessor(x)
            y.setRight(z)
            z.setParent(y)

    update_sizes_up_to_root(z, 1)
    bst.updateMinMax()
    # TODO: fix tree (when it is an avl)


"""tree-delete method.
    @pre: bst is not None and z is in bst
    @pre: z is not None and z.isRealNode()"""


def tree_delete(bst, z):
    if z == bst.getRoot() and z.is_leaf():
        bst.setRoot(AVLNode(None))  # make the root a virtual node, which means there are no nodes in the tree.
        return
    update_sizes_up_to_root(z, -1)
    y = z.getParent()
    if z.is_leaf():
        # z isn't a root for sure.
        if z == y.getRight():
            y.setRight(AVLNode(None))
        if z == y.getLeft():
            y.setLeft(AVLNode(None))
    if not z.getLeft().isRealNode() or not z.getRight().isRealNode():  # z has only one child
        x = z.getRight()
        if z.getLeft().isRealNode():  # z only has left child.
            x = z.getLeft()

        if z != bst.getRoot():  # for sure y is not None if z isn't bst's root.
            if z == y.getRight():
                y.setRight(x)
            if z == y.getLeft():
                y.setLeft(x)
        else:
            bst.setRoot(x)

        x.setParent(y)
    else:  # z has 2 children.
        x = successor(z)
        val = x.getValue()
        tree_delete(bst, x)
        z.setValue(val)

    bst.updateMinMax()



"""listToArray method, converts an avl tree into a list
    @pre: node is not None"""


def listToArray(node):
    if not node.isRealNode():
        return []
    if node.is_leaf():
        return [node.getValue()]
    lst = []
    lst += listToArray(node.getLeft())
    lst.append(node.getValue())
    lst += listToArray(node.getRight())
    return lst


"""fill_tree_in_order method, inserts the values in lst to the tree
    @pre: node is not None
    @pre: lst's size - index is the node's sub-tree size"""


def fill_tree_in_order(node, lst):
    if not node.isRealNode():
        return
    elif node.is_leaf():
        node.setValue(lst[lst[len(lst)-1]])
        lst[len(lst) - 1] += 1
    else:
        fill_tree_in_order(node.getLeft(), lst)
        node.setValue(lst[lst[len(lst) - 1]])
        lst[len(lst) - 1] += 1
        fill_tree_in_order(node.getRight(), lst)


"""search_tree method, looks for a value in the tree
    @pre: val is a string"""


def search_tree(node, val):
    if node is None or not node.isRealNode():
        return -1
    return tree_rank(node) - 1 if node.getValue() == val else search_tree(successor(node), val)


"""fix_tree method fixes nodes from inputted node up until the root, returns the number of rotations
    @pre: node is not None"""


def fix_tree(self, x, is_insert=False):
    counter = 0
    y = x.getParent()
    while y is not None:
        height = 1 + max(y.getLeft().getHeight(), y.getRight().getHeight())
        balance = y.getLeft().getHeight() - y.getRight.getHeight()
        if abs(balance) < 2 and height == y.getHeight():
            break
        elif abs(balance) < 2 and height != y.getHeight():
            y.setHeight(height)
            y.setBF(balance)
            x = y
            y = x.getParent()
        else: #meaning abs(balance) == 2
            if balance == 2:
                balance_child = y.getLeft().getLeft().getHeight() - y.getLeft().getRight().getHeight()
                if balance_child > -1:
                    right_rotate(self, y)
                    counter += 1
                else:
                    left_rotate(self, y.getLeft())
                    right_rotate(self, y)
                    counter += 2
            else: #meaning balance = -2
                balance_child = y.getRight().getLeft().getHeight() - y.getRight().getRight().getHeight()
                if balance_child < 1:
                    left_rotate(self, y)
                    counter += 1
                else:
                    right_rotate(self, y.getRight())
                    left_rotate(self, y)
                    counter += 2
            if is_insert: #if this is after an insert, we can stop after a single rotation
                break
            y.setHeight(height)
            y.setBF(balance)
            x = y
            y = x.getParent()
    return counter


"""left_rotate method rotates the inputted node and its children to the left, and updates their height, size and BF accordingly
    @pre: node is not None"""
def left_rotate(self, x):
    y = x.getRight()

    #updating the pointers
    x.setRight(y.getLeft())
    x.getRight().setParent(x)
    y.setLeft(x)
    y.setParent(x.getParent())
    if x.getParent().getRight() == x:
        x.getParent().setRight(y)
    else:
        x.getParent().setLeft(y)
    x.setParent(y)

    #updating heights, size and BF
    x.updateHeight()
    y.updateHeight()
    x.updateSize()
    y.updateSize()
    x.updateBF()
    y.updateBF()

def right_rotate(self, x):
    y = x.getLeft()

    # updating the pointers
    x.setLeft(y.getRight())
    x.getLeft().setParent(x)
    y.setRight(x)
    y.setParent(x.getParent())
    if x.getParent().getRight() == x:
        x.getParent().setRight(y)
    else:
        x.getParent().setLeft(y)
    x.setParent(y)

    # updating heights, size and BF
    x.updateHeight()
    y.updateHeight()
    x.updateSize()
    y.updateSize()
    x.updateBF()
    y.updateBF()



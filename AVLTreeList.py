# username - romgranot
# id1      - 325020790
# name1    - Rom Granot
# id2      - 325260362
# name2    - Ido Ben David


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
        return tree_select(self.root, i+1).getValue()

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
        tree_delete(self, tree_select(self.getRoot(), i+1))
        self.size = self.root.getSize()

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        return None

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        return None

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        return None

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

    """permute the info values of the list 

    @rtype: list
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        return None

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
        return None

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

    # TODO: fix tree (when it is an avl)


"""tree-delete method.
    @pre: bst is not None and z is in bst
    @pre: z is not None and z.isRealNode()"""


def tree_delete(bst, z):
    def delete_connections_from_node(node):
        node.setParent(None)
        node.setRight(AVLNode(None))
        node.setLeft(AVLNode(None))


    if z == bst.getRoot():
        bst.setRoot(AVLNode(None))  # make the root a virtual node, which means there are no nodes in the tree.
        delete_connections_from_node(z)
        return
    update_sizes_up_to_root(z, -1)
    y = z.getParent()  # guaranteed to be not None and not virtual because z isn't root.
    if not z.getLeft().isRealNode() or not z.getRight().isRealNode():
        x = AVLNode(None)  # if z is a leaf.
        if z.getLeft().isRealNode():  # z only has left child.
            x = z.getLeft()
        elif z.getRight().isRealNode():  # z only has right child.
            x = z.getRight()

        if z == y.getRight():
            y.setRight(x)
        if z == y.getLeft():
            y.setLeft(x)
        x.setParent(y)
    else:  # z has 2 children. im keeping a conservative approach and assuming we have an outside pointer to z,
        # so we can't just change z's info to be x's info.
        x = successor(z)
        tree_delete(bst, x)
        if z == y.getRight():
            y.setRight(x)
        else:
            y.setLeft(x)
        x.setParent(y)
        x.setRight(z.getRight())
        x.setLeft(z.getLeft())

    delete_connections_from_node(z)



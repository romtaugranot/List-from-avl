# username - romgranot
# id1      - 325020790
# name1    - Rom Granot
# id2      - 325260362
# name2    - Ido Ben David


"""A class representing a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

	@type value: str
	@param value: data of your node
	"""

    def __init__(self, value, isReal=True, parent=None, right=None, left=None):
        self.isReal = isReal
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.bf = self.left.height - self.right.height
        if left is None and right is None:
            self.height = 0
        else:  # node isn't a leaf.
            self.height = max(left.height, right.height) + 1

    """returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child
	"""

    def getLeft(self):
        return self.left if self.isReal else None

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child
	"""

    def getRight(self):
        return self.right if self.isReal else None

    """returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

    def getParent(self):
        return self.parent if self.isReal else None

    """return the value

	@rtype: str
	@returns: the value of self, None if the node is virtual
	"""

    def getValue(self):
        return self.value if self.isReal else None

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

    def getHeight(self):
        return self.height if self.isReal else -1

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

    """sets the balance factor of the node

	@type h: int
	@param h: the height
	"""

    def setHeight(self, h):
        self.height = h

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def isRealNode(self):
        return self.isReal

    """sets the node to be virtual"""

    def setVirtual(self, var):
        self.isReal = var


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
	Constructor, you are allowed to add more fields.  
    @imp_inv: empty() == True if and only if root is None
	"""

    def __init__(self):
        self.size = 0
        self.root = None

    # add your fields here

    """returns whether the list is empty

	@rtype: bool
	@returns: True if the list is empty, False otherwise
	"""

    def empty(self):
        return self.root is None

    """retrieves the value of the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: index in the list
	@rtype: str
	@returns: the the value of the i'th item in the list
	"""

    def retrieve(self, i):
        return None

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
        return -1

    """deletes the i'th item in the list

	@type i: int
	@pre: 0 <= i < self.length()
	@param i: The intended index in the list to be deleted
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, i):
        return -1

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
        return None

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
        return self.root


"""Rom's and Ido's functions"""

""" tree-search method from class. """


def tree_search(x, k):
    while x is not None:
        if k == x.value:
            return x
        elif k < x.value:
            x = x.left
        else:
            x = x.right
    return x


""" tree-position method from class. """


def tree_position(x, k):
    y = None
    while x is not None:
        y = x
        if k == x.value:
            return x
        elif k < x.value:
            x = x.left
        else:
            x = x.right
    return y


"""sorted-order method from class."""


def sorted_order(x):
    if x is not None:
        sorted_order(x.left)
        print(x)
        sorted_order(x.right)


"""minimum method from class.
    @pre: x is not None"""


def minimum(x):
    while x.left is not None:
        x = x.left
    return x


"""maximum method.
    @pre: x is not None"""


def maximum(x):
    while x.right is not None:
        x = x.right
    return x


"""successor method from class.
    @inv: successor is None if and only if x.value is the largest value in the tree.
    @pre: x is not None"""


def successor(x):
    if x.right is not None:
        return minimum(x.right)
    y = x.parent
    while y is not None and x == y.right:
        x = y
        y = x.parent
    return y


"""predecessor method from class.
    @inv: predecessor is None if and only if x.value is the smallest value in the tree.
    @pre: x is not None"""


def predecessor(x):
    if x.left is not None:
        return maximum(x.right)
    y = x.parent
    while y is not None and x == y.left:
        x = y
        y = x.parent
    return y


"""tree-insert from class.
    @pre: z is not None and x is not None and z isn't in x's sub-tree"""


def tree_insert(x, z):
    y = tree_position(x, z.value)
    z.parent = y
    if z.value < y.key:
        y.left = z
    else:
        y.right = z


"""tree-delete method.
    @pre: bst is not None and z is in bst (which also means it isn't None)."""


def tree_delete(bst, z):
    y = z.parent
    if y is None:  # z is the only node in tree
        bst.root = None
        z.setVirtual()
        return
    has_two_children = z.left is not None and z.right is not None

    if not has_two_children:  # by pass or remove.
        x = None # if z is leaf.
        if z.left is None:
            x = z.right
        else: # z.right is None:
            x = z.left
        if z == y.right:
            y.right = x
        else:  # z == y.left
            y.left = x

        # for extra safety
        z.setVirtual(False)

    else:  # z has 2 children. im keeping a conservative approach and assuming we have an outside pointer to z,
        # so we can't just change z's info to be x's info.
        x = successor(z)
        tree_delete(bst, x)
        x.setVirtual(True)
        x.setLeft(z.left)
        x.setRight(z.right)
        x.setParent(z.parent)
        # TODO: need to change height as well in the future
        if z == y.left:
            y.left = x
        else:
            y.right = x




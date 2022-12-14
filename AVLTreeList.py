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
        if not self.isRealNode():
            return 0
        return self.getLeft().getHeight() - self.getRight().getHeight()

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

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.value is not None


    """returns whether self is a leaf.

        @rtype: bool
        @returns: True iff node is leaf.
        """


    def is_leaf(self):
        return self.isRealNode() and not self.left.isRealNode() and not self.right.isRealNode()

    """sets parent, left and right child of the node and updates the size, height and bf.

            @rtype: bool
            @returns: True iff node is leaf.
            """


    def new_connections(self, parent, left, right):
        self.setParent(parent)
        self.setLeft(left)
        self.setRight(right)
        self.updateSize()
        self.updateHeight()

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

    def __repr__(self):
        return str(self.root)

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
    @runtime: O(log(i)), using finger trees.
    """

    def retrieve(self, i):
        a = self.min
        while a.parent is not None and a.parent.isRealNode() and a.getSize() < i + 1:
            a = a.parent
        return tree_select(a, i + 1).getValue() if a.isRealNode() else None

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    @runtime: O(log(n))
    """

    def insert(self, i, val):
        z = insert_tree(self, i, AVLNode(val))
        ret = fix_tree(self, z)
        self.size = self.root.getSize()
        self.min = minimum(self.root)
        self.max = maximum(self.root)
        return ret

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    @runtime: O(log(n))
    """

    def delete(self, i):
        parent_of_deleted = tree_delete(self, tree_select(self.getRoot(), i + 1))
        ret = 0
        if parent_of_deleted is not None:
            ret = fix_tree(self, parent_of_deleted)
        self.size = self.root.getSize()
        if self.root.isRealNode():
            self.min = minimum(self.root)
            self.max = maximum(self.root)
        else:
            ret = -1
            self.min = self.root
            self.max = self.root

        return ret

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    @runtime: O(1)
    """

    def first(self):
        return self.min.getValue() if not self.empty() else None

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    @runtime: O(1)
    """

    def last(self):
        return self.max.getValue() if not self.empty() else None

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    @runtime: O(n)
    """

    def listToArray(self):
        return listToArray(self.root)  # the method is down below with the rest of the supporting methods.

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    @runtime: O(1)
    """

    def length(self):
        return self.size

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    @runtime: O(nlog(n))
    """

    def sort(self):
        def merge(A, B):
            """ merging two lists into a sorted list
                A and B must be sorted! """
            n = len(A)
            m = len(B)
            C = [None for i in range(n + m)]

            a = 0
            b = 0
            c = 0
            while a < n and b < m:  # more element in both A and B
                if A[a] < B[b]:
                    C[c] = A[a]
                    a += 1
                else:
                    C[c] = B[b]
                    b += 1
                c += 1

            C[c:] = A[a:] + B[b:]  # append remaining elements (one of those is empty)

            return C

        def mergesort(lst):
            """ recursive mergesort """
            n = len(lst)
            if n <= 1:
                return lst
            else:  # two recursive calls, then merge
                return merge(mergesort(lst[0:n // 2]),
                             mergesort(lst[n // 2:n]))
        lst = self.listToArray()
        lst = mergesort(lst)  # runtime is O(nlog(n)).
        lst.append(0)  # index of the current node, for fill.
        new_tree = copy(self)
        fill_tree_in_order(new_tree.root, lst)  # O(n)
        return new_tree

    """permute the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are permuted.
    @runtime: O(n)
    """

    def permutation(self):
        def shuffle(list_to_shuffle):
            for i in range(len(list_to_shuffle) - 1, 0, -1):
                # Pick a random index from 0 to i
                j = random.randint(0, i)

                # Swap arr[i] with the element at random index
                list_to_shuffle[i], list_to_shuffle[j] = list_to_shuffle[j], list_to_shuffle[i]

        if not self.root.isRealNode():
            return AVLTreeList()
        lst = self.listToArray()  # O(n)
        shuffle(lst)  # O(n).
        lst.append(0)  # index of the current node, for fill.
        new_tree = copy(self)  # O(n)
        fill_tree_in_order(new_tree.root, lst)
        return new_tree

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    @runtime: O(log(n))
    """

    def concat(self, lst):
        if lst is None or not lst.root.isRealNode():  # if other lst is empty, do nothing
            return self.root.getHeight() + 1
        elif not self.root.isRealNode():  # if this lst is empty, make it equal lst.
            self.setRoot(lst.root)
            self.min = lst.min
            self.max = lst.max
            self.size = lst.size
            return self.root.getHeight() + 1
        else:
            h1 = self.root.getHeight()
            h2 = lst.root.getHeight()
            if self.root.getHeight() <= lst.root.getHeight():
                max_in_tree = self.max
                tree_delete(self, self.max)  # O(log(n)) because of the update of max.
                join(self, max_in_tree, lst)
                self.setRoot(lst.root)
            else:
                max_in_tree = lst.max
                tree_delete(lst, lst.max)  # O(log(n)) because of the update of min.
                join(lst, max_in_tree, self)
            return abs(h1 - h2)

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    @runtime: O(n)
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


    """Rom's and Ido's functions"""


"""minimum method from class.
    @pre: x is not None and x.isRealNode()
    @runtime: O(log(n))"""


def minimum(x):
    while x.getLeft().isRealNode():
        x = x.getLeft()
    return x


"""maximum method.
    @pre: x is not None and x.isRealNode()
    @runtime: O(log(n))"""


def maximum(x):
    while x.getRight().isRealNode():
        x = x.getRight()
    return x


"""successor method from class.
    @inv: successor is None if and only if x is the largest in the tree.
    @pre: x is not None and x.isRealNode()
    @runtime: O(log(n))"""


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
    @pre: x is not None and x.isRealNode()
    @runtime: O(log(n))"""


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
    @pre: 0 <= k <= x.getSize()
    @runtime: O(log(n))"""


def tree_select(x, k):
    r = x.getLeft().getSize() + 1
    if k == r:
        return x
    elif k < r:
        return tree_select(x.getLeft(), k)
    else:
        return tree_select(x.getRight(), k - r)


"""tree-rank from class.
    @pre: x is not None and x.isRealNode()
    @runtime: O(log(n))"""


def tree_rank(x):
    r = x.getLeft().getSize() + 1
    y = x
    while y is not None and y.isRealNode():
        if y.getParent() is not None and y.getParent().isRealNode() and y == y.getParent().getRight():
            r = r + y.getParent().getLeft().getSize() + 1
        y = y.getParent()
    return r


"""insert-tree from the powerpoint representation
    @pre: bst is not None
    @pre:z is not None and z.isRealNode()
    @pre: 0 <= i < bst's size
    @return: z's parent.
    @runtime: O(log(n))"""


def insert_tree(bst, i, z):
    if i == 0:
        if bst.getRoot() is None or not bst.getRoot().isRealNode():
            bst.setRoot(z)
            return z
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
    return z.getParent()


"""tree-delete method. returns the parent of the physically deleted node
    @pre: bst is not None and z is in bst
    @pre: z is not None and z.isRealNode()
    @rtype: AVLNode
    @return: the parent of the node deleted.
    @runtime: O(log(n))"""


def tree_delete(bst, z):
    if z == bst.getRoot() and z.is_leaf():
        bst.setRoot(AVLNode(None))  # make the root a virtual node, which means there are no nodes in the tree.
        bst.min = AVLNode(None)
        bst.max = AVLNode(None)
        bst.size = 0
        return None
    y = z.getParent()
    if z.is_leaf():
        # z is not a root for certain
        if z == y.getRight():
            y.setRight(AVLNode(None))
        if z == y.getLeft():
            y.setLeft(AVLNode(None))
        z.new_connections(None, AVLNode(None), AVLNode(None))
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
        z.new_connections(None, AVLNode(None), AVLNode(None))
    else:  # z has 2 children.
        x = successor(z)
        val = x.getValue()
        y = tree_delete(bst, x)  # z's successor has no left child, so the returned value will be x's parent for sure
        z.setValue(val)
    return y


"""listToArray method, converts an avl tree into a list
    @pre: node is not None
    @runtime: O(n)"""


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
    @pre: lst's size - index is the node's sub-tree size
    @runtime: O(n)"""


def fill_tree_in_order(node, lst):
    if not node.isRealNode():
        return
    elif node.is_leaf():
        node.setValue(lst[lst[len(lst) - 1]])
        lst[len(lst) - 1] += 1
    else:
        fill_tree_in_order(node.getLeft(), lst)
        node.setValue(lst[lst[len(lst) - 1]])
        lst[len(lst) - 1] += 1
        fill_tree_in_order(node.getRight(), lst)


"""search_tree method, looks for a value in the tree
    @pre: val is a string
    @rtype: int
    @runtime: O(h + n) where h is the height of node"""


def search_tree(node, val):
    if node is None or not node.isRealNode():
        return -1
    return tree_rank(node) - 1 if node.getValue() == val else search_tree(successor(node), val)


"""fix_tree method fixes nodes from inputted node up until the root, returns the number of rotations
    @pre: node is not None
    @rtype: int
    @runtime: O(log(n))"""


def fix_tree(bst, x):
    counter = 0
    y = x
    while y is not None and y.isRealNode():  # continue until we reach root
        y.setHeight(1 + max(y.getLeft().getHeight(), y.getRight().getHeight()))
        y.setSize(y.getRight().getSize() + y.getLeft().getSize() + 1)
        balance = y.getBF()
        if abs(balance) < 2:
            y = y.getParent()
        else:  # meaning abs(balance) == 2
            if balance == 2:
                if y.getLeft().getBF() > -1:
                    right_rotate(y)
                    counter += 1
                else:
                    left_rotate(y.getLeft())
                    right_rotate(y)
                    counter += 2
            elif balance == -2:  # meaning balance = -2
                if y.getRight().getBF() < 1:
                    left_rotate(y)
                    counter += 1
                else:
                    right_rotate(y.getRight())
                    left_rotate(y)
                    counter += 2
            if abs(y.getBF()) >= 2:
                print(y.getBF(), str(y), y.getLeft().getHeight(), y.getRight().getHeight())
            y.updateHeight()
            y.updateSize()
            y = y.getParent()

    if bst.root.isRealNode():
        y = bst.root
        while y.getParent() is not None and y.getParent().isRealNode():
            y = y.getParent()
    bst.setRoot(y)

    y = x  # updating sizes and heights if needed, to be sure.
    while y is not None:
        y.updateSize()
        y.updateHeight()
        y = y.getParent()
    return counter


"""left_rotate method rotates the inputted node and its children to the left, and updates their height and size accordingly
    @pre: x is not None
    @pre: x is an AVLNode
    @runtime: O(1)"""


def left_rotate(x):
    y = x.getRight()

    # updating the pointers
    x.setRight(y.getLeft())
    x.getRight().setParent(x)
    y.setLeft(x)
    y.setParent(x.getParent())
    if x.getParent() is not None:
        if x.getParent().getRight() == x:
            x.getParent().setRight(y)
        else:
            x.getParent().setLeft(y)
    x.setParent(y)

    # updating heights and size
    x.updateHeight()
    y.updateHeight()
    y.setSize(x.getSize())
    x.updateSize()


"""left_rotate method rotates the inputted node and its children to the left, and updates their height and size accordingly
    @pre: x is not None
    @pre: x is an AVLNode
    @runtime: O(1)"""


def right_rotate(x):
    y = x.getLeft()

    # updating the pointers
    x.setLeft(y.getRight())
    x.getLeft().setParent(x)
    y.setRight(x)
    y.setParent(x.getParent())
    if x.getParent() is not None:
        if x.getParent().getRight() == x:
            x.getParent().setRight(y)
        else:
            x.getParent().setLeft(y)
    x.setParent(y)

    # updating heights and size
    x.updateHeight()
    y.updateHeight()
    y.setSize(x.getSize())
    x.updateSize()


"""copy creates and returns a new AVLTreeList with the same structure as the inputted AVLTreeList
    @rtype: AVLTreeList
    @returns: a copy of the original AVLTreeList
    @runtime: O(n)"""


def copy(self):
    head = copy_rec(self.root)
    ret = AVLTreeList()
    ret.root = head
    ret.size = ret.root.size
    ret.min = minimum(ret.root) if ret.root.isRealNode() else AVLNode(None)
    ret.max = maximum(ret.root) if ret.root.isRealNode() else AVLNode(None)
    return ret


"""copy_rec copies and returns the root of the copied AVLTreeList
    @rtype: AVLNode
    @runtime: O(n)"""


def copy_rec(node):
    if not node.isRealNode():
        return AVLNode(None)

    node_copy = AVLNode(node.value)
    node_copy.setParent(node.getParent())

    node_copy.right = copy_rec(node.right)
    if node.right.isRealNode():
        node_copy.right.setParent(node_copy)
    node_copy.left = copy_rec(node.left)
    if node.left.isRealNode():
        node_copy.left.setParent(node_copy)

    node_copy.height = node.height
    node_copy.size = node.size

    return node_copy


"""join method from class.
    @pre: t1.length >= 1
    @pre: t2.length >= 1
    @pre: height(t1) <= height(t2)
    @pre: x isn't in t1 or t2.
    @runtime: O(log(n))"""


def join(t1, x, t2):
    b = t2.min
    while b.parent is not None and b.parent.getHeight() <= t1.getRoot().getHeight():
        b = b.getParent()
    x.setLeft(t1.getRoot())
    x.setRight(b)
    c = b.getParent()
    if c is not None:
        c.new_connections(c.getParent(), x, c.getRight())
    fix_tree(t2, x)

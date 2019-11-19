import unittest


class Node:
    def __init__(self, key):
        self.left: Node = None
        self.right: Node = None
        self.key: int = key


class BST:
    """ Binary Search Tree.
    """

    def __init__(self):
        self.root: Node = None

    def insert(self, key: int):
        """ Inserts the given key into the BST.
        """
        new = Node(key)
        if self.root is None:
            self.root = new
        else:
            placed = False
            temp = self.root
            while not placed:
                if key < temp.key:
                    if temp.left is None:
                        temp.left = new
                        placed = True
                    else:
                        temp = temp.left
                elif key > temp.key:
                    if temp.right is None:
                        temp.right = new
                        placed = True
                    else:
                        temp = temp.right

    def remove(self, key: int):
        """ Remove the given key from the BST.
        """
        self._remove(self.root, key, False)

    def _remove(self, node: Node, key: int, found: bool):
        if node.key != key and not found:
            if key > node.key:
                self._remove(node.right, key, found)
                if node.right.key == key:
                    node.right = None
                return
            elif key < node.key:
                self._remove(node.left, key, found)
                if node.left.key == key:
                    node.left = None
                return
        if node.key == key:
            found = True
            children = self._numberOfChildren(node)
            if children == 0:
                node = None
            elif children == 1:
                if node.right is not None:
                    node.key = node.right.key
                    node.left = node.right.left
                    node.right = node.right.right
                elif node.left is not None:
                    node.key = node.left.key
                    node.right = node.left.right
                    node.left = node.left.left
            elif children == 2:
                this_node = node.left
                if this_node.right is not None:
                    while this_node.right.right is not None:
                        this_node = this_node.right
                if this_node.right is None:
                    node.key = this_node.key
                    node.left = this_node.left
                else:
                    node.key = this_node.right.key
                    if this_node.right.left is not None:
                        this_node.right = this_node.right.left
                    else:
                        this_node.right = None
            return

    def _numberOfChildren(self, node: Node):
        if node.left is not None and node.right is not None:
            return 2
        elif node.left is None and node.right is None:
            return 0
        else:
            return 1

    def populate(self, A: list):
        """ Creates a tree from the elements in A.
        """
        for i in range(len(A)):
            self.insert(A[i])

    def inorder(self):
        """ Performs an inorder traversal of the BST, printing each element.
        """
        self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return
        else:
            self._inorder(node.left)
            print(node.key)
            self._inorder(node.right)
            return

    def preorder(self):
        """ Performs a preorder traversal of the BST, printing each element.
        """
        self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return
        else:
            print(node.key)
            self._preorder(node.left)
            self._preorder(node.right)

    def postorder(self):
        """ Performs a postorder traversal of the BST, printing each element.
        """
        self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return
        else:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.key)

    def search(self, key: int) -> bool:
        """ Returns whether or not the given key is in the BST.
        """
        return self._search(key, self.root)

    def _search(self, key: int, node) -> bool:
        if node is None:
            return False
        elif node.key == key:
            return True
        else:
            if key < node.key:
                return self._search(key, node.left)
            elif key > node.key:
                return self._search(key, node.right)

    def height(self) -> int:
        """ Returns the height of the BST.
        """
        return self._height(self.root, 0)

    def _height(self, node: Node, max_height: int) -> int:
        if node.left is None and node.right is None:
            return max_height
        elif self._numberOfChildren(node) == 2:
            left_height = self._height(node.left, max_height + 1)
            right_height = self._height(node.right, max_height + 1)
            if left_height > right_height:
                return left_height
            else:
                return right_height
        elif self._numberOfChildren(node) == 1:
            if node.left is not None:
                return self._height(node.left, max_height + 1)
            elif node.right is not None:
                return self._height(node.right, max_height + 1)


class Tests(unittest.TestCase):

    def test_insert(self):
        tree = BST()
        self.assertEqual(tree.root, None)
        tree.insert(10)
        self.assertEqual(tree.root.key, 10)
        tree.insert(15)
        self.assertEqual(tree.root.key, 10)
        return

    def test_populate(self):
        tree = BST()
        arr = [5, 3, 7, 9, 2, 1, 6, 0, 4, 8]
        tree.populate(arr)
        self.assertEqual(tree.root.key, 5)
        self.assertEqual(tree.root.left.key, 3)
        self.assertEqual(tree.root.right.key, 7)
        self.assertEqual(tree.root.right.right.key, 9)
        self.assertEqual(tree.root.left.left.key, 2)
        self.assertEqual(tree.root.left.left.left.key, 1)
        self.assertEqual(tree.root.right.left.key, 6)
        self.assertEqual(tree.root.left.left.left.left.key, 0)
        self.assertEqual(tree.root.left.right.key, 4)
        self.assertEqual(tree.root.right.right.left.key, 8)

    def test_inOrder(self):
        tree = BST()
        arr = [5, 3, 7, 9, 2, 1, 6, 0, 4, 8]
        tree.populate(arr)
        tree.inorder()

    def test_search(self):
        tree = BST()
        arr = [5, 3, 7, 9, 2, 1, 6, 0, 4, 8]
        tree.populate(arr)
        self.assertTrue(tree.search(9))
        self.assertFalse(tree.search(10))

    def test_remove(self):
        # remove node with no children
        tree = BST()
        arr = [5, 3, 7, 9, 2, 1, 6, 0, 4, 8]
        tree.populate(arr)
        self.assertTrue(tree.search(8))
        tree.remove(8)
        for i in range(10):
            if i != 8:
                self.assertTrue(tree.search(i))
        self.assertFalse(tree.search(8))

        # remove node with one child
        tree = BST()
        arr = [5, 3, 7, 9, 2, 1, 6, 0, 4, 8]
        tree.populate(arr)
        self.assertTrue(tree.search(1))
        tree.remove(1)
        for i in range(10):
            if i != 1:
                self.assertTrue(tree.search(i))
        self.assertFalse(tree.search(1))

        # remove node with two children
        tree = BST()
        arr = [5, 3, 7, 9, 2, 1, 6, 0, 4, 8]
        tree.populate(arr)
        self.assertTrue(tree.search(3))
        tree.remove(3)
        for i in range(10):
            if i != 3:
                self.assertTrue(tree.search(i))
        self.assertFalse(tree.search(3))

    def test_height(self):
        tree = BST()
        arr = [5, 3, 7, 9, 2, 1, 6, 0, 4, 8]
        tree.populate(arr)
        self.assertEqual(tree.height(), 4)

# breadth first search: think bacterial propagation
# depth first search: think maze solver

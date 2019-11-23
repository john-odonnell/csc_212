import sys
import unittest


class Node:
    def __init__(self, key):
        self.left: Node = None
        self.right: Node = None
        self.key: str = key
        self.count: int = 1


class BST:
    """ Binary Search Tree.
    """

    def __init__(self):
        self.root: Node = None
        self.unique_words: int = 0
        self.total_words: int = 0
        self.most_frequent: Node = None

    def insert(self, key: str):
        """ Inserts the given key into the BST.
        """
        key = toLower(removePunctuation(key))
        if len(key) < 1:
            return
        new = Node(key)
        if self.root is None:
            self.root = new
            self.most_frequent = new
        else:
            placed = False
            temp = self.root
            while not placed:
                if key < temp.key:
                    if temp.left is None:
                        temp.left = new
                        placed = True
                        self.unique_words += 1
                        self.total_words += 1
                    else:
                        temp = temp.left
                elif key > temp.key:
                    if temp.right is None:
                        temp.right = new
                        placed = True
                        self.unique_words += 1
                        self.total_words += 1
                    else:
                        temp = temp.right
                elif key == temp.key:
                    temp.count += 1
                    placed = True
                    self.total_words += 1

                if placed:
                    if new.count > self.most_frequent.count:
                        self.most_frequent = new

    def remove(self, key: str):
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


def removePunctuation(s: str) -> str:
    """ Removes non-alphanumeric characters.
    """
    new = ""
    for i in range(len(s)):
        if s[i].isalnum():
            new += s[i]
    return new


def toLower(s: str) -> str:
    """ Convert the string to lowercase, in place.
    """
    return s.lower()


class Tests(unittest.TestCase):

    def test_removepun(self):
        tree = BST()
        tree.insert("goodday....")
        self.assertEqual(tree.root.key, "goodday")


def main(filename):
    """ Main.
    """
    # Open the file, and store its contents as a list,
    # where each element is a line from the file
    with open(filename, 'r') as f:
    # with open("pride.txt", "r") as f:
        story = f.readlines()

    book = BST()
    for line in story:
        line = line.strip().split()
        for word in line:
            book.insert(word)

    print("Height           . " + str(book.height()))
    print("Total Words      . " + str(book.total_words))
    print("Unique Words     . " + str(book.unique_words))
    print("Most frequent    . " + str(book.most_frequent.key) + " - " + str(book.most_frequent.count))
    return


if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    main(filename=args.filename)
    # main()

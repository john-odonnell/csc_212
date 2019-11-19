class bstNode:
    def __init__(self, value=0, parent=None, left=None, right=None):
        self.value: int = value
        self.parent: bstNode = parent
        self.left: bstNode = left
        self.right: bstNode = right


class binaryTree:
    def __init__(self):
        self.root: bstNode = None
        self.current: bstNode = None
        self.numNodes: int = 0

    def addElement(self, data: int):
        new = bstNode(data)
        if self.root is None:
            self.root = new
        else:
            self.current = self.root
            last = None
            placed = False
            while not placed:
                last = self.current
                if self.current.left is None and data < self.current.value:
                    self.current.left = new
                    placed = True
                elif self.current.right is None and data > self.current.value:
                    self.current.right = new
                    placed = True
                elif self.current.left is not None and data < self.current.value:
                    self.current = self.current.left
                elif self.current.right is not None and data > self.current.value:
                    self.current = self.current.right
            new.parent = self.current
        self.numNodes += 1

    def removeElement(self, data: int):
        # case 1: no children -> remove
        # case 2: one child -> replace with child
        # case 3: two children -> replace with predecessor

        # get to node
        self.current = self.root
        while self.current is not None and self.current.value != data:
            if data < self.current.value:
                self.current = self.current.left
            elif data > self.current.value:
                self.current = self.current.right
        if self.current is None:
            print("Element not found in BST")
        else:
            if self.current.left is None and self.current.right is None:
                if self.current.parent.left == self.current:
                    self.current.parent.left = None
                elif self.current.parent.right == self.current:
                    self.current.parent.right = None
                self.current.parent = None
            elif self.current.left is not None and self.current.right is not None:
                parent = self.current.parent
                to_replace = self.current
                left = self.current.left
                right = self.current.right
                self.current = self.current.left
                while self.current.right is not None:
                    self.current = self.current.right
                if to_replace != self.root:
                    if parent.right == to_replace:
                        parent.right = self.current
                    elif parent.left == to_replace:
                        parent.left = self.current
                else:
                    self.root = self.current
                if self.current.parent.right == self.current:
                    self.current.parent.right = None
                elif self.current.parent.left == self.current:
                    self.current.parent.left = None
                self.current.left = left
                self.current.right = right
            else:
                if self.current.left is not None:
                    if self.current.parent.left == self.curret:
                        self.current.parent.left = self.current.left
                    elif self.current.parent.right == self.current:
                        self.current.parent.right = self.current.left
                elif self.current.right is not None:
                    if self.current.parent.left == self.current:
                        self.current.parent.left = self.current.right
                    elif self.current.parent.right == self.current:
                        self.current.parent.right = self.current.right
                self.current.parent = None
        self.numNodes -= 1

    def printTree(self, node: bstNode):
        if node is None:
            return
        else:
            print(node.value)
            self.printTree(node.left)
            self.printTree(node.right)


def main():
    bst = binaryTree()
    data = [5, 2, 8, 3, 6, 4, 9, 0, 1, 7]
    for i in range(len(data)):
        bst.addElement(data[i])

    print(str(bst.root.value) + " " + str(bst.numNodes))
    bst.printTree(bst.root)

    print("\n")

    bst.removeElement(7)
    print(str(bst.root.value) + " " + str(bst.numNodes))
    bst.printTree(bst.root)

    print("\n")

    bst.removeElement(0)
    print(str(bst.root.value) + " " + str(bst.numNodes))
    bst.printTree(bst.root)

    print("\n")

    bst.removeElement(5)
    print(str(bst.root.value) + " " + str(bst.numNodes))
    bst.printTree(bst.root)


main()

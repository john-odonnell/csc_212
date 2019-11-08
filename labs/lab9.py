import unittest


class Node:
    ''' Holds data and a reference to the next Node.
    '''

    def __init__(self, data=None):
        '''The constructor for the Node class'''
        self.data: int = data
        self.next: Node = None


class LinkedList:
    ''' Holds a list of Nodes.
    '''

    def __init__(self):
        '''The constructor for the linked list class.

        This function records the head and tail of the list.
        It also records the number of elements in the list
        '''
        self.head: Node = None
        self.tail: Node = None
        self.current: Node = None
        self.n_elem: int = 0

    def __del__(self):
        '''The destructor for the linked list class.

        This function will clear all the nodes within the list
        before it deletes itself
        '''
        self.clear()

    def __iter__(self):
        temp = self.head
        for _ in range(self.n_elem):
            yield temp
            temp = temp.next

    def append(self, data: int) -> None:
        '''Add a new node to the end of the linked list'''
        this_node = Node(data)
        if self.n_elem == 0:
            self.head = this_node
        else:
            self.tail.next = this_node
        self.tail = this_node
        self.n_elem += 1

    def prepend(self, data: int) -> None:
        '''Add a new node to the beginning of the list'''
        this_node = Node(data)
        if self.n_elem == 0:
            self.head = this_node
            self.tail = this_node
        else:
            this_node.next = self.head
            self.head = this_node
        self.n_elem += 1

    def insertAt(self, index: int, data: int) -> None:
        '''Insert a node a specific index'''
        this_node = Node(data)
        if index == 0:
            this_node.next = self.head
            self.head = this_node
        elif index > self.n_elem - 1:
            self.append(data)
        else:
            self.current = self.head
            for i in range(0, index):
                self.current = self.current.next
            this_node.next = self.current.next
            self.current.next = this_node
        if self.current == self.tail:
            self.tail = this_node
        self.n_elem += 1

    def removeAt(self, index: int) -> int:
        '''Removes a node at a specific index and returns its data
        '''
        self.current = self.head
        for i in range(0, index - 1):
            self.current = self.current.next
        data = self.current.next.data
        self.current.next = self.current.next.next
        return data

    def removeLast(self) -> int:
        '''Removes the last node of the list and returns its data
        '''
        data = self.tail.data
        self.current = self.head
        for i in range(self.n_elem - 2):
            self.current = self.current.next
        if self.current.next == self.tail:
            self.current.next = None
        self.tail = self.current
        self.n_elem -= 1
        return data

    def removeFirst(self) -> int:
        '''Removes the first node of the list and returns its data
        '''
        data = self.head.data
        self.head = self.head.next
        self.n_elem -= 1
        return data

    def getSize(self) -> int:
        '''Return the number of elements in the list'''
        n_elements = 0;
        self.current = self.head
        while self.current.next is not None:
            n_elements += 1
            self.current = self.current.next
        return n_elements

    def clear(self) -> None:
        '''Clear the entire list.

        Hint: Python uses garbage collection
        '''
        self.head = self.current = self.tail = None

    def find(self, data: int) -> bool:
        '''Returns True if the data is in the list, False otherwise'''
        # TODO
        pass

    def print(self) -> None:
        '''Prints the whole list.'''
        temp = self.head
        for i in range(self.n_elem):
            print(i, ':', temp.data)
            temp = temp.next


class Tests(unittest.TestCase):

    def test_append(self):
        ll = LinkedList()
        for i in range(10):
            ll.append(i)

        temp = ll.head
        for i in range(10):
            self.assertEqual(temp.data, i)
            temp = temp.next

    def test_prepend(self):
        ll = LinkedList()
        for i in range(10):
            ll.prepend(i)

        temp = ll.head
        i = 9
        while i >= 0:
            self.assertEqual(temp.data, i)
            temp = temp.next
            i -= 1

    def test_insertAt(self):
        ll = LinkedList()
        for i in range(10):
            ll.append(i)
        index = 5
        data = 10
        ll.insertAt(index, data)
        ll.current = ll.head
        for i in range(0, index + 1):
            ll.current = ll.current.next
        self.assertEqual(ll.current.data, data)

        ll = LinkedList()
        for i in range(10):
            ll.append(i)
        index = 12
        data = 10
        ll.insertAt(index, data)
        self.assertEqual(ll.tail.data, data)

        ll = LinkedList()
        for i in range(10):
            ll.append(i)
        index = 0
        data = 10
        ll.insertAt(index, data)
        self.assertEqual(ll.head.data, data)

    def test_removeFirst(self):
        ll = LinkedList()
        ll2 = LinkedList()
        for i in range(10):
            ll.append(i)
            if i != 0:
                ll2.append(i)

        ll.removeFirst()

        ll.current = ll.head
        ll2.current = ll2.head
        for i in range(9):
            self.assertEqual(ll.current.data, ll2.current.data)
            ll.current = ll.current.next
            ll2.current = ll2.current.next

    def test_removeLast(self):
        ll = LinkedList()
        for i in range(10):
            ll.append(i)

        ll.removeLast()

        ll.current = ll.tail
        self.assertEqual(ll.current.data, 8)

    def test_removeAt(self):
        ll = LinkedList()
        ll2 = LinkedList()
        for i in range(10):
            ll.append(i)
            if i != 5:
                ll.append(i)

        index = 5
        ll.removeAt(index)

        ll.current = ll.head
        ll2.current = ll2.head
        for i in range(9):
            self.assertEqual(ll.current.data, ll2.current.data)
            ll.current = ll.current.next
            ll2.current = ll2.current.next



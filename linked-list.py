class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    def _get_data(self):
        return self.data

    def _get_next(self):
        return self.next

    def _set_data(self, data):
        self.data = data

    def _set_next(self, data):
        self.next = data


class LinkedList:

    def __init__(self):
        self.head = None
    
    def _add(self, data):
        self.head = Node(data, self.head)

    def _delete(self, prev, node):
        if not prev:
            self.head = node.next
        else:
            prev.next = node.next

    def _delete_node(self, index):
        node, prev, i = self._find(index)

        if index == i:
            self._delete(prev, node)
        else:
            print("Node with index {} not found".format(index))

    def _is_empty(self):
        return self.head == None

    def _size(self):
        current = self.head
        count = 0

        while current != None:
            count = count + 1
            current = current.get_next()

        return count

    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1
        return node, prev, i

    def _get_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next


def main():
    print("=== Linked List - An ordered set of data elements, each containing a link to its successor")

    ll = LinkedList()

    for i in range (1, 10):
        ll._add(i)

    print("The list is: ")
    ll._get_list()

    data = input("[INT, 0 to exit] What index you want to delete? ")

    while data != 0:
        ll._delete_node(data)
        ll._get_list()    
        data = input('[INT, 0 to exit] What index you want to delete? ')

    print("The list after deleting node with index: ")
    ll._get_list()


if __name__=='__main__':
	main()
class Node:

    def __init__(self, label):
        self.label = label
        self.left = None
        self.rigt = None
        self.parent = None
        self.height = 0

    def _get_label(self):
        return self.label

    def _set_label(self, label):
        self.label = label

    def _get_left(self):
        return self.left

    def _set_left(self, left):
        self.left = left

    def _get_right(self):
        return self.rigt

    def _set_right(self, right):
        self.rigt = right

    def _get_parent(self):
        return self.parent

    def _set_parent(self, parent):
        self.parent = parent

    def _set_height(self, height):
        self.height = height

    def _get_height(self, height):
        return self.height


class AVL:

    def __init__(self):
        self.root = None
        self.size = 0

    def _insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            self.size = 1
        else:
            # Same as Binary Tree
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node is not None:

                    dad_node = curr_node

                    if node._get_label() < curr_node._get_label():
                        curr_node = curr_node._get_left()
                    else:
                        curr_node = curr_node._get_right()
                else:
                    if node._get_label() < dad_node._get_label():
                        dad_node._set_left(node)
                        dad_node._set_height(dad_node._get_height() + 1)

                        if (dad_node._get_right()._get_height() -
                                dad_node._get_left._get_height() > 1):
                            self.rebalance(dad_node)

                    else:
                        dad_node._set_right(node)
                        dad_node._set_height(dad_node._get_height() + 1)

                        if (dad_node._get_right()._get_height() -
                                dad_node._get_left._get_height() > 1):
                            self.rebalance(dad_node)
                    break

    def _rebalance(self, node):
        if (node._get_right()._get_height() -
                node._get_left._get_height() > 1):
            if (node._get_right()._get_height() >
                    node._get_left._get_height()):
                pass
            else:
                pass
            pass
        elif (node._get_right()._get_height() -
                node._get_left._get_height() > 2):
            if (node._get_right()._get_height() >
                    node._get_left._get_height()):
                pass
            else:
                pass
            pass
        pass

    def _rotate_left(self, node):
        aux = node._get_label()
        node = aux._get_right()
        node._set_height(node._get_height() - 1)
        node._set_left(Node(aux))
        node._get_left()._set_height(node._get_height() + 1)
        node._get_right()._set_height(node._get_right()._get_height() - 1)

    def _rotate_right(self, node):
        aux = node._get_label()
        node = aux._get_left()
        node._set_height(node._get_height() - 1)
        node._set_right(Node(aux))
        node._get_left()._set_height(node._get_height() + 1)
        node._get_left()._set_height(node._get_left()._get_height() - 1)

    def _double_rotate_left(self, node):
        self.rotate_right(node._get_right()._get_right())
        self.rotate_left(node)

    def _double_rotate_right(self, node):
        self.rotate_left(node._get_left()._get_left())
        self.rotate_right(node)


def main():
    print("=== AVL Tree - A Self-balancing binary search tree by rotating the nodes")

if __name__=='__main__':
	main()
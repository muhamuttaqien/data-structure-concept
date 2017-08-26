class Node():

    def __init__(self, item=None):
        self.item = item
        self.left = None
        self.right = None

    def _add(self, data):
        new_node = Node(data)

        if not self.item:
            self.item = new_node
        else:
            if data > self.item:
                self.right = self.right and self.right._add(data) or new_node
            elif data < self.item:
                self.left = self.left and self.left._add(data) or new_node
            else:
                print("BSTs do not support repeated items.")

        return self

    def _search(self, data):
        if self.item == data:
            return True
        elif self.left and data < self.item:
            return self.left._search(data)
        elif self.right and data > self.item:
            return self.right._search(data)
        else:
            return False
    
    def _is_leaf(self):
        return not self.right and not self.left

    def _print_pre_order(self):
        print self.item

        if self.left:
            self.left._print_pre_order()

    def _pre_order_array(self):
        nodes = []

        if self.item:
            nodes.append(self.item)
        if self.left:
            nodes.extend(self.left._pre_order_array())
        if self.right:
            nodes.extend(self.right._pre_order_array())

        return nodes


class BST():

    def __init__(self):
        self.root = None

    def _add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.root._add(data)

    def _get_pre_order(self):
        if self.root:
            self.root._get_pre_order()

    def _search(self, data):
        if self.root:
            return self.root._search(data)

    def _pre_order_array(self):
        if self.root:
            return self.root._pre_order_array()
        else:
            return "Tree is empty."


def pre_order(tree, nodes=None):
    nodes = nodes or []
    if tree:
        nodes.append(tree.item)
        if tree.left:
            pre_order(tree.left, nodes)
        if tree.right:
            pre_order(tree.right, nodes)

    return nodes

def post_order(tree, nodes=None):
    nodes = nodes or []
    if tree:
        if tree.left:
            nodes = post_order(tree.left, nodes)
        if tree.right:
            nodes = post_order(tree.right, nodes)
        nodes.append(tree.item)

    return nodes

def in_order(tree, nodes=None):
    nodes = nodes or []
    if tree:
        if tree.left:
            nodes = in_order(tree.left, nodes)
        
        nodes.append(tree.item)
        if tree.right:
            nodes = in_order(tree.right, nodes)

    return nodes


def main():
    print("=== Binary Tree - A data structure in which a record is linked to two successor records, usually referred to as the left branch when less and the right when greater than the previous record")

    bst = BST()

    data = [10, 5, 6, 3, 8, 2, 1, 11, 9, 4]

    for datum in data:
        bst._add(datum)

    print("Searching for nodes 16 and 6:")
    print(bst._search(16))
    print(bst._search(6))


    print("Preorder: {}".format(pre_order(bst.root)))
    print("Postorder: {}".format(post_order(bst.root)))
    print("Inorder: {}".format(in_order(bst.root)))
    print("Preorder: {}".format(pre_order(bst.root)))


if __name__=='__main__':
	main()
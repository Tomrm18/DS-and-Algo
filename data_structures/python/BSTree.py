# Python implementation of a Binary Search Tree

import collections


class BSTNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BSTree():
    def __init__(self):
        self.root = None

    def print(self):
        # defaults to preorder print
        self.levelOrder(self.root)

    # depth first search
    # recursion solution
    def preOrder(self, root):
        if root:
            # visits the current node
            # then any left
            # then right if no left child available
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    # depth first search
    # recursion solution
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)

    # depth first search
    # recursive solution
    def postOrder(self, root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.data)

    # breath first search
    # iterative solution
    def levelOrder(self, root):
        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queueLength = len(queue)
            level = []

            for i in range(queueLength):
                node = queue.popleft()

                if node:
                    level.append(node.data)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                result.append(level)

        print(result)
        return result

    def add(self, data):
        if self.root:
            self.insert(self.root, data)
        else:
            self.root = BSTNode(data)

    def insert(self, node, data):
        if not node or data == node.data:
            return None

        if data < node.data:
            if not node.left:
                node.left = BSTNode(data)
            else:
                self.insert(node.left, data)

        if data > node.data:
            if not node.right:
                node.right = BSTNode(data)
            else:
                self.insert(node.right, data)

    def remove(self, data):
        if not self.root:
            return

        return self.removeValue(self.root, data)

    def removeValue(self, node, data):
        if not node:
            return None

        if node.data == data:

            if not node.right:
                return node.left

            if not node.left:
                return node.right

            if node.left and node.right:
                temp = node.right

                while temp.left:
                    temp = temp.left
                    node.data = temp.data
                    node.right = self.removeValue(node.right, node.data)

        elif data < node.data:
            node.left = self.removeValue(node.left, data)
        else:
            node.right = self.removeValue(node.right, data)

        return node


tree = BSTree()
tree.root = BSTNode(0)
tree.add(1)
tree.add(-1)
tree.add(-5)
tree.add(3)
tree.remove(-5)

tree.print()

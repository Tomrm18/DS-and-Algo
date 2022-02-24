# Python implementation of a binary tree
import collections


class BTreeNode():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree():
    def __init__(self):
        self.root = None

    # also sometimes called height
    # results may vary depending on if question requires
    # root node to be counted as 0 or 1
    # default is 0
    def maxDepth(self):
        depth = self.depth(self.root)
        print(depth)
        return depth

    def depth(self, root):
        if not root:
            return -1
        return 1 + max(self.depth(root.left), self.depth(root.right))

    def invert(self):
        self.root = self.invertTree(self.root)

    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = self.invertTree(
            root.right), self.invertTree(root.left)

        return root

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

# returns True if two trees are the same
# False otherwise


def compareTrees(node1, node2):
    if not node1 and not node2:
        return True

    if not node1 or not node2:
        return False

    if node1.data != node2.data:
        return False

    return (compareTrees(node1.left, node2.left) and compareTrees(node1.right, node2.right))


def mergeTrees(tree1, tree2):
    mergedTree = BTree()
    mergedTree.root = merge(tree1.root, tree2.root)
    return mergedTree


def merge(node1, node2):
    if not node1 and not node2:
        return None

    # extracting the value from each node
    # if null, defaults to 0
    val1 = node1.data if node1 else 0
    val2 = node2.data if node2 else 0

    root = BTreeNode(val1 + val2)

    root.left = merge(node1.left if node1 else None,
                      node2.left if node2 else None)

    root.right = merge(node1.right if node1 else None,
                       node2.right if node2 else None)

    return root


tree = BTree()
tree.root = BTreeNode(1)
tree.root.left = BTreeNode(2)
tree.root.right = BTreeNode(3)


tree.print()
tree.invert()
tree.print()

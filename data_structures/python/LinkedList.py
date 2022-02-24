class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = Node()

    def add_to_head(self, item):
        if self.head.data is None:
            self.head.data = item
        else:
            newNode = Node(item)
            temp = self.head
            self.head = newNode
            self.head.next = temp

    def add_to_tail(self, item):
        if self.head is None:
            self.add_to_head(item)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(item)

    def remove_from_head(self):
        self.head = self.head.next

    def remove_from_tail(self):
        prev = None
        temp = self.head

        while temp.next is not None:
            prev = temp
            temp = temp.next

        prev.next = None

    def insert(self, item, index):
        if self.head is None or index == 0:
            self.add_to_head(item)
        else:
            newNode = Node(item)
            temp = self.head
            prev = None
            count = 0

            while temp is not None:
                # if we have reached the node

                if (count == index):
                    prev.next = newNode
                    newNode.next = temp
                    return

                count += 1
                prev = temp
                temp = temp.next

            # if we reached this line then the index is out of bounds
            # so we just add the item to the lists tail
            self.add_to_tail(item)

    def deleteIndex(self, index):
        if index == 0:
            self.remove_from_head()
        else:
            temp = self.head
            prev = None
            count = 0

            while temp is not None:

                if count == index:
                    # need to check if the node is the tail
                    if temp.next is None:
                        self.remove_from_tail()
                    # node is not tail
                    else:
                        prev.next = temp.next
                        temp = None
                    return

                count += 1
                prev = temp
                temp = temp.next

    # delays result pointer until
    # current pointer has moved through positionFromTail number of nodes
    # so that may when current hits the tail,
    # the result pointer will be positionFromTail away from the tail
    def getNodeFromTail(self, positionFromTail):
        index = 0
        current = self.head
        result = self.head

        while current:
            current = current.next

            if index > positionFromTail:
                result = result.next
            index += 1
        return result.data

    # sorts the list
    def sort(self):
        # self.slowSort()
        self.head = self.mergeSort(self.head)

    def mergeSort(self, head):
        if not head or not head.next:
            return head

        middle = self.getMiddle(head)
        afterMiddle = middle.next

        middle.next = None

        left = self.mergeSort(head)

        right = self.mergeSort(afterMiddle)

        sortedList = self.sortedMerge(left, right)
        return sortedList

    def sortedMerge(self, left, right):
        result = None

        # if left is None return right
        # if right is None return left
        if not left:
            return right
        if not right:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sortedMerge(left.next, right)
        else:
            result = right
            result.next = self.sortedMerge(left, right.next)
        return result

    # fast moves up 2 nodes
    # slow moves up 1 node
    # effectively, when fast arrives at the end of the list,
    # slow will be at or near the middle
    def getMiddle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        # while there are still 2 nodes after fast
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # n^2 approach

    def slowSort(self):

        current = self.head
        temp = None
        index = None

        while current:
            index = current.next

            while index:
                if current.data > index.data:
                    temp = current.data
                    current.data = index.data
                    index.data = temp

                index = index.next

            current = current.next

    def reverse(self):
        prev = None
        temp = self.head

        while temp is not None:
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        self.head = prev

    def print(self):
        temp = self.head
        while self.head is not None:
            print(self.head.data)
            self.head = self.head.next
        self.head = temp

    def reversePrint(self):
        if self.head:
            self.reversePrintRecur(self.head.next)
            print(self.head.data)
        else:
            return

    def reversePrintRecur(self, temp):
        if temp:
            self.reversePrintRecur(temp.next)
            print(temp.data)
        else:
            return

    # list must already be sorted
    def removeDuplicates(self):
        if self.head:
            temp = self.head

            while temp.next:
                if temp.data == temp.next.data:
                    temp.next = temp.next.next
                else:
                    temp = temp.next

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


def compare_lists(list1, list2):
    tempOne = list1.head
    tempTwo = list2.head

    while tempOne and tempTwo:
        if tempOne.data != tempTwo.data:
            return 0

        tempOne = tempOne.next
        tempTwo = tempTwo.next

    return 1


def mergeLists(list1, list2):
    newList = LinkedList()
    newList.head = merge(list1.head, list2.head)
    return newList


def merge(head1, head2):
    if not head1 and not head2:
        return None

    if not head1:
        return head2

    if not head2:
        return head1

    if head1.data < head2.data:
        smallerNode = head1
        smallerNode.next = merge(head1.next, head2)
    else:
        smallerNode = head2
        smallerNode.next = merge(head1, head2.next)

    return smallerNode


list = LinkedList()
list.add_to_head(3)
list.add_to_head(3)
list.add_to_head(3)
list.add_to_head(4)
list.add_to_head(5)
list.add_to_head(5)

list.sort()
list.print()

print("#####")

list.removeDuplicates()

list.print()

print(list.has_cycle())

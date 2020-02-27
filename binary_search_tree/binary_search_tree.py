from dll_queue import Queue
from dll_stack import Stack
from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../queue_and_stack')


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # print(self.value)
        # print(value)
        # LEFT CASE
        # check if our new node's value is less than the current node's value
        if value < self.value:
            # does it have a child to the left?
            if not self.left:
                # place our new node here
                self.left = BinarySearchTree(value)
            # otherwise
            else:
                # repeat process for the left
                self.left.insert(value)

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
        if value >= self.value:
            # does it have a child to the right?
            if not self.right:
                # place our new node here
                self.right = BinarySearchTree(value)
            # otherwise
            else:
                # repeat the process for the right
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE
        # check if the value matches the target
        # if self.value == target:
        #     # return True
        #     return True
        # # LEFT CASE
        # # if target less than value
        # if target < self.value:
        #     # check if the left child exists
        #     if not self.left:
        #         # call the contains method of the left
        #         self.left.contains(target)
        # # RIGHT CASE
        # if target >= self.value:
        #     # check if right child exists if not
        #     if not self.right:
        #         return False
        #     # otherwise
        #     else:
        #         return self.right.contains(target)
        ##################################### 
        # BASE CASE
        if self is None or self.value is target:
            return False
        # LEFT CASE
        if self.left < target:
            return self.left.contains(target)
        else:
            return True
        # RIGHT CASE
        if self.right >= target:
            return self.right.contains(target)
        else:
            return True


    # Return the maximum value found in the tree
    def get_max(self):
        # base case
        # if empty tree
        if self is None:
            return None
        # recursive case
        # if there is no right value 
        if not self.right:
            # return the root node value
            return self.value
        # otherwise
        else:
            # return get max of the right hand child
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # BASE CASE
        cb(self.value)
        # run the callback passing in the selfs value
        # if left exists
        if self.left:
            # run the for each on left
            self.left.for_each(cb)
        # if right exists
        if self.right:
            # run the for each on the right
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

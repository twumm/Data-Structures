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
        self.size = 0
        self.storage = DoublyLinkedList()

    # Insert the given value into the tree
    def insert(self, value):
        # LEFT CASE
        # check if our new node's value is less than the current node's value
        if value < self.value:
            # does it have a child to the left?
            if not self.left:
                # place our new node here
                self.storage.add_to_head(value)
            # otherwise
            else:
                # repeat process for the left
                BinarySearchTree.insert(self, value)

        # RIGHT CASE
        # check if the new nodes value is greater than or equal to the current nodes value
        if value >= self.value:
            # does it have a child to the right?
            if not self.right:
                # place our new node here
                self.storage.add_to_tail(value)
        # otherwise
        else:
            # repeat the process for the right
            BinarySearchTree.insert(self, value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # BASE CASE

        # LEFT CASE

        # RIGHT CASE
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # base case
        # if empty tree
            # return none

        # recursive case
        # if there is no right value 
            # return the root node value
        # otherwise
            # return get max of the right hand child
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

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

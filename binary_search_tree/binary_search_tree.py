"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # left case?
        # check if the value is less than the root value?
        if value < self.value:
            # move to the left and check if it is none?
            if self.left is None:
                # insert node here
                self.left = BSTNode(value)
            # otherwise
            else:
                # call insert on the root's left node
                self.left.insert(value)
        # right case?
        if value >= self.value:
        # otherwise
            # move to the right and check if it is none?
            if self.right is None:
                # insert the node here
                self.right = BSTNode(value)
            # otherwise
            else:
                # call insert on the root's right node
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if root node = target
        if target == self.value:
            return True
        # left: check if target is < node value
        elif target < self.value:
            # move left
            # check node has left value
            if self.left == None:
                return False
            else:
                print(target, self.left.value)
                # else call contains on this node
                return self.left.contains(target)


        # right: chek if target > value
        elif target > self.value:
            #move right
            # check node has left value
            if self.right == None:
                return False
            else:
                return self.right.contains(target)
                     

    # Return the maximum value found in the tree
    def get_max(self):
        max_value = self.value 
        if self.right == None:
            return max_value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass



bst = BSTNode(5)
arr = []
cb = lambda x: arr.append(x)

bst.for_each(cb)

print(arr)


# """
# This code is necessary for testing the `print` methods
# """
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# # bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
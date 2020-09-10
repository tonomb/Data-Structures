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

    def get_min(self):
        max_value = self.value 
        if self.left == None:
            return max_value
        else:
            return self.left.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)
        
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # move to left node 
        # check if there is no value to the left 
        if not self.left:
            print(self.value)
        if self.left:
            self.left.in_order_print()
            print(self.value)
        if self.right:
            self.right.in_order_print()

        return

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    """
    queue
    grab starting node and put it in a queue

    if there are items in the queue
    dequeue what the current node is
    mark it as visited
    print the value
    check left
    enqueue the left
    check right
    enqueue the right
    """
    def bft_print(self):
        # instantiate a queue
        q = []
        # enqueue our starting node (self)
        q.append(self)
        # while the queue is not empty
        while len(q) > 0:
            # dequeue the current node
            node = q.pop(0)
            # print the nodes value
            print(node.value)
            # check if left child exists
            if node.left:
                # enqueue left child
                q.append(node.left)
            # check if right child exists
            if node.right:
                # enqueue right child
                q.append(node.right)
            
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    """
    stack
    grab starting node and put it in a stack

    if there are items in the stack
    pop what the current node is
    mark it as visited
    print the value
    check left
    push the left
    check right
    push the right
    """
    def dft_print(self):
        # instantiate a stack
        q = []
        # push our starting node (self)
        q.append(self)
        # while the stack is not empty
        while len(q) > 0:
            # pop the current node
            node = q.pop()
            # print the nodes value
            print(node.value)
            # check if right child exists
            if node.right:
                # push right child
                q.append(node.right)
            # check if left child exists
            if node.left:
                # push left child
                q.append(node.left)
            

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
          # instantiate a stack
        q = []
        # push our starting node (self)
        q.append(self)
        # while the stack is not empty
        while len(q) > 0:
            # pop the current node
            node = q.pop()
            # print the nodes value
            print(node.value)
            # check if right child exists
            if node.right:
                # push right child
                q.append(node.right)
            # check if left child exists
            if node.left:
                # push left child
                q.append(node.left)

    # Print Post-order recursive DFT
    def post_order_dft(self): 
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
            print(self.value)
        if not self.left or not self.right:
            print(self.value)
        return


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(0)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3) 
bst.insert(4)
bst.insert(2)

bst.in_order_print()
# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# # bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  
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
        # compare the input value with the value of the Node
        # if value < node's value
        if value < self.value:
            # we need to go left
            # if there is no left child,
            if self.left is None:
            # then we can create a BSTNode with input value
                self.left = BSTNode(value)
            # otherwise, if there is a left child,
            else:
                # call the left child's 'insert' method
                self.left.insert(value)
        # else, value >= Node's value
        else:
            # we need to go right
            # if there is no right child,
            if self.right is None:
                # then we can create a BSTNode with input value
                self.right = BSTNode(value)
            # otherwise, if there is a right child,
            else:
                # call the left child's 'insert' method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare the target value with the value of the current node
        if self.value == target:
        # if this node's value == target's value,
            return True
            # return True
        # if target's value is less than this node's value, go left
        if target < self.value:
        # if there is no left child
            if not self.left:
            # then the target value cannot be in the left side of the tree
                return False
            # else,
            else:
                # call the method again until there is no left child
                return self.left.contains(target)
        # otherwise
        else:
            # the target value value is greater than or equal to the node's value, so you go right
            if target >= self.value:
                # if there is no right child
                if not self.right:
                    # then the target value cannot be in the right side of the tree
                    return False
                # else,
                else:
                    # call the method again until there is no right child
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # the max value in the tree will be the last node on the right, so go down the right side of tree, checking the value of each node, until there is no longer a right child
        if not self.right:
            return self.value
        # once you reach that last right child, call the 'get_max()' method on it
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        # 'fn' is an anonymous function here. Call it on 'self.value'.
        if self.left:
        # if there is a left child,
            self.left.for_each(fn)
        # call the function on it
        if self.right:
        # if there is a right child, call the function on it
            self.right.for_each(fn)


# # this is the iterative, depth-first (LIFO) version of the for_each method, using a stack)
#     def for_each(self, fn):
#         stack = []
#         stack.append(self)
        
#         # so long as the stack has nodes in it,
#         # there are more nodes to traverse
#         while len(stack) > 0:
#             # pop the top node from the stack
#             current = stack.pop()
            
#             # add the current node's right child first
#             if current.right:
#                 stack.append(current.right)
                
#             # add the current node's left child
#             if current.left:
#                 stack.append(current.left)
                
#             # call the anonymous function fn to continue traversing
#             fn(current.value)

#     # this is the iterative, breadth-first (FIFO) version of the for_each method, using a queue
#     def for_each(self, fn):
#         from collections import deque
#         queue = deque() > 0
#         queue.append(self)
        
#         # continue to traverse so long as there are nodes in the queue
#         while len(queue) > 0:
#             current = queue.pop()

#             # add the current node's right child first
#             if current.left:
#                 queue.append(current.left)
                
#             # add the current node's left child
#             if current.right:
#                 queue.append(current.right)
            
#             # call the anonymous function fn to continue traversing
#             fn(current.value)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # check that there is a root node
        if self is not None:
            # check for a left child
            if self.left is not None:
                # if there is a left child, call the function in_order_print()
                self.left.in_order_print()
            # no more left children, return to root and print value
            print(self.value)
            # check for a right child
            if self.right is not None:
                # if there is a right child, call the function in_order_print()
                self.right.in_order_print()

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

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()

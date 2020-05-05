import sys
sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if empty
            # if empty, put node here/atroot
        if self is None:
            self = value
        # otherwise
        else:
            # if new is LESS than node.value, go LEFT
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                    return
                else:
                    self.left.insert(value)
            # if new value is GREATER than or EQUAL to node.value, go RIGHT
            else:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                    return
                else:
                    self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if node.value == findvalue
        if self.value == target:
            # return true
            return True
        # if the value doesn't exist
        elif self.value is None:
            # return false
            return False
        # if the target is LESS than the current value, travel down the left side
        elif target < self.value:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
        # if the target is GREATER than current value, travel down the right side
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
        # if it doesn't exist and all hope is lost, return false
        else:
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        # if theres no value to the right
        if self.right is None:
            # then return the root value
            return self.value
        # else, if there IS a value to the right
        else:
            # I think of 'current' as an iterator
            current = self
            # so if 'current' exists
            if current:
                # this while loop will run until it reaches the end of the tree, where it will return 'None'
                while current.right is not None:
                    # updates 'current' to the next node every iteration
                    current = current.right
                # once the loop reaches the last value and realizes there's no next, it will return the final value
                return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value is not None:
            cb(self.value)
        if self.left is not None:
            self.left.for_each(cb)
        if self.right is not None:
            self.right.for_each(cb)
        

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        
        if node.left is not None:  # to print in order, need to take the left first
            node.left.in_order_print(node.left)

        print(node.value)
        if node.right is not None:
            node.right.in_order_print(node.right)

  
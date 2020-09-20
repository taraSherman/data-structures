"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        # the length of the stack
        return len(self.storage)

    def push(self, value):
        # add element to head
        self.storage.append(value)

    def pop(self):
        if self.storage == []:
            return None
        else:
            # remove element from tail
            return self.storage.pop()

class Linked_Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        self.storage.remove_head()


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        # create a new Node
        new_node = Linked_Stack(value)
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of my new Node to the head
            new_node.set_next(self.head)
            # update the head attribute
            self.head = new_node

    def remove_head(self):
        # for empty linked list
        if self.head is None and self.tail is None:
            # there is nothing to actually return
            return None
        # what is there is only one element in the linked list? (head and tail are same Node, therefore the next_node_reference for that Node is None)
        if not self.head.get_next():
            head = self.head
            # delete the linked list's head reference
            self.head = None
            # also delete the linked list's tail reference
            self.tail = None
            return head.get_value()
        value = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return value

    def add_to_tail(self, value):
        # create new node
        new_node = Linked_Stack(value)
        # if linked list is empty
        if self.head is None:
            #update head and tail attributes
            self.head = new_node
            self.tail = new_node
        # if linked list is not empty
        else:
            #update next node of our tail
            self.tail.set_next(new_node)
            # update self.tail
            self.tail = new_node

    def remove_tail(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            # there is nothing to actually return
            return None
        # if we have a non-empty linked list
        if self.head == self.tail:
            # store the node so we can remove the value
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.tail.get_value()
            current = self.head
        # check the current Node's next_node_reference to see that that is not the tail Node
        while current.get_next() is not self.tail:
            # if it isn't, then move on down linked list until it IS the tail
            current = current.get_next()
        # at this point, 'current' is the node right before the tail
        value = self.tail.get_value()
        # move self.tail to the Node right before
        self.tail = current
        return value

    def contains(self, value):
        # loop trhough linked list until next pointer is None
        current = self.head
        while current.get_value() == value:
            return True
        current = current.get_next()
        return False

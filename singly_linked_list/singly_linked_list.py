class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # what attributes do we need?
        self.head = None
        self.tail = None

    def add_to_head(self, value):
    # create a new Node
        new_node = Node(value)
        if self.head is None:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next_node of my new Node to the head
            new_node.set_next(self.head)
            # update the head attribute
            self.head = new_node

    def add_to_tail(self, value):
        # create new node
        new_node = Node(value)
        # if linked list is empty
        if self.head is None:
            #update head and tail attributes
            self.head = new_node
            self.tail = new_node
        # id linked list is not empty
        else:
            #update next node of our tail
            self.tail.set_next(new_node)
            # update self.tail
            self.tail = new_node

    def remove_head(self):
        # empty list
        if self.head is None:
            return None
        # else, return VALUE of the old head
        else:
            ret_value = self.head.get_value()
        # list with one element
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # list with 2 elements
        else:
            self.head = self.head.get_next()
        return ret_value
    
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return

        if self.head == self.tail:
            # store the node so we can remove the value
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value

        else:
            value = self.tail.get_value()
            current = self.head

        while current.get_next() is not self.tail:
            current = current.get_next()

        self.tail = current
        self.tail.set_next(None)
        self.tail = current
        return value

    def contains(self, value):
        # loop trhough linked list until next pointer is None
        current = self.head
        while current.get_value() == value:
            return True
        current = current.get_next()
        return False

    def get_max(self):
        # TODO time permitting
        pass

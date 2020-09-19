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

    # def remove_head(self):
    #     # empty list
    #     if self.head is None:
    #         return None
    #     # else, return VALUE of the old head
    #     else:
    #         ret_value = self.head.get_value()
    #     # list with one element
    #     if self.head == self.tail:
    #         self.head = None
    #         self.tail = None
    #     # list with 2 elements
    #     else:
    #         self.head = self.head.get_next()
    #     return ret_value

    def add_to_tail(self, value):
        # create new node
        new_node = Node(value)
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

    def get_max(self):
        # TODO time permitting
        pass

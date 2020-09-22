"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        # if this node has a reference to the previous node,
        # assign the next ref of that previous node to this node's next ref
        if self.prev:
            self.prev.next = self.next
        # if this node has a next reference,
        # assign the prev reference of that node to this node's prev ref
        if self.next:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create a new Node
        new_node = ListNode(value)
        # update length
        self.length += 1
        if not self.head and not self.tail:
            # update head and tail attributes
            self.head = new_node
            self.tail = new_node
        else:
            # set next and prev of the new Node
            new_node.next = self.head
            # update the head attributes
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        #  create new node
        new_node = ListNode(value)
        # update length
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return
        self.add_to_head(node.value)
        self.delete(node)
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return
        #  single node
        if self.head is self.tail:
            self.head = None
            self.tail = None
            node.delete()
        # if node is head
        elif node is self.head:
            # set head to this node's next
            self.head = node.next
            # and delete
            node.delete()
        # if node is tail
        elif node is self.tail:
            # set tail to this node's previous
            self.tail = node.prev
            # and delete
            node.delete()
        else:
            # if it is any other node in the list, just delete
            node.delete()
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # create max variable
        current = self.head
        max = self.head.value
        # loop through nodes
        while(current is not None):
        # compare value in node to max found
            if current.value > max:
                max = current.value
            current = current.next
        # return max found
        return max

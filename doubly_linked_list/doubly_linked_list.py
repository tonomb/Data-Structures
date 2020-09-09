"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_previous(self):
        return self.prev

    def set_previous(self, new_prev):
        self.prev = new_prev

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_value(self):
        return self.value

            
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
        #if list is empty
        if not self.head:
            # wrap value in ListNode
            new_node = ListNode(value)
            #handle new nodes pointers
            new_node.set_next(None)
            new_node.set_previous(None)
            
            #change head pointer
            self.head = new_node
            #change tail pointer
            self.tail = new_node

            #add length
            self.length += 1

            return new_node

        # wrap value in ListNode
        new_node = ListNode(value)
        #handle new nodes pointers
        new_node.set_next(self.head)
        new_node.set_previous(None)

        #change old head nodes pointers
        self.head.set_previous(new_node)

        #change head pointer
        self.head = new_node

        #add length
        self.length += 1
        
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.head:
            return None
        #check if 1 value
        # if head has no next, then we have a single element in our list
        if not self.head.get_next():
            # get a reference to the head
            head = self.head
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # remove length
            self.length -= 1
            # return the value
            return head.get_value()

        # current head node
        value = self.head.get_value()
        
        # point head to current heads next value
        self.head = self.head.get_next()
        
        #point new heads prev value to none ,
        self.head.set_previous(None)

        # remove length
        self.length -= 1

        return value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # if list is empty
        if not self.tail:
            # wrap value in ListNode
            new_node = ListNode(value)
            #handle new nodes pointers
            new_node.set_next(None)
            new_node.set_previous(None)
            
            #change head pointer
            self.head = new_node
            #change tail pointer
            self.tail = new_node

            #add length
            self.length += 1

            return new_node

        new_node = ListNode(value)

        #set pointer of new node
        new_node.set_previous(self.tail)

        #change old tail next value to new node
        self.tail.set_next(new_node)

        # change tail pointer to new node
        self.tail = new_node

        # add length
        self.length += 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # return None if there is no head (i.e. the list is empty)
        if not self.tail:
            return None
        #check if 1 value
        # if head has no next, then we have a single element in our list
        if not self.tail.get_next():
            # get a reference to the tail
            tail = self.tail
            # delete the list's head reference
            self.head = None
            # also make sure the tail reference doesn't refer to anything
            self.tail = None
            # remove length
            self.length -= 1
            # return the value
            return tail.get_value()
        

        value = self.tail.get_value()

        # change tail pointer tu current tail prev value
        self.tail = self.tail.get_previous()

        #change new tails next pointer to none
        self.tail.set_next(None)

         # remove length
        self.length -= 1

            
        return value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if node is the tail
        if not node.get_next():
            current_node = node
            current_node_prev = node.get_previous()
            current_node_next = node.get_next() #none

            # change prev node's next pointer to current nodes next pointer
            current_node_prev.set_next(None)

            #change heads prev pointer to current node
            self.head.set_previous(current_node)

            #change current node pointers to none and head
            current_node.set_previous(None)
            current_node.set_next(self.head)

            #change head pointer to current node
            self.head = current_node
            self.tail = current_node_prev
            return self.head
        
        current_node = node
        current_node_prev = node.get_previous()
        current_node_next = node.get_next()

        # change prev node's next pointer to current nodes next pointer
        current_node_prev.set_next(current_node_next)

        # change next node's prev pointer to current nodes prev pointer
        current_node_next.set_previous(current_node_prev)

        #change heads prev pointer to current node
        self.head.set_previous(current_node)

        #change current node pointers to none and head
        current_node.set_previous(None)
        current_node.set_next(self.head)

        #change head pointer to current node
        self.head = current_node
        

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if node is the head
        if not node.get_previous():
            current_node = node
            current_node_prev = node.get_previous() #none
            current_node_next = node.get_next()

            # change next node's prev pointer to current nodes prev pointer
            current_node_next.set_previous(None)

            #change tails next pointer to current node
            self.tail.set_next(current_node)

            # change current nodes pointer nodes prev pointer
            current_node.set_previous(self.tail)
            current_node.set_next(None)


            #change tail pointer to current node
            self.head =current_node_next
            self.tail = current_node
            
            return self.tail
          
        current_node = node
        current_node_prev = node.get_previous() 
        current_node_next = node.get_next()

        # change next node's prev pointer to current nodes prev pointer
        current_node_next.set_previous(current_node_prev)

        #change tails next pointer to current node
        self.tail.set_next(current_node)


        #change current node pointers to none and head
        current_node.set_previous(self.tail)
        current_node.set_next(None)
        #change tail pointer to current node
        self.tail = current_node
        
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current_node_prev = node.get_previous()
        current_node_next = node.get_next()
        # change prev node's next pointer to current nodes next pointer
        current_node_prev.set_next(current_node_next)
        # change next node's prev pointer to current nodes prev pointer
        current_node_next.set_previous(current_node_prev)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value



node = ListNode(1)
dll = DoublyLinkedList(node)


dll.add_to_head(40)
print('head', dll.head.value)
print('tail', dll.tail.value)

print('moving to end')
dll.move_to_end(dll.head)
print('ntail', dll.tail.value) 
print('nhead', dll.tail.prev.value)

print('adding to tail')
dll.add_to_tail(4)
print('head', dll.head.value)
print('tail', dll.tail.value)

print('moving to end', dll.head.next.value)
dll.move_to_end(dll.head.next)
print('ntail', dll.tail.value) 
print('nhead', dll.tail.prev.value)


"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    # init a node with a value of value
    new_node = ListNode(value)

    #if the linked list is empty
    if self.length == 0:
      self.head = new_node
      self.tail = new_node
    
    #otherwise the next node will reference the head node
    new_node.next = self.head    
    #the prev node will reference the newly inserted node
    self.head.prev = new_node
    #the new node will become the head node
    self.head = new_node
    self.length += 1

  def remove_from_head(self):
    #returns if there it it an empty list
    if self.head is None:
      print("Does this work?")
      return 
   
    #checks to see if the head node has a next ref, if it doesn't it's the only thing in the list
    #and we can just set the head node to None
    if self.head.next is None:
      value = self.head.value
      self.head = None
      self.tail = None
      self.length -= 1
      return 

    #otherwise we find just the head element of our list
    #save its value to the node and delete it
    else:
      value = self.head.value
      self.head.delete()
      # self.head = self.head.next
      # self.head.prev = None
      self.length -= 1
      return value

  def add_to_tail(self, value):
    #init a node with a value of value
    new_node = ListNode(value)

    #if the list is empty
    if self.length == 0:
      self.head = new_node
      self.tail = new_node

    #otherwise the next node will reference the tail node
    new_node.prev = self.tail   
    #the prev node will reference the newly inserted node
    self.tail.next = new_node
    #the new node will become the tail node
    self.tail = new_node
    self.length += 1

  def remove_from_tail(self):
       #returns if there it it an empty list
    if self.tail is None:
      return 
   
    #checks to see if the head node has a next ref, if it doesn't it's the only thing in the list
    #and we can just set the head node to None
    if self.tail.prev is None:
      value = self.tail.value
      self.head = None
      self.tail = None
      self.length -= 1
      return

    #otherwise we find just the head element of our list
    #save its value to the node and delete it
    else:
      value = self.tail.value
      self.tail.delete()
      # self.head = self.head.next
      # self.head.prev = None
      self.length -= 1
      return value 

  def move_to_front(self, node):
    # if list is empty node becomes head & tail
    if self.length == 0:
      self.head = node
      self.tail = node
  
    #otherwise we assign the old head to point it's previous pointer at the inserted node
    current_head = self.head
    #we assign the inserted node's next pointer to point at the old head
    node.next = current_head
    #and we assign the new inserted node to be the list head
    current_head.next = node

    
    #we check to see if the node that we're moving is the tail
    #if so, we set it's next pointer
    if self.tail == node:
      self.tail = node.prev
         
    #and we assign the new inserted node to be the list as the tail
    self.head= node
    node.prev = None
        
    

  def move_to_end(self, node):
    # if list is empty node becomes head & tail
    if self.length == 0:
      self.head = node
      self.tail = node

    #otherwise we assign the old tail to point it's next pointer at the inserted node
    current_tail = self.tail
    #we assign the inserted node's previous pointer to point at the old tail
    node.prev = current_tail
    current_tail.next = node
    
    #we check to see if the node that we're moving is the head
    #if so, we set it's next pointer
    if self.head == node:
      self.head = node.next
         
    #and we assign the new inserted node to be the list as the tail
    self.tail = node
    node.next = None


  def delete(self, node):
    #if there is no previous ref on the node
    if node.prev is None:
      #the head will now equal the next node after it
      self.head = node.next
      # self.length -= 1
    else: 
      #or if the node has a previous ref that node will now point via a next ref 
      #to the one after the one being deleted
      node.prev.next = node.next
    

    #if there is no next ref on the node
    if node.next is None:
      #the tail will now equal the next node after it
      self.tail = node.prev
    else:
      #or if the node has a next ref that node will now point via a previous ref 
      #to the one after the one being deleted
      node.next.prev = node.prev

    # remove from the length for every deletion
    self.length -= 1
    
  def get_max(self):
    pass

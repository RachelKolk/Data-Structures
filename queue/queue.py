class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list Node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next_node):
        self.next_node = new_next_node


class Queue:
  def __init__(self, head=None):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []
    self.head = head

  def enqueue(self, item):

    new_node = Node(item)
    current = self.head
    if current is None:
      self.head = new_node
    else:
      while current.get_next():
        current = current.get_next()
      current.set_next(new_node)
    self.storage.append(new_node)

 
  def dequeue(self):

    current = self.head
    if current is not None:
      #will remove the first element from the list
      self.head = current.get_next()
      self.storage.pop()
      return current.value
    else:
      return None

    

  def len(self):
    return len(self.storage)


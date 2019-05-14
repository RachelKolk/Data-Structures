class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    #insert method to add item to queue
    if item not in self.storage:
      self.storage.insert(0, item)
      return True
    return False
  
  def dequeue(self):
    #using pop to remove item from queue
    if len(self.storage) > 0:
      return self.storage.pop()

  def len(self):
    return len(self.storage)

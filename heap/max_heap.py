class Heap:
  def __init__(self):
    self.storage = []
    self.current_size = 0

  def insert(self, value):
    self.storage.append(value)
    self.current_size = self.current_size + 1
    print(self.current_size)
    
    self._bubble_up(self.current_size -1)

  def delete(self):
    pass

  def get_max(self):
    pass

  def get_size(self):
    pass

  def _bubble_up(self, index):
    # check to make sure the item can actually be moved up the heap
    while index // 2 > 0:
      # if the current item's value is greater than that of its parent's...
      if self.storage[index].value > self.storage[index - 1 // 2].value:
        # we store the parent item in a temp variable
        tmp = self.storage[index - 1 // 2]
        # and then swap the parent and child items index positions
        self.storage[index - 1 // 2] = self.storage[index]
        self.storage[index] = tmp
    index = index - 1 // 2

  def _sift_down(self, index):
    pass

class Heap:
  def __init__(self):
    self.storage = []
    

  def insert(self, value):
    # append the new value to the end of the heap
    self.storage.append(value)
    # and move the new node up to the proper positions using the bubble_up function
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    # if the heap has two or more values
    if len(self.storage) > 1:
      # we swap the first and last values of the heap
      self._swap(0, len(self.storage) - 1)
      # we pop the max value off the heap and store it in a max variable
      max = self.storage.pop()
      #and then we sift the swapped item down to where it belongs
      self._sift_down(0)
    #if there is only one variable in the heap
    elif len(self.storage) == 1:
      # we save it as the max variable so we can return it as the largest item
      max = self.storage.pop()
    else: 
      max = False
    # return our largest heap item
    return max

  def get_max(self):
    # make sure that our heap contains at least one item...
    if self.storage[0]:
      #if there is it will return the top item because that will be the largest
      return self.storage[0]
    else:
      return False

  def get_size(self):
    return len(self.storage)

  # created this just to make it easier to swap nodes in the functions
  def _swap(self, i, k):
    self.storage[i], self.storage[k] = self.storage[k], self.storage[i]

  def _bubble_up(self, index):
    # find the parent index of the new node index
    parent = (index - 1) // 2
    # if the value of the new node is less than its parent...
    if index <= 0:
      #it will already be in the right order and we don't have to do anything
      return
    # if the value of the index is greater than its parent...
    elif self.storage[index] > self.storage[parent]:
      # we'll swap the two nodes
      self._swap(index, parent)
      #and bubble_up the parent node
      self._bubble_up(parent)


  def _sift_down(self, index):
    # start by defining the index formulas assigned to each side
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index
    # we compare the index value to both the left and right to see which is the largest
    if len(self.storage) > left and self.storage[largest] < self.storage[left]:
      largest = left
    if len(self.storage) > right and self.storage[largest] < self.storage[right]:
      largest = right
    # if the largest value is not at the index we swap and sift down
    if largest != index:
      self._swap(index, largest)
      self._sift_down(largest)

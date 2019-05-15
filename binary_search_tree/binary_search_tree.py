class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


  def insert(self, value):

    if self is None:
      self = value

    elif value < self.value:
      if self.left is None:
        self.left = BinarySearchTree(value)
      else: 
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)


  def contains(self, target):
    if self.value == target:
      return True

    elif self.value > target:
      if self.left:
        return self.left.contains(target)
      else:
        return False

    else:
      if self.right:
        return self.right.contains(target)
      else: 
        return False


  def get_max(self):
    
    if self.right is None:
      return self.value
    
    else:

      current_node = self

      while current_node.right is not None:
        current_node = current_node.right
    return current_node.value


  def for_each(self, cb):
    pass
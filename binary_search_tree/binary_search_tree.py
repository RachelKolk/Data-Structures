class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert (self, data):
    if self.value == data:
      return False

    elif self.value > data:
      if self.left:
        return self.left.insert(data)
      else:
        self.left = Node(data)
        return True

    else:
      if self.right:
        return self.right.insert(data)
      else:
        self.right = Node(data)
        return True

  def contains(self, data):
    if self.value == data:
      return True

    elif self.value > data:
      if self.left:
        return self.left.contains(data)
      else:
        return False

    else:
      if self.right:
        return self.right.contains(data)
      else: 
        return False


class BinarySearchTree:
  # def __init__(self, value):
  #   self.value = value
  #   self.left = None
  #   self.right = None
  def __init__(self, value):
    self.root = None
    self.left = None
    self.right = None
    self.value = value
    

  def insert(self, value):
    if self.root:
      return self.root.insert(value)
    else:
      self.root = Node(value)
      return True

  def contains(self, target):
    if self.root:
      return self.root.contains(target)
    else:
      return False

  def get_max(self):
    pass

  def for_each(self, cb):
    pass
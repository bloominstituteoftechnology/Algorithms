
'''
Max Stack - provide O(1) access time complexity with maxValue stack.
            items on the stack are processed in FILO order.

getMax - method to access max value on stack in O(1) time complexity.
'''
class Stack:
  def __init__(self):
    self.storage = []

  def push(self, item):
    self.storage.append(item)
  
  def pop(self):
    if len(self.storage) > 0:
      return self.storage.pop()
    else:
      return None

  def peek(self):
    storage_size = len(self.storage)
    if storage_size > 0:
      return self.storage[storage_size -1]
    else:
      return None

class MaxStack:
  def __init__(self):
    self.stack = Stack()
    self.maxValues = Stack()

  def push(self,item):
    self.stack.push(item)
    peekValue = self.maxValues.peek()
    if peekValue is None or peekValue <= item:
      self.maxValues.push(item)

  def pop(self):
    item = self.stack.pop()
    if item == self.maxValues.peek():
      self.maxValues.pop()
    return item

  def getMax(self):
    return self.maxValues.peek()
  
m = MaxStack()
m.push(50)
m.push(60)
m.push(40)
m.push(45)
print(m.stack.storage, m.maxValues.storage)
print(m.pop())
print(m.stack.storage, m.maxValues.storage)

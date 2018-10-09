def iterative_search(array, target):
    for item in array:
        if item == target:
            return True
    return False
# time: O(n)
# space: O(1)

def recursive_search(array, target):
    # base case
    if len(array) == 0:
        return False
    # move towards the base case
    if target == array.pop():
        return True
    return recursive_search(array, target)
# time: O(n)
# space: O(n)


# stack class takes advantage of built-in Python list methods
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]
        

class MaxStack:
    def __init__(self):
        self.items = []
        self.max_values = []

    def push(self, item):
        self.items.append(item)
        if not len(self.max_values) or item > self.max_values[-1]:
            self.max_values.append(item)

    def pop(self):
        popped = self.items.pop()
        if popped == self.max_values[-1]:
            self.max_values.pop()
        return popped

    def peek(self):
        return self.items[-1]

    def getMax(self):
        return self.max_values[-1]
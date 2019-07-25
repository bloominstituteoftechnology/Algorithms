class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertLeft(self, value):
        self.left =  BinaryTreeNode(value)
        return self.left


    def insertRight(self, value):
        self.right =  BinaryTreeNode(value)
        return self.right
  
def checkBalanced(rootNode):
    # empty tree is balanced
    if rootNode == None:
        return True

    def minDepth(node):
        
        if node == None:
            return 0
        return 1 + min(minDepth(node.left), minDepth(node.right))

    def maxDepth(node):
        if node == None:
            return 0
        return 1 + max(maxDepth(node.left), maxDepth(node.right))
    
    return (minDepth(rootNode) - maxDepth(rootNode) == 0)

node = BinaryTreeNode(5)
node.insertLeft(4)
node.insertRight(6)
print(checkBalanced(node))
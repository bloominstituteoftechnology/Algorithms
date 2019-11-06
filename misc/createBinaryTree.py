
import math
'''
Create binary tree from an ascending list
a = [1,2,3,4,5,6]
'''

class BinaryTree:
    def __init__(self,value):
        self.node = value
        self.left = None
        self.right = None



def createBinaryTree(sorted_list, left, right):
    
    if right < left :
        return None
        
    mid = (left+right) // 2
    node = BinaryTree(sorted_list[mid])

    node.left = createBinaryTree(sorted_list, left, mid-1) # mid taken for root node
    
    node.right = createBinaryTree(sorted_list, mid+1, right)

    return node

def isBT(tree):
    '''
    validate binaryTree by checking left value < root < right value.
    '''
    if tree is None:
        return None

    if tree.left is not None and tree.left.node > tree.node:
        return False # left must be less than root

    if tree.right is not None and tree.right.node < tree.node:
        return False # right node must be greater than root


    isBT(tree.left)
    isBT(tree.right)

    return True

def maxDepth(tree):
    if tree is None:
        return 0    # max return integer value
    
    return 1 + max(maxDepth(tree.left), maxDepth(tree.right))

a=[1,2,3,4,5,6]
tree = createBinaryTree(a,0,len(a)-1)
print(f' Is Binary Tree = {isBT(tree)}')
print(f' Max Depth of Tree = {maxDepth(tree)}')
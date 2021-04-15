#Basic Node definition. Each Node contains a Value, a left child, and a right child
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

#insert Value into the appropiate spot in the tree
def insert(root, node):

    if root is None:
        root=node
    elif root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)

def search_helper(root, n):
    if root is None:
        return False
    if root.val==n:
        return True
    if root.val>n:
        return search_helper(root.left, n)
    return search_helper(root.right, n)

def search(n):
    return search_helper(bst, n)

def inorder_traversal(root):
    #finish code to print all values with an inorder traversal
    if root is not None:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root is not None:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)

bst = Node(5)
insert(bst,Node(2))
insert(bst,Node(7))
insert(bst,Node(10))
insert(bst,Node(4))
insert(bst,Node(1))

print("------inorder traversal------")
inorder_traversal(bst)

print("------preorder traversal------")
preorder_traversal(bst)

print("------postorder traversal------")
postorder_traversal(bst)

print("------search------")

print(search(1))
print(search(2))
print(search(3))
print(search(4))
print(search(5))
print(search(6))
print(search(7))
print(search(8))
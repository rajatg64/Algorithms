class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertBST(root, data):
    if root is None:
        root = Node(data)
        return root
    elif data < root.data:
        if root.left is None:
            root.left = Node(data)
        else:
            return insertBST(root.left, data)
    else:
        if root.right is None:
            root.right = Node(data)
        else:
            return insertBST(root.right, data)

def preorderBST(root):
    if root is None:
        return
    else:
        print(root.data)
        inorderBST(root.left)
        inorderBST(root.right)

def PostorderBST(root):
    if root is None:
        return
    else:
        inorderBST(root.left)
        inorderBST(root.right)
        print(root.data)

def inorderBST(root):
    if root is None:
        return
    else:
        inorderBST(root.left)
        print(root.data)
        inorderBST(root.right)

def SearchKey(root, key):
    if root is None:
        return False
    else:
        if key == root.data:
            return True
        elif key < root.data:
            return SearchKey(root.left, key)
        else:
            return SearchKey(root.right, key)


def level_order_transversal(root):
    q = []
    q.append(root)
    while(len(q) > 0):
        temp = q.pop(0)
        print(temp.data)
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)
            
root = Node(50)
insertBST(root,30)
insertBST(root,20)
insertBST(root,40)
insertBST(root,70)
insertBST(root,60)
insertBST(root,80)

inorderBST(root)

print(SearchKey(root, 20))

level_order_transversal(root)


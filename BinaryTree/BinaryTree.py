class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.data = key

def PreOrder(root):
    if (not root):
        return
    print(root.data, " ")
    PreOrder(root.left)
    PreOrder(root.right)

def PostOrder(root):
    if (not root):
        return
    PostOrder(root.left)
    PostOrder(root.right)
    print(root.data)

def InOrder(root):
    if (not root):
        return
    PostOrder(root.left)
    print(root.data)
    PostOrder(root.right)



def LevelOrder(root):
    q = []
    q.append(root)

    while(len(q)):
        temp = q[0]
        print(temp.data)
        q.pop(0)

        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)

node =  Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)

#LevelOrder(node)
#PreOrder(node)
PostOrder(node)



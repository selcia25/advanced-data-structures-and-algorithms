class Node:

    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data

class SplayTree:

    def __init__(self):
        self.root = None

    def Maximum(self, n):
        while n.right != None:
            n = n.right
        return n
    
    def leftRotate(self, p):
        x = p.right # right child of p is x
        p.right = x.left # left child of x will become right child of p
        if x.left != None:
            x.left.parent = p # p will become parent of x's left child
        
        x.parent = p.parent
        if p.parent == None: # when p is root, x becomes root
            self.root = x
        elif p == p.parent.right: # when p is right child
            p.parent.right = x
        else: # when p is left child
            p.parent.left = x
        x.left = p
        p.parent = x

    def rightRotate(self, p):
        x = p.left
        p.left = x.right

        if x.right != None:
            x.right.parent = p

        x.parent = p.parent
        if p.parent == None:
            self.root = x
        elif p == p.parent.right:
            p.parent.right = x
        else:
            p.parent.left = x

        x.right = p
        p.parent = x

    def Splay(self, n):

        # splay node n to root, stop the loop when n reaches root

        while n.parent != None: # run this loop until node is not root

            if n.parent == self.root: # node has a parent which is the root - one rotation(either left/right)
                # Zig rotation
                if n == n.parent.left: # Left child
                    self.rightRotate(n.parent)
                # Zag Rotation
                else: # Right child
                    self.leftRotate(n.parent)
            
            else: # two rotations - set p as parent & g as grandparent
                p = n.parent
                g = p.parent
                # Zig-zig rotation
                if n.parent.left == n and p.parent.left == p: # both n and p are left children
                    self.rightRotate(g)
                    self.rightRotate(p)
                # Zag-zag rotation
                elif n.parent.right == n and p.parent.right == p: # both n and p are right children
                    self.leftRotate(g)
                    self.leftRotate(p)
                # Zig-zag rotation
                elif n.parent.right == n and p.parent.left == p: # n - right, p - left
                    self.leftRotate(p)
                    self.rightRotate(g)
                # Zag-zig rotation
                else:
                    self.rightRotate(p)
                    self.leftRotate(g)

    def Search(self, n, x):  # splay the node searched to the root
        if x == n.data:
            self.Splay(n)
            return n
        elif x < n.data:
            return self.Search(n.left, x)
        elif x > n.data:
            return self.Search(n.right, x)
        else:
            return ("Not found")
        
    def Insert(self, n):  # insert & splay to root
        y, temp = None, self.root
        while temp != None:
            y = temp
            if n.data < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        n.parent = y
        if y == None:
            self.root = n
        elif n.data < y.data:
            y.left = n
        else:
            y.right = n
        self.Splay(n)

    def Delete(self, n):
        self.Splay(n)  # Splay the node to root

        left_subtree = SplayTree()
        left_subtree.root = self.root.left
        if left_subtree.root != None:
            left_subtree.root.parent = None # make the left subtree's parent None i.e. root - node to be deleted

        right_subtree = SplayTree()
        right_subtree.root = self.root.right
        if right_subtree.root != None:
            right_subtree.root.parent = None # make the right subtree's parent None i.e. root - node to be deleted

        if left_subtree.root != None:
            m = left_subtree.Maximum(left_subtree.root) # find the maximum value in left subtree
            left_subtree.Splay(m)
            left_subtree.root.right = right_subtree.root
            self.root = left_subtree.root

        else:
            self.root = right_subtree.root

    def Inorder(self, n):
        if n != None:
            self.Inorder(n.left)
            print(n.data)
            self.Inorder(n.right)
if __name__ == '__main__':
    t = SplayTree()

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(100)
e = Node(90)
f = Node(40)
g = Node(110)
h = Node(120)
t.Insert(a)
t.Insert(b)
t.Insert(c)
t.Insert(d)
t.Insert(e)
t.Insert(f)
t.Insert(g)
t.Insert(h)
print("Inorder traversal of the Splay Tree:")
t.Inorder(t.root)
print("Deleting node 40 from the Splay Tree:")
t.Delete(f)
print("Inorder traversal of the Splay Tree after deletion:")
t.Inorder(t.root)
print("Searching for node with value 90 in the Splay Tree:")
node = t.Search(t.root, 90)
print("Splayed node with value 90 to the root:")
print(node.data)
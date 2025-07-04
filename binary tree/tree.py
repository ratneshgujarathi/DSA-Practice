from collections import deque

class BT:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        new_node = BT(val)

        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()

            if not node.left:
                node.left = new_node
                return

            queue.append(node.left)

            if not node.right:
                node.right = new_node
                return

            queue.append(node.right)





def dfs(root):
    if root is None:
        return
    
    print(root.data)
    dfs(root.left)
    dfs(root.right)


def bfs(root, ans):
    if root is None:
        return

    q = deque()
    q.append(root)

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        ans.append(level)
            
def pre_order_traversal(root):
    if root is None:
        return
    print(root.data)
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)

def post_order_traversal(root):
    if root is None:
        return
    pre_order_traversal(root.left)
    pre_order_traversal(root.right)
    print(root.data)
        
def in_order_traversal(root):
    if root is None:
        return
    pre_order_traversal(root.left)
    print(root.data)
    pre_order_traversal(root.right)
        


root = BT(1)
tree = Tree(root)

tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)


# pre_order_traversal(tree.root)
# post_order_traversal(tree.root)
# in_order_traversal(tree.root)

# dfs(tree.root)
ans = []
bfs(tree.root, ans)

print(ans)
# 二叉树遍历

# 定义节点
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.parent = None

"""二叉树
          0
      /       \
     1          2
   /   \       /  \
  3     4     5    6
"""

# 递归前序遍历 根-左-右 1 2 4 5 3 6 7
def recursive_preorder_traversal(root):
    if root != None:

        # 打印根节点
        print(root.data)

        # 遍历左子树
        left = root.left
        if left != None:
            recursive_preorder_traversal(left)

        # 遍历右子树
        right = root.right
        if root.right != None:
            recursive_preorder_traversal(right)

# 递归中序遍历 左-根-右 3 1 4 0 5 2 6
def recursive_inorder_traversal(root):
    if root != None:

        # 遍历左子树
        left = root.left
        if left != None:
            recursive_inorder_traversal(left)

        # 打印根节点
        print(root.data)

        # 遍历右子树
        right = root.right
        if right != None:
            recursive_inorder_traversal(right)

# 递归后序遍历 左-右-中 3 4 1 5 6 2 0
def recursive_postorder_traversal(root):
    if root != None:

        # 遍历左子树
        left = root.left
        if left != None:
            recursive_postorder_traversal(left)

        # 遍历右子树
        right = root.right
        if right != None:
            recursive_postorder_traversal(right)

        # 打印根节点
        print(root.data)

if __name__ == '__main__':

# 构建二叉树
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    root.left = node1
    node1.parent = root
    root.right = node2
    node2.parent = root
    node1.left = node3
    node3.parent = node1
    node1.right = node4
    node4.parent = node1
    node2.left = node5
    node5.parent = node2
    node2.right = node6
    node6.parent = node2

    recursive_preorder_traversal(root)
    # recursive_inorder_traversal(root)
    # recursive_postorder_traversal(root)
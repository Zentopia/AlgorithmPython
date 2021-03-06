# 定义节点
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# 链表反转
# 1. 循环法
def reverse(head_node):

    next_node = head_node.next
    prev_node = head_node

    #第一个节点反转后成为最后一个节点
    prev_node.next = None

    while True:
        head_node = next_node
        next_node = head_node.next

        #反转
        head_node.next = prev_node

        if next_node == None:
            break
        prev_node = head_node

    return head_node

## 2. 递归法
def recursive_reverse(reversed_node, new_node):
    if new_node == None:
        print(reversed_node)
        return reversed_node

    next_node = new_node.next
    new_node.next = reversed_node
    return recursive_reverse(new_node, next_node)

if __name__ == '__main__':

    # 创建链表
    head_node = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    head_node.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # 循环法
    # head_node = reverse(head_node)

    # 递归法
    new_node = head_node.next
    head_node.next = None
    head_node = recursive_reverse(head_node, new_node)

    # 打印反转后的链表
    while head_node != None:
        print(head_node.data)
        head_node = head_node.next
        
"""
宝宝写的：

class Node:
def __init__(self,data):
    self.data = data
    self.next = None


def recursive_reverse(reversed_node, next_node):
    if next_node == None:
        return reversed_node
    new_node = next_node.next
    next_node.next = reversed_node
    return recursive_reverse(next_node, new_node)

def loop(head_node):
    second_node = head_node.next
    third_node = second_node.next
    head_node.next = None
    second_node.next = head_node
    while third_node!=None:
        head_node = second_node
        second_node = third_node
        third_node = third_node.next
        second_node.next = head_node
    return second_node

def print_node(head_node):
    while(head_node!=None):
        print(head_node.data)
        head_node = head_node.next

if __name__ == '__main__':
    head_node = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    head_node.next = node1
    node1.next = node2
    node2.next = node3
    # head_node.next = None
    # head_node = recursive_reverse(head_node,node1)
    head_node = loop(head_node)
    print_node(head_node)
 """

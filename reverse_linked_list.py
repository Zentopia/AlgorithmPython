# 定义节点
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

# 链表反转
def reverse(head_node):

    next_node = head_node.next
    prev_node = head_node

    #第一个节点反转后称为最后一个节点
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

    head_node = reverse(head_node)

    # 打印反转后的链表
    while head_node != None:
        print(head_node.data)
        head_node = head_node.next
# 定义节点
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


#创建链表
head_node = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

head_node.next = node1
node1.next = node2
node2.next = node3

#链表反转

while True:
    current_node = head_node
    head_node = head_node.next
    temp_node = head_node.next

    if temp_node == None:
        break

while head_node != None:
    print(head_node.data)
    head_node = head_node.next
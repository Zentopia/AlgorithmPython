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
node4 = Node(4)

head_node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

#链表反转
temp_node = head_node.next
current_node = head_node
current_node.next = None

while True:
    head_node = temp_node
    temp_node = head_node.next
    #反转
    head_node.next = current_node

    if temp_node == None:
        break
    current_node = head_node

#打印链表
while head_node != None:
    print(head_node.data)
    head_node = head_node.next
# Односвязный список

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next= c
c.next = d
d.next = b
#print(d.next.data)


# Поиск цикла с помощью метода кролика и черепахи
# сложность O(n)
class FindLoop:

    def __init__(self):
        self.head = None

    # функция создания цикла в классе Node

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # выводим цикл на экран

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def detect_loop(self):
        slow = self.head
        fast = self.head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Тест


linked_list = FindLoop()
linked_list.push(1)
linked_list.push(2)
linked_list.push(3)
linked_list.push(4)
linked_list.push(5)

# создаем цикл

linked_list.head.next.next.next.next = linked_list.head
#linked_list.print_list()
if linked_list.detect_loop():
    print('Loop found')
else:
    print('No loop')
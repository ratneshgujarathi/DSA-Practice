class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, node:ListNode):
        if not self.head:
            self.head = node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = node


    def insert_at_beginning(self, node:ListNode):
        if not self.head:
            self.head = node
            return
        node.next = self.head
        self.head = node

    def insert_node_at_position(self, pos ,node: ListNode):
        if pos == 0:
            self.insert_at_beginning(node)

        ind = 1
        curr = self.head
        while curr.next:
            if pos == ind:
                node.next = curr.next
                curr.next = node
                return
            else:
                curr = curr.next
                ind+=1

        print('position not found')

    def update_node_at_position(self, pos, val):
        ind = 0
        curr = self.head
        while curr.next:
            if pos == ind:
                curr.val = val
                return
            else:
                curr = curr.next
                ind+=1

        print('position not found')

    def update_node_with_val(self, key, val):
        curr = self.head
        while curr.next:
            if curr.val == key:
                curr.val = val
                return
            else:
                curr = curr.next

    def delete_node_with_val(self, key):
        curr = self.head
        prev = None
        while curr.next:
            if curr.val == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def print_linked_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    def search_with_val(self, key):
        ind = 0
        curr = self.head

        if curr.val == key:
            return ind

        while curr:
            if curr.val == key:
                return ind
            ind+=1
            curr = curr.next

        return -1

ll = LinkedList()
ll.insert_at_end(ListNode(1))
ll.print_linked_list()

ll.insert_at_end(ListNode(2))
ll.print_linked_list()

ll.insert_at_end(ListNode(3))
ll.print_linked_list()

ll.insert_at_beginning(ListNode(4))
ll.print_linked_list()

ll.insert_node_at_position(1, ListNode(5))
ll.print_linked_list()

ll.update_node_at_position(2, 7)
ll.print_linked_list()

ll.update_node_with_val(5, 8)
ll.print_linked_list()

ll.delete_node_with_val(8)
ll.print_linked_list()

print(ll.search_with_val(5))

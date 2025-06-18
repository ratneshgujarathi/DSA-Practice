class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

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
        node.prev = curr


    def insert_at_beginning(self, node:ListNode):
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def insert_node_at_position(self, pos ,node: ListNode):
        if pos == 0:
            self.insert_beginning(node.data)  # Or handle `node` directly
            return

        curr = self.head
        index = 0

        while curr:
            if index == pos - 1:
                node.next = curr.next
                node.prev = curr
                if curr.next:
                    curr.next.prev = node  # Fix backward link
                curr.next = node
                return
            curr = curr.next
            index += 1

        print("Position out of bounds")

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
    
    def length(self):
        length = 0
        curr = self.head
        while curr:
            length+=1
            curr = curr.next

        return length
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.next     
            curr.next = prev           
            prev = curr               
            curr = next_node 

        self.head = prev

dl = LinkedList()
dl.insert_at_end(ListNode(1))
dl.print_linked_list()

dl.insert_at_end(ListNode(2))
dl.print_linked_list()

dl.insert_at_end(ListNode(3))
dl.print_linked_list()

dl.insert_at_beginning(ListNode(4))
dl.print_linked_list()

dl.insert_node_at_position(1, ListNode(5))
dl.print_linked_list()

dl.update_node_at_position(2, 7)
dl.print_linked_list()

dl.update_node_with_val(5, 8)
dl.print_linked_list()

dl.delete_node_with_val(8)
dl.print_linked_list()

print(dl.search_with_val(7))

print(dl.length())

dl.reverse()
dl.print_linked_list()

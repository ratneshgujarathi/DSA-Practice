class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def print_linked_list(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

class Solution:
    def reverse_iter(self, head):
        curr = head
        prev = None

        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        head = prev
        return head
    
    def reverse_recur(self, head):
        if not head or not head.next:
            return head
        
        new_node = self.reverse_recur(head.next)
        front = head.next
        front.next = head
        head.next = None

        return new_node 
    

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
s = Solution()
head.print_linked_list(head)
head = s.reverse_iter(head)
head.print_linked_list(head)


            
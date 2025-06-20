class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    def print_linked_list(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

class Solution:
    
    def odd_even_list(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        odd , even, even_head = head, head.next, head.next

        while even is not None and even.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = even_head

        return head
    

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2

s = Solution()
head = s.odd_even_list(head)
head.print_linked_list(head)
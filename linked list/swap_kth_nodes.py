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
    '''Note - linked list is 1-indexing list'''
    def swap_kth_nodes(self, head: ListNode, k: int) -> ListNode:
        curr = head
        for _ in range(k-1):
            curr = curr.next

        l, r = curr, head

        while curr.next:
            curr = curr.next
            r = r.next

        l.val, r.val = r.val, l.val

        return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2

s = Solution()
head = s.swap_kth_nodes(head, k)
head.print_linked_list(head)
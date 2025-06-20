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
    def delete_kth_node_from_end(self, head: ListNode, k: int) -> ListNode:
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next

        if fast is None:
            new_node = head.next
            return new_node
        
        while fast.next:
            slow = slow.next
            fast= fast.next

        temp  = slow.next
        slow.next = slow.next.next
        del temp
        
        return head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2

s = Solution()
head = s.delete_kth_node_from_end(head, k)
head.print_linked_list(head)
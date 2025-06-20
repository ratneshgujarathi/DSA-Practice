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
    def sort_0s_1s_2s(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        zero_head = ListNode(-1)
        one_head = ListNode(-1)
        two_head = ListNode(-1)

        zero = zero_head
        one = one_head
        two = two_head
        curr = head

        while curr:
            if curr.val == 0:
                zero.next = curr
                zero = zero.next
            elif curr.val == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next

            curr = curr.next

        zero.next = one_head.next if one_head.next is not None else two_head.next
        one.next = two_head.next
        two.next = None

        new_node = zero_head.next

        return new_node



head = ListNode(0, ListNode(1, ListNode(0, ListNode(1, ListNode(2, ListNode(0, ListNode(1, ListNode(2))))))))
s = Solution()
head = s.sort_0s_1s_2s(head)
head.print_linked_list(head)
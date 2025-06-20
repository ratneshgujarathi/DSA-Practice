class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    @staticmethod
    def print_linked_list(head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

class Solution:
    def reverse(self, head):
        temp = head
        prev = None
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    
    def find_kth_node(self, head, k):
        k-=1
        while head and k > 0:
            k-=1
            head = head.next

        return head
    
    def get_length(self, head):
        length = 0
        while head:
            length+=1
            head = head.next

        return length
    def rotate_by_k(self, head, k):
        if not head or not head.next or k == 0:
            return head
        # get length
        n = self.get_length(head)

        # calculating k as k can be more than length
        k %= n
        if k == 0:
            return head
        
        temp = head

        # dividing into two halves 0 -> k and k+1 -> n
        first_half = self.find_kth_node(temp, n - k)
        second_half = first_half.next
        first_half.next = None

        # reversing both halves
        first_reversed = self.reverse(temp)
        second_reversed = self.reverse(second_half)

        # join both halves
        curr  = first_reversed
        while curr.next:
            curr = curr.next

        curr.next = second_reversed

        return self.reverse(first_reversed)
    
sample = ListNode(1, ListNode(2,ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
ListNode.print_linked_list(sample)
s = Solution()
rotated = s.rotate_by_k(sample, 2)
ListNode.print_linked_list(rotated)
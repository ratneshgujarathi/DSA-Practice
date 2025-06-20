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
    def reverse(self, head):
        temp = head
        prev = None
        while temp:
            new_node = temp.next
            temp.next = prev
            prev = temp
            temp = new_node
            
        head = prev
        return head
    
    def add_1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        head = self.reverse(head)
        carry = 1
        temp = head
        while temp:
            if carry:
                new_val = temp.val + carry
                temp.val = new_val % 10
                carry = new_val // 10 
                temp = temp.next
            else:
                break

        head = self.reverse(head)
        if carry:
            new_node = ListNode(carry)
            new_node.next = head
            head = new_node
        
        return head
    
    def backtrack(self, head):
        if head is None:
            return 1 
        carry = self.backtrack(head.next)
        head.val = head.val + carry
        if head.val < 10:
            return 0
        head.val = 0
        return 1

    def add_1_backtracking(self, head):
        if not head or not head.next:
            return head
        
        carry = self.backtrack(head)
        if carry:
            new_node = ListNode(carry)
            new_node.next = head
            head = new_node
        return head
    
    def add_k_in_ll(self, head, k):
        if not head or not head.next:
            return head
        
        head = self.reverse(head)
        carry = k
        temp = head
        while temp:
            if carry:
                new_val = temp.val + carry
                temp.val = new_val % 10
                carry = new_val // 10 
                temp = temp.next
            else:
                break

        head = self.reverse(head)
        if carry:
            new_node = ListNode(carry)
            new_node.next = head
            head = new_node
        
        return head

    def add_two_ll(self, head1, head2):
        dummy = ListNode(-1)
        temp = dummy
        l1 = head1
        l2 = head2
        carry = 0

        while l1 or l2:
            new_sum = carry
            if l1: new_sum+=l1.val
            if l2: new_sum+=l2.val
            new_node = ListNode(new_sum%10)
            carry = new_sum//10
            temp.next = new_node
            temp = temp.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            temp.next = ListNode(carry)

        return dummy.next

head = ListNode(9, ListNode(9, ListNode(9)))
head1 = ListNode(0, ListNode(0, ListNode(0, ListNode(1))))
s = Solution()

head = s.add_two_ll(head, head1)
head.print_linked_list(head)
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
    def find_tail(self, head, k):
        k-=1
        while head and k > 0:
            k-=1
            head = head.next
        return head
    
    def get_length(self, head):
        count = 0
        while head:
            count+=1
            head = head.next
        return count
    
    def split_ll(self, head, k):
        ans = []
        # getting the length
        n = self.get_length(head)

        # divinding into parts and extras
        part_size = n // k
        extra = n % k

        temp = head
        for i in range(k):
            # calculation of current size of division
            curr_part_size = part_size + (1 if i < extra else 0 )
            if curr_part_size == 0:
                ans.append(None)
                continue

            part_head = temp

            # find the end of the divided part
            tail = self.find_tail(part_head, curr_part_size)

            # assigning back the next part of ll to proceed further
            if tail:
                temp = tail.next
                tail.next = None

            ans.append(part_head)

        return ans
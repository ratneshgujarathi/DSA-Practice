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
        curr = head
        prev = None
        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        return prev

    def find_kth_node(self, head, k):
        k-=1
        while head and k > 0:
            k-=1
            head = head.next

        return head

    def reverse_node_k_groups(self, head, k):
        temp = head
        prev = None

        while temp:
            kth_node = self.find_kth_node(temp, k)

            if not kth_node:
                if prev: 
                    prev.next = temp
                break

            next_node = kth_node.next
            kth_node.next = None

            reverse_head = self.reverse(temp)

            if temp == head:
                head = reverse_head
            else:
                prev.next = reverse_head

            prev = temp
            temp = next_node

        return head


sample = ListNode(1, ListNode(2,ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
s = Solution()
ListNode.print_linked_list(sample)

ListNode.print_linked_list(s.find_kth_node(sample, 3))
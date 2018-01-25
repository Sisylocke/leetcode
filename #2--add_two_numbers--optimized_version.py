# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def addTwoNumbers(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        flag = 0
        ln = ListNode(0)
        r = ln
        while l1 is not None or l2 is not None or flag:
            if l1 is None and l2 is not None:
                sum = l2.val + flag
            elif l2 is None and l1 is not None:
                sum = l1.val + flag
            elif l1 is None and l2 is None:
                sum = flag
            else:
                sum = l1.val + l2.val + flag

            flag = 1 if sum >= 10 else 0
            sum %= 10
            p = ListNode(sum)
            r.next = p
            r = p

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return ln.next
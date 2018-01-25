# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def convert_to_integer(linknode):
        int_list = []
        while linknode is not None:
            int_list.append(linknode.val)
            linknode = linknode.next
        integer = int(''.join(map(str, int_list))[::-1])  # numbers are arranged in normal order
        return integer

    @staticmethod
    def convert_to_linklist(integer):
        int_list = [i for i in map(int, str(integer))][::-1]

        link_list = []

        listnode = ListNode(int_list[0])
        link_list.append(listnode.val)
        if len(int_list) > 1:
            for ln in int_list[1:]:
                listnode.next = ListNode(ln)
                listnode = ListNode(ln)
                link_list.append(listnode.val)
        return link_list

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_integer = self.convert_to_integer(l1)
        l2_integer = self.convert_to_integer(l2)
        l = l1_integer + l2_integer

        l_listnode = self.convert_to_linklist(l)
        return l_listnode

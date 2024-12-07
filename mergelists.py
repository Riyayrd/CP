##https://leetcode.com/problems/merge-two-sorted-lists/

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        list3=ListNode()
        cur=list3
        while list1 and list2:
            if list1.val<list2.val:
                cur.next=list1
                list1=list1.next
            else:
                cur.next=list2
                list2=list2.next
            cur=cur.next
        cur.next=list1 or list2

        return list3.next            
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

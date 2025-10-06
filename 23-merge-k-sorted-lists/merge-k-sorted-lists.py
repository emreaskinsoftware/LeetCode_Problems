# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    def mergeTwoLists(self,list1,list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val<= list2.val:
                list1.next = self.mergeTwoLists(list1.next,list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1,list2.next)
                return list2
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        while len(lists)>1:
            merged = []
            for i in range(0,len(lists),2):            
                if i+1<len(lists):
                    if not lists[i+1]:
                        merged.append(lists[i])
                    elif not lists[i]:
                        merged.append(lists[i+1])
                    else:
                        l1 = lists[i]
                        l2 = lists[i+1]
                        merged.append(self.mergeTwoLists(l1,l2))
                else:
                    merged.append(lists[i])
            lists=merged
        
        return lists[0]
        
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(list1: ListNode,list2: ListNode):
    merged = dummy = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            merged.next = list1
            list1 = list1.next
            merged = merged.next
        elif list1.val > list2.val:
            merged.next = list2
            list2 = list2.next
            merged = merged.next
        else:
            merged.next = list1
            list1 = list1.next
            merged = merged.next
            merged.next = list2
            list2 = list2.next
            merged = merged.next
    if list1 or list2:
        merged.next = list1 if list1 else list2
    return dummy.next



list1 = ListNode(1,ListNode(2,ListNode(4,None)))
list2= ListNode(1,ListNode(3,ListNode(4,None)))

print(main(list1,list2))





class ListNode:
    def __init__(self,data=''):
        self.data=data
        self.next=None

        return
def mergetwolist(l1:ListNode,l2:ListNode):
    dummy=ListNode()
    tail=dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next=l1.data
            l1=l1.next
        elif l2.data<l1.data:
            tail.next=l2.data
            l2=l2.next
        tail=tail.next
    if l1:
        tail.next=l1
    elif l2:
        tail.next=l2
    return dummy.next

node1=ListNode((4,6,8))
node2=ListNode([1,3])

print(mergetwolist(node1,node2))
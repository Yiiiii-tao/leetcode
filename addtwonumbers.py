class ListNode:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __repr__(self):
        return self.data
class Solution:
    def addTwoNumbers(self, l1, l2):
        L1=l1.next
        LL1=l1
        L2=l2.next
        LL2=l2
        val=(l1.data+l2.data)%10
        c=(l1.data+l2.data)//10
        l3=ListNode(val)
        L3=l3
        while(L1!=None or L2!=None or c!=0):
            if(L1==None):
                LL1.next=ListNode(0)
            else:
                L1=L1.next
            if(L2==None):
                LL2.next=ListNode(0)
            else:
                L2=L2.next
            v=(LL1.next.data+LL2.next.data+c)%10
            c=(LL1.next.data+LL2.next.data+c)//10
            L3.next=ListNode(v)
            LL1=LL1.next
            LL2=LL2.next
            L3=L3.next
        return l3


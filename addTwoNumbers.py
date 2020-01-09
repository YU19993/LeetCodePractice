class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

def printList(l1: ListNode):
    meet = 0
    ll1 = l1
    while meet == 0:
        print(ll1.val)
        if ll1.next == None:
            #print("meet")
            meet = 1
        else:
            #print("go next")
            ll1 = ll1.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        current = 0
        result = ListNode(0) # hold for head
        e1 = 0
        e2 = 0
        while e1 == 0 or e2 == 0:

            #read from l1
            if e1 == 0:
                n1 = l1.val
            else:
                n1 = 0

             #read from l2
            if e2 == 0:
                n2 = l2.val
            else:
                n2 = 0

            #check end of list
            if l1.next == None:
                e1 = 1
            else:
                l1 = l1.next

             #check end of list
            if l2.next == None:
                e2 = 1
            else:
                l2 = l2.next

            n = n1 + n2 + carry
            current = n % 10
            carry = int(n/10)
            temp = ListNode(current)

            tempNode = result
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next=temp

        if carry != 0:
            temp = ListNode(carry)
            tempNode = result
            while tempNode.next != None:
                tempNode = tempNode.next
            tempNode.next=temp

        return result.next


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

#printList(l1)
#printList(l2)

func = Solution()
printList(func.addTwoNumbers(l1, l2))

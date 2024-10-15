#below is leetcode 876, do the slightly harder two pointer approach
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def midPointer(head):
    fast = slow = head  #

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == "__main__":
    print("hi")
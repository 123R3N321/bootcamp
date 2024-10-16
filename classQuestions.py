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

#below is leetcode 206, I want to try both iterative and recursive
def iterativeRev(head):
    cur = head
    prev = None
    while cur:
        next = cur.next
        cur.next = prev

        prev = cur
        cur = next
    return prev
'''
takeaway from above qn: 
do not overcomplicate
and in python, node.next is
like treating the pointer not the object
itself
'''

#below is leetcode 143, which is actually just a combination of
# leecode 876 and 206
## approach ##
# find middle point
#rev the second half
# intersperse-connect the two halves.


#below is leetcode 36. Baby version of sudoku solver
#hash and use ..in... method of dict
# I can also just use the algo in my sudoku solver.


#below is leetcode 48
# I can think of concentric onion rotate approach
# better solution: transpose, then left-right mirror
def transpose(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

def horFlip(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n//2):
            mat[i][j], mat[i][n-j-1] = mat[i][n-j-1], mat[i][j]
def clock90Rot(mat):
    transpose(mat)
    horFlip(mat)


if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # transpose(mat)
    # horFlip(mat)
    clock90Rot(mat)
    for each in mat:
        print (each)
from csv import excel


#problem 167
def squeeze(lst, target):
    '''
    do default zero-ind then convert back
    simple two-pointer approach
    '''
    lo = 0
    hi = len(lst) - 1
    #assume len>1, at least 2
    while lo<hi:
        res = lst[lo] + lst[hi]
        if res < target:
            lo+=1

        elif res>target:
            hi-=1

        elif res == target:
            return [lo+1, hi+1]
    return [-1,-1]

#problem 75
def threeElemTetrisSort(lst):
    '''
    my mistake:
        attempted iterative solution with insert and append
        which interrupted lst order and thus failed

    hint from chatGPT:
        two pointer (actually three) in-place swap, which is prolly the simplest orthodox solution

    my idea:
        forward-backward iteration, tetris approach;
        iterate forward, find all 0s and note indices:
        eg: 1,4,5,7,8,9
        then do all "fall back", 1 becomes 0, 4 becomes 1, 7 becomes 2, and 9 becomes 3
        similarly, backward iteration, find all 2s and note indices:
        eg: 2,3,6,10 (assume 10 is final ind)
        then "fall forward", 10 stays 10, 6 becomes 9, 3 becomes 8, 2 becomes 7

        lastly, fill gap with 1s
    '''
    fCount = bCount = 0
    for i in range(len(lst)):
        num = lst[i]
        if num == 0:
            fCount+=1
        elif num == 1:
            pass
        elif num == 2:
            bCount+=1
        else:   #error
            raise Exception(f"unexpected element {num}")

    for i in range(len(lst)):
        lst[i] = 1
    for i in range(fCount):
        lst[i] = 0
    iter = -1
    for i in range(bCount):    #go backward
        lst[iter] = 2
        iter-=1

def threeElemPtrSort(lst):
    if len(lst)<=1:
        return

    hi = len(lst) - 1
    lo = iter = 0

    while iter<=hi:
        if lst[iter] == 0:
            lst[iter], lst[lo] = lst[lo], lst[iter]
            lo += 1
        elif lst[iter] == 1:
            pass
        elif lst[iter] == 2:
            lst[iter], lst[hi] = lst[hi], lst[iter]
            hi -= 1
            iter-=1
        else:
            raise Exception(f"unexpected element {lst[iter]}")

        iter += 1

# problem 238
# this problem is very, very contrived. I don like it

def standard(lst):
    '''
    this is the standard solution leetcode wants
    compute pre and post fix product
    and then multiply the complements as needed
    very ugly solution
    '''
    if len(lst)<=1:
        return lst
    if len(lst)==2:
        return [lst[1],lst[0]]
    else:   #at least 3 elems in lst
        proLst=lst.copy()
        prepro(proLst)
        postLst = lst.copy()
        postpro(postLst)

        print(proLst,'\n',postLst)

        res = []
        for i in range(len(proLst)):
            if i == 0:  #begin
                res.append(postLst[1])
            elif i == len(proLst)-1:  #end
                res.append(proLst[-2])
            else:
                print(f"\tind: {i}, product of: {proLst[i-1]} * {postLst[i+1]}")
                res.append(proLst[i-1] * postLst[i+1])
        return res

#below are helper funcs for problem238
def prepro(lst):
    if len(lst)<=1:
        return
    if len(lst)==2:
        lst[1] *= lst[0]
        return
    for i in range(1,len(lst)):
        lst[i]*=lst[i-1]

def postpro(lst):
    if len(lst)<=1:
        return
    if len(lst)==2:
        lst[0] *= lst[1]
    for i in range(len(lst)-2,-1,-1):
        lst[i]*=lst[i+1]


#week2 homework:

# leetcode 8, string to int conversion

'''
thoughts:
read string backward seems to make the most sense
we need to: store cur val
            store number of digits we have
            track what we see
            reset if needed
'''


def weirdAtoI(msg):
    for i in range(len(msg)):  # remove leading empty spaces
        char = msg[i]
        if char != ' ':
            msg = msg[i:]
            break

    digits = -1
    num = 0
    for i in range(len(msg) - 1, -1, -1):  # we go bckward in ind
        char = msg[i]
        if char.isdigit():
            digits += 1
            num += (ord(char) - 48) * (10 ** digits)
        else:
            if i == 0 and char == '+':
                pass
            elif i == 0 and char == '-':
                num = -num
            else:  # reset
                num = 0
                digits = -1

    if num > 2 ** 31 - 1:
        num = 2 ** 31 - 1
    elif num < -(2 ** 31):
        num = - (2 ** 31)

    return num
'''
conclusions:
very contrived problem. Not fun.
'''

#next, leetcode 438

'''
I can think of a dictionary solution
which will give runtime m*n where
m is size of p, n is size of s
let's see how it works

update: dic is not good for repeated letters

update: even in sliding window, move left and right most part only (assume long needle)
'''
def anaSlidingWindow(hey, needle):
    map = [0]*26
    for each in needle:
        map[ord(each)-97]+=1    #hashed map yay!

    res = []
    front = 0
    back = len(needle) - 1
    for each in hey[front:back+1]:
        map[ord(each)-97]-=1
    if checkMap(map):
        res.append(0)

    while back < len(hey)-1:
        map[ord(hey[front])-97]+=1
        front = front+1
        back = back + 1
        map[ord(hey[back])-97]-=1
        if checkMap(map):
            res.append(front)
    return res



def checkMap(lst):
    return all(x==0 for x in lst)




if __name__ == '__main__':
    print(anaSlidingWindow('baa','aa'), " should be [1]")

    print(anaSlidingWindow('abab','ab'), " should be [0,1,2]")
    print(anaSlidingWindow("cbaebabacd",'abc'), 'should be [0,6]')
    # lst = [1,2,3,4]
    # print(lst)
    #
    # res = standard(lst)
    # print(res)

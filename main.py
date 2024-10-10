
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

if __name__ == '__main__':
    print("hello")
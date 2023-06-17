def twosume2(n:list[int],target:int)->list[int]:
    l,r=0,len(n)-1
    while l<r:
        cursum=n[l]+n[r]
        if cursum>target:
            r-=1
        elif cursum<target:
            l+=1
        else:
            return [l+1,r+1]
    return []

print(twosume2([1,3,5,6,8],8))
class solution:
    def twosums(self,nums:list[int],target:int)-> list[int]:
        prevmap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[n]=i
        return


def twosums2(self,nums:list[int],target:int)-> list[int]:
        prevmap={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in prevmap:
                return [prevmap[diff],i]
            prevmap[n]=i 
        return

print(twosums2('',[1,3,5,8],8))
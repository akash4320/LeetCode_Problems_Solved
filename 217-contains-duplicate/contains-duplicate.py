class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        retBool = False
        mydict = {}
        for i in range(0,len(nums)):
            if mydict.get(str(nums[i])):
                retBool = True
                break
            else:
                mydict[str(nums[i])] = str(nums[i])

        return retBool
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        st = 1
        end = n

        while True:
            num = (st+end)//2 
            second = isBadVersion(num)
            first = isBadVersion(num-1)

            if second is True:
                if first is False:
                    return num
                else:
                    end = num
            else:
                if isBadVersion(num+1) is True:
                    return num+1
                else:
                    st = num
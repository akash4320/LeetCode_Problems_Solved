def computeSum(n: int) -> int:
    return (n*(n+1)/2)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int(computeSum(len(nums)) - sum(nums))
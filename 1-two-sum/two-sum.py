def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            return mid
    return None

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nList = nums[:]
        nList.sort()
        retList = []
    
        for i in range(0, len(nList)):
            if(nList[i] < 0):
                if binary_search(nList[i+1:len(nList)],target + abs(nList[i])) is not None:
                    retList.append(nums.index(nList[i]))
                    if nList[i] == target + abs(nList[i]):
                        retList.append(nums.index(target + abs(nList[i]),nums.index(nList[i])+1,len(nums)))
                    else:
                        retList.append(nums.index(target + abs(nList[i])))
                    break
            else:
                if binary_search(nList[i+1:len(nList)],(target - nList[i])) is not None:
                    retList.append(nums.index(nList[i]))
                    if nList[i] == target - nList[i]:
                        retList.append(nums.index(target - nList[i],nums.index(nList[i])+1,len(nums)))
                    else:
                        retList.append(nums.index(target - nList[i]))
                    break
        
        return retList
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lls = len(nums)
        for i in range(lls):
            for ii in range(lls-i-1):
                if ( nums[i] + nums[ii+i+1] ) == target:
                    output = []
                    output.append(i)
                    output.append(ii+i+1)
                    return output
        return []

nums = [2, 7, 11, 15]
target = 9

obj = Solution()
output = obj.twoSum(nums, target)
print(output)

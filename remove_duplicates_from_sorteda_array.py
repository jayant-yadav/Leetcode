from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            print(nums[i])

        return 10



if __name__ == "__main__":
    nums=[0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    k = s.removeDuplicates(nums)
    print(k)
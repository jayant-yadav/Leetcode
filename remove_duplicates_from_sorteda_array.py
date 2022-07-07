# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u_idx = 0;
        u_no = -200;
        no_uq = 0;
        for i in range(len(nums)):
            for j in range(u_idx,len(nums)): #start looking after the prev found unique element idx
                if u_no!=nums[j]:
                    u_idx = j
                    u_no = nums[j]
                    print(f'{i} {u_idx}\n')
                    break
                elif j == len(nums)-1:
                    no_uq = 1 
                else:
                    pass

            nums[i] = nums[u_idx]
            if u_idx == len(nums)-1 or no_uq == 1:
                break
        print(nums)
        return i+1

if __name__ == "__main__":
    nums=[1,1,1,1,1,2,2,2]
    s = Solution()
    k = s.removeDuplicates(nums)
    print(k)
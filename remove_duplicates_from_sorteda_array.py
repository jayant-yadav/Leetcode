from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        u_idx = 0;
        l_idx = 0;
        for i in range(len(nums)):
            # BUG: the way of checking unique element is wrong.
            # it should not compare elements
            for j in range(u_idx,len(nums)): #start looking after the prev found unique element idx
                if nums[i]!=nums[j]:
                    u_idx = j
                    print(f'{i} {u_idx}\n')
                    break
                else:
                    pass
            if i == 0:
                pass
            else:
                nums[i] = nums[u_idx]
                if u_idx == len(nums)-1:
                    break

        print(nums)
        return i

if __name__ == "__main__":
    nums=[0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    k = s.removeDuplicates(nums)
    print(k)
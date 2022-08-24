from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        l = len(digits)

        if digits[l-1] != 9:
            digits[l-1] += 1

        else:

            for i in range(l): # check how many 9s are there
                if digits[l-i-1] == 9:
                    idx = l-i-1
                else: break
            
            if idx != 0:

                digits[idx-1] +=1

                for i in range(idx,l):
                    digits[i] = 0


            else:
                # the no. is 999..
                for i in range(idx,l):
                    digits[i] = 0

                digits = [1] + digits

        return digits



if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([9,8,9]))
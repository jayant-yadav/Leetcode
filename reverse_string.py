# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/879/
from typing import  List

class Solution:
    def reverseString(self, s: List[str]) -> None:

        for i in range(int(len(s)/2)):
            a = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = a

        print(s)




            

if __name__ == '__main__':
    sol = Solution()
    sol.reverseString(["h","e","l","l","o"])
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        str1 = ""
        s = s.lower()

        for i in s:
            if i.isalnum(): 
                str1=str1+i
        if str1 == str1[::-1]:
            return True
        else:
            return False 
        

if __name__ == '__main__':
    sol = Solution()
    x=sol.isPalindrome("0P")
    print(x)
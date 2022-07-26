class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) <= len(haystack):
            
            try :
                ans = haystack.index(needle)
                return ans
            except:
                return -1 
            
        if len(needle) == 0:
            return 0

        return -1

        
if __name__ == '__main__':
    sol = Solution()
    s = "aaaa"
    t = "baa"
    print(sol.strStr(s,t))
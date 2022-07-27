class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(needle) <= len(haystack):
            
            # try :
            #     ans = haystack.index(needle)
            #     return ans
            # except:
            #     return -1 
            needle_len = len(needle)
            haystack_len = len(haystack)
            i,j = 0,0
            at = 0
            while j <= (needle_len-1) and i <= (haystack_len-1):

                # print(i,haystack[i])
                print(j,needle[j])
                if needle[j] == haystack[i] :
                    if j == 0:
                        at = i
                    
                    i+=1
                    j+=1
                else:
                    j=0
                    if at == 0:
                        i+=1
                    else:
                        i = at+1

            if j == needle_len:
                return at


        if needle_len == 0:
            return 0

        return -1

        
if __name__ == '__main__':
    sol = Solution()
    s = "mississippi"
    t = "issip"
    # s = "hello"
    # t = 'llf'
    print(sol.strStr(s,t))
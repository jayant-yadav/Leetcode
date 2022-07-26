class Solution:
    def reverse(self, x: int) -> int:

        n = int(x)
        while int(n/10) > 0:
            q = int(n/10)
            r = int(n%10)
            print(r)
            n = q
        
        return x

if __name__ == "__main__":
    sol = Solution()
    x = sol.reverse(321)
class Solution:
    def reverse(self, x: int) -> int:

        if -10 < x < 10:
            return x

        y = []
        neg = False
        if x < 0 :
            neg  = True
            x*= -1

        while True:
            y.append(int(x%10))
            x = int(x/10)
            if int(x/10) == 0:
                y.append(int(x%10))
                break

        print(y)

        x = 0


        for i in range(len(y)):
            x += y[i]
            if i < len(y)-1 :
                x *= 10 
        
        if neg == True:
            x *= -1

        if x > pow(2, 31) -1 or x < pow(-2, 31):
            x = 0
        return x

if __name__ == "__main__":
    sol = Solution()
    x = sol.reverse(-321)
    print(x)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        d1 = Counter(s)
        d2 = Counter(t)
        if d1 == d2:
            return True
        else:
            return False
                
                
if __name__ == '__main__':
    sol = Solution()
    s = "anagram"
    t = "nagatam"
    print(sol.isAnagram(s,t))
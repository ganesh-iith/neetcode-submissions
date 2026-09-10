class Solution:
    def check(self, s: str, t: str) -> bool:
        s1 = [0] * 26
        t1 = [0] * 26
        for char in s:
            s1[ord(char) - ord('a')] += 1
        
        for char in t:
            t1[ord(char) - ord('a')] += 1

        for i in range(0,26):
            if(s1[i] != t1[i]):
                 return False

        return True
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return self.check(s,t)
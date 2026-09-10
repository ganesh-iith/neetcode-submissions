class Solution:
  
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s1 = [0] * 26
        t1 = [0] * 26
        for char in s:
            s1[ord(char) - ord('a')] += 1
        
        for char in t:
            t1[ord(char) - ord('a')] += 1

        return s1==t1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq = [0] * 26
        for i in range(len(s)):
            ls = s[i]
            lt = t[i]
            freq[ord(ls) - ord('a')] = freq[ord(ls) - ord('a')] + 1
            freq[ord(lt) - ord('a')] = freq[ord(lt) - ord('a')] - 1
        
        return freq == [0] * 26
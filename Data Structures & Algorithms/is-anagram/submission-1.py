class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq = [0] * 26
        for ls in s:
            freq[ord(ls) - ord('a')] = freq[ord(ls) - ord('a')] + 1
        for lt in t:
            freq[ord(lt) - ord('a')] = freq[ord(lt) - ord('a')] - 1
        
        return freq == [0] * 26
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        freq_s = [0] * 26
        freq_t = [0] * 26
        for ls in s:
            freq_s[ord(ls) - ord('a')] = freq_s[ord(ls) - ord('a')] + 1
        for lt in t:
            freq_t[ord(lt) - ord('a')] = freq_t[ord(lt) - ord('a')] + 1
        
        return freq_s == freq_t
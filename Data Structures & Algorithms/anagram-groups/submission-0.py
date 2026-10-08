class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        anagrams = []
        for word in strs:
            key = str(self.to_anagram_dict(word))
            if anagram_dict.get(key) is None:
    
                anagram_dict[key] = []
    
            anagram_dict[key].append(word)

        for value in anagram_dict.values():
            anagrams.append(value)

        return anagrams
    
    def to_anagram_dict(self, str1) -> bool:
        str_dict = {}
        for letter in "abcdefghijklmnopqrstuvwxyz":
            str_dict[letter] = 0
        for letter in str1:
            str_dict[letter] += 1
        
        return str_dict
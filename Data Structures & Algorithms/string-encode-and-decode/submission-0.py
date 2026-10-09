class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""

        for word in strs:
            for letter in word:
                if letter == ",":
                    encoding += r"\,"
                    continue
                
                if letter == "\\":
                    encoding += r"\\"
                    continue
                
                encoding += letter
            
            encoding += ","
        
        return encoding


    def decode(self, s: str) -> List[str]:
        decoding = []
        word = ""

        i = 0
        while i < len(s):
            letter = s[i]
            i += 1
            if letter == "\\" and i < len(s):
                next_letter = s[i]
                if next_letter == "\\":
                    word += "\\"
                    i += 1
                    
                if next_letter == ",":
                    word += ","
                    i += 1
                continue
            
            if letter == ",":
                decoding.append(word)
                word = ""
                continue
            
            word += letter

        return decoding
                
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += word + "€"

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        for i in range(len(s)):
            if s[i] != "€":
                word += s[i]
            
            else:
                res.append(word)
                word = ""

        return res
            

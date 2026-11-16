class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t):
            return False

        letters_s = {}
        letters_t = {}

        for letters in s:
            if letters in letters_s:
                letters_s[letters] += 1
            else:
                letters_s[letters] = 1

        for letters in t:
            if letters in letters_t:
                letters_t[letters] += 1
            else:
                letters_t[letters] = 1

        return letters_t == letters_s
        
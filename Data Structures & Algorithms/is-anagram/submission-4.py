class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}

        for char in s:
            if char not in t:
                return False
            if char in letters_s:
                letters_s[char] += 1
            else:
                letters_s[char] = 1

        for char in t:
            if char not in s:
                return False
            if char in letters_t:
                letters_t[char] += 1
            else:
                letters_t[char] = 1

       
        for letters in letters_s:
            if letters_s[letters] != letters_t[letters]:
                return False

        return True

        
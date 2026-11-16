class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        new_word = ""

        while p1 < len(word1) or p2 < len(word2):

            if p1 < len(word1):
                new_word += word1[p1] 
                p1 += 1

            if p2 < len(word2):
                new_word += word2[p2]
                p2 += 1

        return new_word
        

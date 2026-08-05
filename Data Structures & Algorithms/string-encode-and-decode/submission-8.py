class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += f"{len(word)}#{word}"

        return s

    #since spaces can be strings, need to keep track of the strings length?
    

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find the # separating the length from the word
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word_start = j + 1
            word_end = word_start + length
            result.append(s[word_start:word_end])

            i = word_end

        return result
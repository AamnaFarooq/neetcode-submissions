class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        same = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in same:
                same[key].append(word)
            else:
                same[key] = [word]

        return list(same.values())
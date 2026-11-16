class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = []
        same = {}
        i = -1
        lengths = sorted(strs)
        final = []
        
        for words in lengths:
            store.append("".join(sorted(words)))
        print(store)
        for words in store:
            i += 1
            if words in same:
                same[words].append(lengths[i])
            else:
                same[words] = [lengths[i]]

        for keys in same:
            final.append(same[keys])

        return final
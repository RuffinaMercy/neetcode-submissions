class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs :
            sorted_word = ''.join(sorted(s))
            hashmap[sorted_word].append(s)
        return list(hashmap.values())

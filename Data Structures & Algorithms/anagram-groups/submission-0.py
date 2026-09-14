class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for s in strs:
            sorted_word = ''.join(sorted(s))
            hashMap[sorted_word].append(s)
        return list(hashMap.values())

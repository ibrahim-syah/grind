class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupMap = defaultdict(list)

        for s in strs:
            charsets = [0] * 26
            for c in s:
                charsets[ord(c) - ord('a')] += 1
            groupMap[tuple(charsets)].append(s)
        
        return list(groupMap.values())
        
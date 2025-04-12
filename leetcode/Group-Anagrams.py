class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = defaultdict(list)

        for s in strs:
            charIndices = [0] * 26
            for c in s:
                idx = ord(c) - ord(\a\)
                charIndices[idx] += 1
            mapped[tuple(charIndices)].append(s)

        return list(mapped.values())

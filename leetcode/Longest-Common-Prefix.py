class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = \\
        for i in range(len(strs[0])):
            currPrefix = strs[0][:i+1]
            for s in strs:
                if i == len(s) or s[:i+1] != currPrefix:
                    return prefix
            prefix = currPrefix

        return prefix
        

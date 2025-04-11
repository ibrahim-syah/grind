class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) <= 0:
            return \\

        shortestWordLength = math.inf
        for word in strs:
            shortestWordLength = min(shortestWordLength, len(word))

        if shortestWordLength <= 0:
            return \\

        result = \\
        for i in range(shortestWordLength):
            firstWord = strs[0][:i+1]
            for word in strs:
                if word[:i+1] != firstWord:
                    return result
            result = firstWord

        return result
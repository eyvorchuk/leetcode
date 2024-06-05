class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        min_length = len(strs[0])
        for s in strs[1:]:
            min_length = min(min_length, len(s))

        for i in range(min_length):
            in_all = True
            for s in strs[1:]:
                if s[i] != strs[0][i]:
                    in_all = False
                    break
            if in_all:
                common += strs[0][i]
            else:
                break
        return common

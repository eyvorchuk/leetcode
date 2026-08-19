class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"}": "{", "]": "[", ")": "("}
        last = ""
        for p in s:
            if p in ["{", "[", "("]:
                last += p
            else:
                if len(last) == 0 or pairs[p] != last[-1]:
                    return False
                last = last[:-1]
        return last == ""


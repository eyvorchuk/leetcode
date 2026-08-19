class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        i = 1
        while i < len(words):
            if collections.Counter(words[i]) == collections.Counter(words[i-1]):
                words.remove(words[i])
            else:
                i += 1
        return words

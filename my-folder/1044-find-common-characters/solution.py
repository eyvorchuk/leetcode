class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        charCounts = []
        for w in words:
            count = {}
            for c in w:
                if c not in count:
                    count[c] = 1
                else:
                    count[c] += 1
            charCounts.append(count)
        common = []
        firstWord = charCounts[0]
        for letter in firstWord:
            inAll = True
            minCount = firstWord[letter]
            for word in charCounts[1:]:
                if letter not in word:
                    inAll = False
                    break
                else:
                    minCount = min(minCount, word[letter])
            if inAll:
                common.extend(letter * minCount)
        return common
        

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_count = dict(collections.Counter(words[0]))
        for char in char_count:
            for word in words[1:]:
                curr_char_count = collections.Counter(word)
                if char not in curr_char_count.keys():
                    char_count[char] = 0
                    break
                elif curr_char_count[char] < char_count[char]:
                    char_count[char] = curr_char_count[char]
        common = []
        for (char, count) in char_count.items():
            for c in range(count):
                common.append(char)
        return common

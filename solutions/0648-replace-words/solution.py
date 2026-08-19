class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort()
        sentence_words = sentence.split(" ")
        for word in sentence_words:
            for root in dictionary:
                if word.startswith(root):
                    sentence = sentence.replace(word, root, 1)
                    break
        return sentence

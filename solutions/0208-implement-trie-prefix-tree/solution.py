class Trie:

    def __init__(self):
        self.children = {}
        self.letter = ""

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            if word[i] in curr.children.keys():
                curr = curr.children[word[i]]
            else:
                curr.children[word[i]] = Trie()
                curr = curr.children[word[i]]
                curr.letter = word[i]
        curr.children["_end_"] = Trie()
        curr = curr.children["_end_"]
        curr.letter = "_end_"
            

    def search(self, word: str) -> bool:
        curr = self
        for i in range(len(word)):
            if word[i] in curr.children.keys():
                curr = curr.children[word[i]]
            else:
                return False
        return "_end_" in curr.children.keys()
            

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for i in range(len(prefix)):
            if prefix[i] in curr.children.keys():
                curr = curr.children[prefix[i]]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

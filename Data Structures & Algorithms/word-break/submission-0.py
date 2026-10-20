class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.eow = True

    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.eow


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        trie = Trie()

        for word in wordDict:
            trie.insert(word)
        n = len(s)
        dp = {}

        def wbreak(key):
            if len(key) == 0:
                return True
            if key in dp:
                return dp[key]
            for i in range(len(key) + 1):
                first_part = key[:i]
                second_part = key[i:]
                dp[key] = trie.search(first_part) and wbreak(second_part)
                if dp[key]:
                    return True

            return False

        return wbreak(s)

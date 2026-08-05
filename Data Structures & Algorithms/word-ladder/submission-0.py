class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # solve using BFS, add the beginWord in the q along with level
        # make set of wordlist
        # popleft the word, check in stack, remove from stack and change every character

        if endWord not in wordList:
            return 0

        q = deque([(beginWord, 1)])
        size = len(beginWord)
        st = set(wordList)
        while q:

            word, level = q.popleft()

            if word == endWord:

                return level

            for i in range(len(word)):
                for ch in range(ord("a"), ord("z") + 1):

                    replacedChArray = list(word)

                    replacedChArray[i] = chr(ch)

                    replacedWord = "".join(replacedChArray)

                    if replacedWord in st:
                        st.remove(replacedWord)
                        q.append((replacedWord, level + 1))

        return 0

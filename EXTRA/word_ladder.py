from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set=set(wordList)

        if endWord not in word_set:
            return 0
        queue=deque([(beginWord,1)])
        visited={beginWord}

        while queue:
            word,steps=queue.popleft()
            if word==endWord:
                return steps
            for i in range (len(word)):
                letters=list(word)

                for ch in "abcdefghijklmnopqrstuvwxyz":
                    letters[i]=ch
                    new_word="".join(letters)

                    if new_word in word_set and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word,steps + 1))
        return 0        
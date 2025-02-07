from collections import deque
from typing import List
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Using set for O(1) lookups
        allWords = set(wordList)

        # If endWord is not in wordList
        if endWord not in allWords:
            return 0

        # Initialise queue
        q = deque([(1, beginWord)])

        # Alphabet letters for transformations
        alphabet = string.ascii_lowercase

        # BFS
        while q:
            level, word = q.popleft()

            # Return level if current word is endWord
            if word == endWord:
                return level

            for i in range(len(word)):
                for letter in alphabet:
                    newWord = word[:i] + letter + word[i+1:]
                    
                    if newWord in allWords:
                        q.append((level + 1, newWord))
                        allWords.discard(newWord)  # Avoid visiting the same word again

        # Return 0 if no transformation sequence exists
        return 0

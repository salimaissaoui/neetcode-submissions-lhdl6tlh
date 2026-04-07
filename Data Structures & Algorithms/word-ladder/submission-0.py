from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList = set(wordList)
        queue = deque()
        queue.append((beginWord, 1))
        visited = {beginWord}

        while queue:
            curr_word, res = queue.popleft()
            if curr_word == endWord:
                return res
            for i in range(len(curr_word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    temp = curr_word[:i] + char + curr_word[i+1:]
                    if temp in wordList and temp not in visited:
                        queue.append((temp, res + 1))
                        visited.add(temp)
        return 0
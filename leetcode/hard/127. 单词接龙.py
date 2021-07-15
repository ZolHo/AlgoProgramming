class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        worddict = {}
        wordList.append(beginWord)
        for w in wordList:
            worddict[w] = set()
            for i in range(len(w)):
                temp = w[0:i] + '*' + w[i + 1:]
                worddict[w].add(temp)
        que = [[beginWord, 1]]

        while len(que) > 0:
            temp = que.pop(0)
            if temp[0] == endWord:
                return temp[1]
            for w in list(wordset):
                for i in worddict[temp[0]]:
                    if i in worddict[w]:
                        que.append([w, temp[1] + 1])
                        if w in wordset:
                            wordset.remove(w)
        return 0
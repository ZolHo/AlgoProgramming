class Trie:

    def __init__(self):
        self.node_sum = 0
        self.node_dict = {}


    def insert(self, word: str) -> None:
        if len(word)==0 :
            self.node_sum+=1
            return
        if word[0] in self.node_dict :
            nextT = self.node_dict[word[0]]
            nextT.insert(word[1:])
        else :
            newT = Trie();
            self.node_dict[word[0]] = newT;
            newT.insert(word[1:])


    def search(self, word: str) -> bool:
        if len(word)==0:
            return True if self.node_sum!=0 else False
        if word[0] in self.node_dict :
            return self.node_dict[word[0]].search(word[1:])
        else :
            return False


    def startsWith(self, prefix: str) -> bool:
        if len(prefix)==0:
            return True
        if prefix[0] in self.node_dict :
            return self.node_dict[prefix[0]].startsWith(prefix[1:])
        else :
            print(prefix)
            return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
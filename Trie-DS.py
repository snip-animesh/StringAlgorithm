class Trie:
    head={}

    def insert(self,word):
        current_node=self.head

        for ch in word:
            if ch not in current_node:
                current_node[ch]={}
            current_node=current_node[ch]
        current_node['*']=True

    def search(self,word):
        current_node=self.head

        for ch in word:
            if ch not in current_node:
                return False
            current_node=current_node[ch]
        if "*" in current_node:
            return True
        else:
            return False

    # def printf(self):
    #     print(self.head)
        
        
trie=Trie()
trie.insert("hi")
trie.insert("hello")
trie.insert('apple')
print(trie.search('hi'))
print(trie.search('Yahabibi'))
# trie.printf()


# --> video to understand the logic - https://www.youtube.com/watch?v=AXjmTQ8LEoI&t=977s
# --> video to implement code - https://www.youtube.com/watch?v=o6563NNbdtg&t=202s

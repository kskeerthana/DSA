class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.isTerminating = False

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def charIndex(self,char):
        return ord(char) - ord('a')

    def insert(self,value):
        value_obj = self.root
        # value = value.lower()
        value_len = len(value)
        for i in range(value_len):
            sylIndex = self.charIndex(value[i])
            
            if not value_obj.children[sylIndex]:
                value_obj.children[sylIndex] = TrieNode()
            value_obj = value_obj.children[sylIndex]
        value_obj.isTerminating = True        
    
    def search(self,search_value):
        search_obj = self.root
        val_len = len(search_value)
        for char in range(val_len):
            char_index = self.charIndex(search_value[char])
            if not search_obj.children[char_index]:
                return False
            search_obj = search_obj.children[char_index]   
        return True        

trie = Trie()
trie.insert('data')
trie.insert('structures')
trie.insert('str')
trie.insert('trie')
# trie.search('tre')
print(trie.search('z'))
# trie.search('tur')
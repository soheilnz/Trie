# Trie tree:
# { a trie-tree is a tree-based data structure that organizes information in a hierarchy.(each node can have more than
# 2 children.)
#   it's typically used to store or search strings in a space and time efficient way.
#   Any node in a trie can store non-repetitive multiple characters.
#   Every node stores link of the next character of string.
#   Every node keeps track of 'end of string'.}
# WHY WE NEED TRIE:
# {- spelling checker
# - auto-completion}


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

# Time : O(1)
# Space : O(1)


class Trie:
    def __init__(self):
        self.rootNode = TrieNode()

    def insertString(self, word):
        current = self.rootNode
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("Success")

# Time : O(m) m = len(word)
# space : O(m)

    def searchString(self, word):
        currentNode = self.rootNode
        for i in word:
            node = currentNode.children.get(i)
            if node is None:
                return False
            currentNode = node

        if currentNode.endOfString is True:
            return True
        else:
            return False

# Time: O(m)
# Space: O(1)

#Deleting starts from the leaf node.


def deleteString(root, word, index):
    ch = word[index]
    currentNode = root.children.get(ch)
    canDelete = False

    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index + 1)
        return False

    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True

    if currentNode.endOfString is True:
        deleteString(currentNode, word, index + 1)
        return False

    canDelete = deleteString(currentNode, word, index + 1)
    if canDelete is True:
        root.children.pop(ch)
        return True
    else:
        return False


newTrie = Trie()
newTrie.insertString("APP")
newTrie.insertString("APPL")
# print(newTrie.searchString("APPL"))
deleteString(newTrie.rootNode, "APP", 0)
print(newTrie.searchString("APP"))

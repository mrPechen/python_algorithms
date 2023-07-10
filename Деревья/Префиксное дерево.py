"""
Префиксное дерево - это структура данных для хранения набора строк.
Представляет собой подвешенное дерево с символами на ребрах.
Строки являются последовательной записью всех символов хранящихся
на ребрах.

Add - Сложность O(s), где S - это длина строки.
Search - Сложность O(s), где S - это длина строки.

Эта структура очень гибкая. Например, можно вывести все слова в
отсортированном порядке. Сложность O(k), где K - это сумма длин всех строк.
Так же эту структуру данных можно использовать вместо бинарного дерева
или хэш таблицы.
"""

char_size = 26


class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}


class Trie(object):

    def __init__(self):
        self.root = TrieNode("")

    def add(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    def dfs(self, node, pre):

        if node.is_end:
            self.output.append((pre + node.char))

        for child in node.children.values():
            self.dfs(child, pre + node.char)

    def search(self, x):

        node = self.root

        for char in x:
            if char in node.children:
                node = node.children[char]
            else:

                return []

        self.output = []
        self.dfs(node, x[:-1])

        return self.output


tr = Trie()
tr.add('here')
tr.add('hear')
tr.add('he')
tr.add('hello')
tr.add('how')
print(tr.search('he'))
print(tr.search('her'))
print(tr.search('hel'))
print(tr.search('how'))
print(tr.search('he'))
print(tr.search('her'))
print(tr.search('hel'))
print(tr.search('how'))
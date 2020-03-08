import time
from itertools import chain


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}

    def insert(self, key: str):
        node = self
        for letter in key:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = key


def searchRecursive(
    node: TrieNode, symbol: str, pattern: str, previous: (int,), cost: int
):
    _filter = lambda x: len(x)
    row = (previous[0] + 1,)
    for column in range(1, len(pattern) + 1):
        row += min(
            row[column - 1] + 1,
            previous[column] + 1,
            previous[column - 1] + int(pattern[column - 1] != symbol)
        ),

    return (
        ((node.word, row[-1]),) if row[-1] <= cost and node.word is not None else ()
    ) + tuple(chain(
        *filter(_filter, tuple(searchRecursive(v, k, pattern, row, cost) for k, v in node.children.items())))
        if min(row) <= cost else ())


def levenshtein(word1, word2):
    columns = len(word1) + 1
    rows = len(word2) + 1

    # build first row
    currentRow = [0]
    for column in range(1, columns):
        currentRow.append(currentRow[column - 1] + 1)

    for row in range(1, rows):
        previousRow = currentRow
        currentRow = [previousRow[0] + 1]

        for column in range(1, columns):

            insertCost = currentRow[column - 1] + 1
            deleteCost = previousRow[column] + 1

            if word1[column - 1] != word2[row - 1]:
                replaceCost = previousRow[column - 1] + 1
            else:
                replaceCost = previousRow[column - 1]

            currentRow.append(min(insertCost, deleteCost, replaceCost))

    return currentRow[-1]


def search(words, pattern, maxCost):
    _results = ()
    for word in words:
        cost = levenshtein(pattern, word)
        if cost <= maxCost:
            _results += ((word, cost),)
    return _results


test_case = "baleful"
mutations = 2
with open("/usr/share/dict/words", "rt") as fid:
    dictionary = fid.read().split()
trie = TrieNode()
for word in dictionary:
    trie.insert(word)


start = time.time()
matches = search(dictionary, test_case, mutations)
for result in matches:
    print(result)

simple_search = (time.time() - start)
start = time.time()

matches = tuple(chain(*chain(
    searchRecursive(node, symbol, test_case, tuple(range(len(test_case) + 1)), mutations)
    for symbol, node in trie.children.items()
)))

for result in matches:
    print(result)
trie_search = time.time() - start

print(f"""
    Simple search: {int(simple_search*1000)/1000} s
    Trie search: {int(trie_search*1000)/1000} s
    Speedup: {int(simple_search/trie_search)}x
""")


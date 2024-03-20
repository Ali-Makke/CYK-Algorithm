from itertools import product

# enter your grammar rules here (Must be in Chomsky Normal Form(CNF))
Rules = {
    "S": [("A", "B"), ("B", "C")],
    "A": [("B", "A"), "a"],
    "B": [("C", "C"), "b"],
    "C": [("A", "B"), "a"]
}

# input the starting non-terminal here:
start = "S"
# input word here
word = "b a a b a".split()

wordLen = len(word)
chart = [[list() for _ in range(wordLen)] for _ in range(wordLen)]

# fills the first raw with the possible non-terminals of the terminals in the given word
i = 0
for letter in word:
    for key in Rules:
        for value in Rules[key]:
            if letter in value:
                chart[0][i].append(key)
    i += 1


def isInGrammar(list_Product, level, k):
    for tupl in list_Product:
        for key in Rules:
            if tupl in Rules[key]:
                chart[level + 1][k].append(key)


memo = {}
# helps the inner loops(traverser the chart all in all)
level = -1
for j in range(wordLen, -1, -1):
    level += 1
    # iterates through the cells from left to right
    # selects the next cell for each outer loop(for each j)
    for k in range(j - 1):
        # Gets all relevant combinations of previous relevant cells
        for p in range(level + 1):
            if all(not sub_list for sub_list in chart[p][k]) or all(
                    not sub_list for sub_list in chart[level - p][p + k + 1]):
                continue
            list1, list2 = chart[p][k], chart[level - p][p + k + 1]
            list_Product = tuple(product(list1, list2))
            if memo.get(list_Product) is not None:
                chart[level + 1][k].append(memo[list_Product])
                continue
            isInGrammar(list_Product, level, k)
            memo.update({list_Product: ', '.join(chart[level + 1][k])})

# prints true if the word is valid in your grammar
print(start in chart[wordLen - 1][0] or start in [item.strip() for item in chart[wordLen - 1][0][1].split(',') if
                                                  item.strip()])

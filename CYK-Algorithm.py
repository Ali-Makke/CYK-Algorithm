from itertools import product
#enter your grammar rules here (Must be in Chomsky Normal Form(CNF))
Rules = {
    "S": [("A", "B"), ("B", "C")],
    "A": [("B", "A"), "a"],
    "B": [("C", "C"), "b"],
    "C": [("A", "B"), "a"]
}
#input the starting non-terminal here:
start = "S"
#input word here
word = "b a a b a".split()

wordLen = len(word)
chart = [[set() for _ in range(wordLen)] for _ in range(wordLen)]

# fills the first raw with the possible non-terminals of the terminals in the given word
for i, letter in enumerate(word):
    for key, value in Rules.items():
        for v in value:
            if letter in v:
                chart[0][i].add(key)


def isInGrammar(list_Product, level, k):
    for tupl in list_Product:
        for key in Rules:
            if tupl in Rules[key]:
                chart[level + 1][k].add(key)


# helps the inner loops(traverser the chart all in all)
for level in range(wordLen - 1):
    for rowCell in range(wordLen - level - 1):
        # Gets all relevant combinations of previous relevant cells
        for cell in range(level + 1):
            if not chart[cell][rowCell] or not chart[level - cell][cell + rowCell + 1]:
                continue
            list_Product = product(chart[cell][rowCell], chart[level - cell][cell + rowCell + 1])
            isInGrammar(list_Product, level, rowCell)

# prints true if the word is valid in your grammar
if start in chart[wordLen - 1][0]:
    print("True -> Your sentence is valid")
else:
    print("False -> Your sentence is NOT valid")

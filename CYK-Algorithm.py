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

# fills the first row with the possible non-terminals of the terminals in the given word
i = 0
for letter in word:
    for key in Rules:
        for value in Rules[key]:
            if letter in value:
                chart[0][i].add(key)
    i += 1


def isInGrammar(letterList, level, rowCell):
    for tupl in letterList:
        for key in Rules:
            if tupl in Rules[key]:
                chart[level + 1][rowCell].add(key)


# helps the inner loops(traverser the chart all in all)
for level in range(wordLen - 1):
    # iterates through the rows from longest row(first row) to shortest row(last row)
    # moves to the next row for each outer loop(for each level)
    for rowCell in range(wordLen - level - 1):
        # Gets all relevant combinations of previous relevant cells
        for cell in range(level + 1):
            #skips a loop if one of the product cells is empty
            if not chart[cell][rowCell] or not chart[level - cell][cell + rowCell + 1]:
                continue
            list_Product = product(chart[cell][rowCell], chart[level - cell][cell + rowCell + 1])
            isInGrammar(list_Product, level, rowCell)

#prints true if the word is valid in your grammar
print(start in chart[wordLen - 1][0], "-> your word is valid for this grammar")

#shows the chart after filled:
#for row in chart:
#    print(row)

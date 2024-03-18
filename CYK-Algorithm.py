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
chart = [[list() for _ in range(wordLen)] for _ in range(wordLen)]

# fills the first raw with the possible non-terminals of the terminals in the given word
i = 0
for letter in word:
    for key in Rules:
        for value in Rules[key]:
            if letter in value:
                chart[0][i].append(key)
    i += 1


def isInGrammar(letterList, l, k1):
    for tupl in letterList:
        for key0 in Rules:
            if tupl in Rules[key0]:
                chart[l + 1][k1].append(key0)


# helps the inner loops(traverser the chart all in all)
level = -1
for j in range(wordLen, -1, -1):
    level += 1
    # iterates through the rows from longest row(first row) to shortest row(last row)
    # moves to the next row for each outer loop(for each j)
    for k in range(j - 1):
        for p in range(level + 1):
            list1, list2 = chart[p][k], chart[level - p][p + k + 1]
            isInGrammar(list(product(list1, list2)), level, k)

#prints true if the word is valid in your grammar
print(start in chart[wordLen - 1][0], "-> your word is valid for this grammar")

#shows the chart after filled:
#for row in chart:
#    print(row)

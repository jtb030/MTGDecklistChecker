    # # Compare each decklist with every other decklist
    # decklistKeys = list(newDecklistDict.keys())
    # for i in range(len(decklistKeys)):
    #     for j in range(i + 1, len(decklistKeys)):
    #         deck1Name = decklistKeys[i]
    #         deck2Name = decklistKeys[j]
    #         print(f"Comparing decklists: {deck1Name} with {deck2Name}")
    #         duplicateFinder(newDecklistDict[deck1Name], newDecklistDict[deck2Name])
    #         equivalents = duplicateFinder(newDecklistDict[deck1Name], newDecklistDict[deck2Name])
    #         masterDuplicates[(deck1Name, deck2Name)] = equivalents
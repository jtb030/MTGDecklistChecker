#########################
#FUNCTION DECLARATIONS
#########################

def createDecklistDict():
    try:
        # Prompt the user to enter names of arrays
        # Each Deck/List assigned as own array
        # Creates Dynamic # of arrays based on user input
        
        deckNamesIn = input("Enter the names of the arrays, separated by commas: ")
        if not deckNamesIn.strip():
            raise ValueError("Array names cannot be empty.")
        deckNamesList = [name.strip() for name in deckNamesIn.split(',') if name.strip()]
        
        # Create a dictionary to hold the arrays
        decklistDict = {}
        
        for name in deckNamesList:
            if name:
                decklistDict[name] = [0] # Initialize arrays with default values (e.g., zeros)
        
        return decklistDict
    
    except ValueError as e:
        print(f"Invalid input: {e}")
        return {}

def listInput():

    print("\nEnter/Paste Decklist (Each Item Should Be Separated by a Newline)")
    # print("Each card should be separated by a new line")
    print("To End Input: \n\t Enter Blank Line \n\t Input Ctrl+D (Mac/OS)/Ctrl+Z+Enter (Windows)")
    deckListInput = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        deckListInput.append(line)

    #TEST LINE
    # print(deckListInput)

    return deckListInput

def duplicateFinder(deck1, deck2):
    # Function to compare each item in deck1 with every item in deck2
    duplicates = []
    for item1 in deck1:
        for item2 in deck2:
            print(f"Comparing {item1} with {item2}")
            if item1 == item2:
                duplicates.append(item1)
    return duplicates


#########################
#MAIN LOGIC
#########################

if __name__ == "__main__":
    newDecklistDict = createDecklistDict() #Create decklist dict with names & empty values
    masterDuplicates = {}
    # Display the created arrays
    for name, array in newDecklistDict.items(): #Fill each decklist with values gathered from user input
        newDecklistDict[name] = listInput()


    # Compare each decklist with every other decklist
    decklist_names = list(newDecklistDict.keys())
    for i in range(len(decklist_names)):
        for j in range(i + 1, len(decklist_names)):
            deck1_name = decklist_names[i]
            deck2_name = decklist_names[j]
            print(f"Comparing decklists: {deck1_name} with {deck2_name}")
            equivalents = duplicateFinder(newDecklistDict[deck1_name], newDecklistDict[deck2_name])
            for item in equivalents:
                if item not in masterDuplicates:
                    masterDuplicates[item] = set()
                masterDuplicates[item].update([deck1_name, deck2_name])

    # Print the stored equivalent values for each pair of decklists
    for decks, equivalents in masterDuplicates.items():
        deck1_name = decks
        deck2_name = decks
        print(f"Equivalent items in {deck1_name} and {deck2_name}: {equivalents}")

    # Print the master list of equivalents
    print("\nMaster list of equivalents found:")
    for item, decks in masterDuplicates.items():
        print(f"Item {item} found in {', '.join(decks)}")
import os

#########################
#FUNCTION DECLARATIONS
#########################

def createDecklistDict():
    try:
        # Prompt the user to enter names of arrays
        # Each Deck/List assigned as own array
        # Creates Dynamic # of arrays based on user input
        
        deckNamesIn = input("Enter the names of the deck lists to check, separated by commas: ")
        if not deckNamesIn.strip():
            raise ValueError("Names cannot be empty. :(")
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
    print("To End Input: \n\t Enter two consecutive blank lines \n\t Or use Ctrl+D (Mac/Unix) / Ctrl+Z+Enter (Windows)")
    deckListInput = []
    empty_line_count = 0
    while True:
        try:
            line = input().strip()
            if not line:
                empty_line_count += 1
                if empty_line_count == 2:
                    break
            else:
                empty_line_count = 0
                deckListInput.append(line)
        except EOFError:
            break

    # Remove any trailing empty lines
    while deckListInput and not deckListInput[-1]:
        deckListInput.pop()

    return deckListInput

def duplicateFinder(deck1, deck2):
    # Function to compare each item in deck1 with every item in deck2
    duplicates = []
    for item1 in deck1:
        for item2 in deck2:
            # print(f"Comparing {item1} with {item2}")  # Commented out
            if item1 == item2:
                duplicates.append(item1)
    return duplicates

def save_results_to_file(masterDuplicates, decklist_names):
    # Function to optionally save results to a file
    filename = "duplicate_results.txt"
    with open(filename, 'w') as f:
        f.write("Master list of equivalents found:\n")
        for item, decks in masterDuplicates.items():
            ordered_decks = [deck for deck in decklist_names if deck in decks]
            count = len(ordered_decks)
            f.write(f"{item} found {count} time{'s' if count > 1 else ''} in {', '.join(ordered_decks)}\n")
    print(f"Results saved to {filename}")


#########################
#MAIN LOGIC
#########################

if __name__ == "__main__":
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
    
    newDecklistDict = createDecklistDict() #Create decklist dict with names & empty values
    masterDuplicates = {}
    decklist_names = list(newDecklistDict.keys())  # Preserve the order of entered decklists

    # Display the created arrays
    for name, array in newDecklistDict.items(): #Filleach decklist with values gathered from user input
        newDecklistDict[name] = listInput()


    # Compare each decklist with every other decklist
    for i in range(len(decklist_names)):
        for j in range(i + 1, len(decklist_names)):
            deck1_name = decklist_names[i]
            deck2_name = decklist_names[j]
            # print(f"Comparing decklists: {deck1_name} with {deck2_name}")  # Commented out
            equivalents = duplicateFinder(newDecklistDict[deck1_name], newDecklistDict[deck2_name])
            for item in equivalents:
                if item not in masterDuplicates:
                    masterDuplicates[item] = set()
                masterDuplicates[item].update([deck1_name, deck2_name])

    # Print the stored equivalent values for each pair of decklists
    for i in range(len(decklist_names)):
        for j in range(i + 1, len(decklist_names)):
            deck1_name = decklist_names[i]
            deck2_name = decklist_names[j]
            equivalents = [item for item, decks in masterDuplicates.items() if deck1_name in decks and deck2_name in decks]
            if equivalents:
                print(f"Equivalent items in {deck1_name} and {deck2_name}: {equivalents}")

    # Print the master list of equivalents
    print("\nMaster list of equivalents found:")
    for item, decks in masterDuplicates.items():
        ordered_decks = [deck for deck in decklist_names if deck in decks]
        count = len(ordered_decks)
        print(f"{item} found {count} time{'s' if count > 1 else ''} in {', '.join(ordered_decks)}")
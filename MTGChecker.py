import sys

def createDecklistDict():
    try:
        # Prompt the user to enter names of arrays
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
    
def fillDecklists(decklistName):
    deckListName = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        deckListName.append(line)



def listInput():
    # print("Enter/Past decklist.\n")
    deckListInput = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        deckListInput.append(line)

    #TEST LINE
    print(deckListInput)

    return deckListInput


    #loop = True
    
    # numLists = int(input("How many lists are you checking?"))
    # if numLists <= 2:
    #     raise ValueError("Must check at least 2 lists.")

    # for i in range(numLists):
    
    # while (loop): 
        
    #     loopUserInput = input("Do you have more lists to enter? Y/N")
    #     loopUserInput = loopUserInput.upper()
    #     if(loopUserInput == "N"):
    #         exit

if __name__ == "__main__":

    newDecklistDict = createDecklistDict()

    # Display the created arrays
    for name, array in newDecklistDict.items():
        print(f"{name}: {array}")
        listInput(name)
        print(name) 

    print("Enter/Paste First decklist.\n")
    listInput()



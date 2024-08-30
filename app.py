from flask import Flask, render_template, request
from MTGChecker import duplicateFinder

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        deck_names = request.form.get('deck_names')
        deck_lists = request.form.get('deck_lists')

        # Process deck names
        deck_names_list = [name.strip() for name in deck_names.split(',') if name.strip()]
        
        # Process deck lists
        deck_lists_dict = {}
        current_deck = None
        for line in deck_lists.split('\n'):
            line = line.strip()
            if line in deck_names_list:
                current_deck = line
                deck_lists_dict[current_deck] = []
            elif current_deck and line:
                deck_lists_dict[current_deck].append(line)

        # Find duplicates
        masterDuplicates = {}
        for i in range(len(deck_names_list)):
            for j in range(i + 1, len(deck_names_list)):
                deck1_name = deck_names_list[i]
                deck2_name = deck_names_list[j]
                equivalents = duplicateFinder(deck_lists_dict[deck1_name], deck_lists_dict[deck2_name])
                for item in equivalents:
                    if item not in masterDuplicates:
                        masterDuplicates[item] = set()
                    masterDuplicates[item].update([deck1_name, deck2_name])

        # Prepare results
        for item, decks in masterDuplicates.items():
            ordered_decks = [deck for deck in deck_names_list if deck in decks]
            count = len(ordered_decks)
            results.append(f"{item} found {count} time{'s' if count > 1 else ''} in {', '.join(ordered_decks)}")

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

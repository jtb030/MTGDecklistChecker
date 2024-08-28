MTGChecker README

HIGH-LEVEL OVERVIEW
	This script was designed to function similar to how conditional formatting would work in Microsoft Excel/Google Sheets. It's purpose is to:
	Take in multiple deck lists, 
	Compare all the lists
	Find any duplicates (cards found in multiple lists)
	Spit out a master list of any cards found, the number of occurrences, & their locations



INSTRUCTIONS
1. Run Script
2. Enter names for the lists they are checking
3. Enter deck lists to check
	> This can be typed manually or copy/pasted
4. Findings should be printed in console



EXAMPLE INPUTS

Deck list names (Separated by commas):
	> Tax Evasion, Tyranny, Insurrection 

Deck lists

(Tax Evasion)
	1 Lightning Bolt
	1 Glock-19 with a switch
	1 Fraudulent tax write offs

(Tyranny)
	1 Lightning Bolt
	1 Militia

(Insurrection)
	1 Lightning Bolt 
	1 January 6th



EXPECTED OUTPUT
	Based on the example inputs, the following should be spit out:

"1 Lightning Bolt" found "3" times in: Tax Evasion, Tyranny, Insurrection
	
	
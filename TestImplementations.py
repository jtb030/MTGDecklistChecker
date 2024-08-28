# Method 1: Using ANSI escape codes

# ANSI escape code constants
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

print("Method 1: Using ANSI escape codes")
print(f"{RED}This is red text{RESET}")
print(f"{GREEN}{BOLD}This is bold green text{RESET}")
print(f"{BLUE}{ITALIC}This is italic blue text{RESET}")
print(f"{RED}{UNDERLINE}This is underlined red text{RESET}")
print(f"{GREEN}Green{RESET} and {BLUE}blue{RESET} in the same line")

print("\n" + "=" * 40 + "\n")

# Method 2: Using colorama library

# First, install colorama: pip install colorama
from colorama import Fore, Back, Style, init

# Initialize colorama
init()

print("Method 2: Using colorama library")
print(Fore.RED + "This is red text")
print(Fore.GREEN + Style.BRIGHT + "This is bright green text")
print(Fore.BLUE + Style.DIM + "This is dim blue text")
print(Back.YELLOW + Fore.BLACK + "Black text on yellow background" + Style.RESET_ALL)
print(Fore.MAGENTA + Style.NORMAL + "This is normal magenta text" + Style.RESET_ALL)

# Combining styles
print(Fore.CYAN + Back.WHITE + Style.BRIGHT + "Bright cyan text on white background" + Style.RESET_ALL)

# Using format strings with colorama
name = "Alice"
age = 30
print(f"{Fore.GREEN}{name}{Style.RESET_ALL} is {Fore.YELLOW}{age}{Style.RESET_ALL} years old.")

print("\n" + "=" * 40 + "\n")

# Method 3: Saving results to a file

import os
from datetime import datetime

def save_results_to_file(masterDuplicates, decklist_names):
    # Get the user's home directory
    home_dir = os.path.expanduser("~")
    
    # Create a default directory for saving results
    default_dir = os.path.join(home_dir, "MTGChecker_Results")
    os.makedirs(default_dir, exist_ok=True)
    
    # Generate a default filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    default_filename = f"duplicate_results_{timestamp}.txt"
    default_path = os.path.join(default_dir, default_filename)
    
    # Ask user for custom file path or use default
    custom_path = input(f"Enter file path to save results (press Enter to use default: {default_path}): ").strip()
    file_path = custom_path if custom_path else default_path
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write results to file
    with open(file_path, 'w') as f:
        f.write("Master list of equivalents found:\n")
        for item, decks in masterDuplicates.items():
            ordered_decks = [deck for deck in decklist_names if deck in decks]
            count = len(ordered_decks)
            f.write(f"{item} found {count} time{'s' if count > 1 else ''} in {', '.join(ordered_decks)}\n")
    
    print(f"Results saved to {file_path}")

print("Method 3: Saving results to a file")
print("This function allows saving results to a file with custom or default path.")
print("To use it, call save_results_to_file(masterDuplicates, decklist_names)")


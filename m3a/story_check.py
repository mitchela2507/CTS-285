"""
The Lost Artifact of Blackwood Manor
A Text-Based Choose-Your-Own-Adventure Game
"""

import sys

def ask(prompt, options):
    """
    Displays a prompt and a numbered list of options.
    Validates user input until a valid selection is made.
    """
    print(f"\n{prompt}")
    for idx, option in enumerate(options, 1):
        print(f"  [{idx}] {option}")

    while True:
        raw = input("\nEnter your choice (number): ").strip()
        if raw.isdigit():
            choice = int(raw)
            if 1 <= choice <= len(options):
                return choice
        print(f"Invalid input. Please enter a number between 1 and {len(options)}.")

# Global state
inventory = []

def passage_start():
    print("\n--- THE FRONT FOYER ---")
    print("You step into Blackwood Manor. Heavy rain storms outside.")
    print("Lord Blackwood's rare Obsidian Amulet was stolen tonight.")
    print("Damp footprints lead toward the Library, while a quiet scraping sound echoes from the Basement door.")

    choice = ask("What do you do?", [
        "Follow footprints into the Library",
        "Investigate the Basement door",
        "Examine the hall coat rack"
    ])

    if choice == 1:
        passage_library()
    elif choice == 2:
        passage_basement()
    elif choice == 3:
        passage_coat_rack()

def passage_coat_rack():
    print("\n--- THE COAT RACK ---")
    print("You search a drenched trench coat hanging near the entrance.")
    print("In the pocket, you find a Small Silver Key! You take it with you.")
    if "key" not in inventory:
        inventory.append("key")

    choice = ask("Where to next?", [
        "Head to the Library",
        "Head to the Basement door"
    ])

    if choice == 1:
        passage_library()
    elif choice == 2:
        passage_basement()

def passage_library():
    print("\n--- THE LIBRARY ---")
    print("Books are scattered everywhere. A desk drawer is locked tight.")
    print("Behind a velvet curtain, you notice a subtle draft coming from a hidden passage.")

    choice = ask("What do you explore?", [
        "Try to unlock the desk drawer",
        "Step through the hidden curtain passage",
        "Return to the Foyer"
    ])

    if choice == 1:
        passage_desk_drawer()
    elif choice == 2:
        passage_secret_passage()
    elif choice == 3:
        passage_start()

def passage_desk_drawer():
    print("\n--- THE DESK DRAWER ---")
    if "key" in inventory:
        print("You use the Silver Key! Inside, you find Lord Blackwood's secret journal.")
        print("It reveals he secretly faked the theft to collect insurance money!")
        print("Footsteps approach behind you!")

        choice = ask("Quick, what is your move?", [
            "Confront Lord Blackwood who enters the room",
            "Flee into the secret curtain passage"
        ])

        if choice == 1:
            ending_twist()
        elif choice == 2:
            passage_secret_passage()
    else:
        print("The desk drawer is locked tight with a silver lock. You need a key to open it.")
        choice = ask("What do you do?", [
            "Go back and search elsewhere"
        ])
        if choice == 1:
            passage_library()

def passage_basement():
    print("\n--- THE DARK BASEMENT ---")
    print("You descend into the cold damp cellar.")
    print("A masked burglar in black is stuffing the Obsidian Amulet into a bag!")

    choice = ask("How do you react?", [
        "Sneak up and attempt to tackle the thief",
        "Block the doorway and demand they surrender",
        "Retreat to call the police"
    ])

    if choice == 1:
        passage_tackle_thief()
    elif choice == 2:
        passage_block_door()
    elif choice == 3:
        passage_start()

def passage_tackle_thief():
    print("\n--- BASEMENT SHOWDOWN ---")
    print("You leap at the thief! After a short struggle, you knock the amulet free and restrain the culprit.")
    ending_success()

def passage_block_door():
    print("\n--- DOORWAY STANDOFF ---")
    print("The thief panics, drops a blinding smoke bomb, and escapes through a cellar window!")
    print("You managed to retrieve the fallen Amulet, but the culprit got away.")
    ending_partial()

def passage_secret_passage():
    print("\n--- HIDDEN PASSAGE ---")
    print("You navigate a dark stone tunnel beneath the manor.")
    print("Up ahead, light shines from an escape hatch leading to the gardens.")

    choice = ask("Which direction?", [
        "Climb out into the Gardens",
        "Turn back to the Library"
    ])

    if choice == 1:
        passage_gardens()
    elif choice == 2:
        passage_library()

def passage_gardens():
    print("\n--- RAINY GARDENS ---")
    print("You burst into the stormy night.")
    print("You catch Lord Blackwood handing a wad of cash to an accomplice in a getaway car!")

    choice = ask("What do you do?", [
        "Snap photos with your phone as evidence"
    ])
    if choice == 1:
        ending_twist()

# ENDINGS

def ending_success():
    print("\n=== ENDING 1: MASTER DETECTIVE (SUCCESS) ===")
    print("CONGRATULATIONS! You safely retrieved the Obsidian Amulet and caught the thief.")
    print("The city press praises your sharp detective skills!")

def ending_partial():
    print("\n=== ENDING 2: A PARTIAL VICTORY ===")
    print("YOU SOLVED THE CASE... ALMOST. You saved the precious amulet, but the thief escaped.")

def ending_twist():
    print("\n=== ENDING 3: THE BLACKWOOD CONSPIRACY (TWIST) ===")
    print("UNEXPECTED TWIST! Lord Blackwood orchestrated the theft himself for insurance fraud!")
    print("Thanks to your evidence, the police arrest Lord Blackwood.")

def main():
    """Main game execution loop."""
    playing = True
    while playing:
        global inventory
        inventory = []  # Reset inventory for new run

        print("\n==============================================")
        print("  WELCOME TO THE LOST ARTIFACT OF BLACKWOOD MANOR")
        print("==============================================")

        passage_start()

        again = ask("Would you like to play again?", ["Yes", "No"])
        if again == 2:
            playing = False
            print("\nThank you for playing Detective! Goodbye.\n")

if __name__ == "__main__":
    main()
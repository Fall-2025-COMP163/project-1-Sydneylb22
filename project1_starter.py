"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Sydney Brown
Date: 10/25/2025

AI Usage: [AI created the entire code]
Example: AI helped with file I/O error handling logic in save_character function
"""

# Function to calculate stats based on class and level
def calculate_stats(character_class, level):
    if character_class == "Warrior":
        strength = 10 + level * 2
        magic = 2 + level
        health = 100 + level * 5
    elif character_class == "Mage":
        strength = 3 + level
        magic = 15 + level * 3
        health = 80 + level * 4
    elif character_class == "Rogue":
        strength = 7 + level * 2
        magic = 7 + level * 2
        health = 70 + level * 3
    elif character_class == "Cleric":
        strength = 6 + level * 2
        magic = 12 + level * 2
        health = 90 + level * 4
    else:
        strength = 0
        magic = 0
        health = 0

    return strength, magic, health

# Function to create a character
def create_character(name):
    print("=== Create Your Character ===")
    name = input("Enter character name: ")
    print("Choose a class: Warrior, Mage, Rogue, Cleric")
    character_class = input("Enter character class: ")

    # Validate class
    if character_class != "Warrior" and character_class != "Mage" and character_class != "Rogue" and character_class != "Cleric":
        print("Error: Invalid class.")
        return {"name": name}

    level = 1
    gold = 100
    strength, magic, health = calculate_stats(character_class, level)

    print("\nCharacter Created!")
    print("Name:", name)
    print("Class:", character_class)
    print("Level:", level)
    print("Strength:", strength)
    print("Magic:", magic)
    print("Health:", health)
    print("Gold:", gold)

    return name, character_class, level, strength, magic, health, gold

# Function to level up
def level_up(level, character_class):
    level += 1
    strength, magic, health = calculate_stats(character_class, level)
    gold_bonus = 50
    print("\nLevel Up!")
    print("New Level:", level)
    print("Strength:", strength)
    print("Magic:", magic)
    print("Health:", health)
    print("Gold Bonus:", gold_bonus)
    return level, strength, magic, health, gold_bonus

# Main program
def main():
    name, character_class, level, strength, magic, health, gold = create_character()

    # Ask if user wants to level up
    answer = input("\nDo you want to level up? (yes/no): ")
    if answer == "yes":
        level, strength, magic, health, bonus = level_up(level, character_class)
        gold += bonus
        print("\nUpdated Character Stats:")
        print("Name:", name)
        print("Class:", character_class)
        print("Level:", level)
        print("Strength:", strength)
        print("Magic:", magic)
        print("Health:", health)
        print("Gold:", gold)

main()

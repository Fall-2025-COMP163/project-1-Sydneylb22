"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Sydney Brown
Date: October 30, 2025

AI Usage:
AI assistance (ChatGPT) was used to help design function structure,
stat formulas, and file formatting consistency for save/load functions.
No external code was copied. AI suggestions were adapted manually.
"""

import os 


def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns: dictionary with keys:
    name, class, level, strength, magic, health, gold
    """
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]

    # Handle invalid class gracefully
    if character_class not in valid_classes:
        print("Error: Invalid class.")
        return None 

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100

    character = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

    return character


def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns: (strength, magic, health)
    """
    if character_class == "Warrior":
        strength = 10 + (level * 5)
        magic = 2 + (level * 1)
        health = 120 + (level * 10)

    elif character_class == "Mage":
        strength = 3 + (level * 1)
        magic = 12 + (level * 5)
        health = 80 + (level * 8)

    elif character_class == "Rogue":
        strength = 7 + (level * 3)
        magic = 6 + (level * 2)
        health = 90 + (level * 5)

    elif character_class == "Cleric":
        strength = 6 + (level * 2)
        magic = 10 + (level * 4)
        health = 110 + (level * 9)

    else:
        strength = magic = health = 0

    return (strength, magic, health)


def save_character(character, filename):
    """
    Saves character to text file in specific format.
    Returns True if successful, False if error.
    """
    # Since no try/except allowed, handle through logic
    if not character or "name" not in character:
        return False

    if filename == "":
        return False

    file = open(filename, "w")
    if file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
        file.close()
        return True
    else:
        return False


def load_character(filename):
    """
    Loads character from text file.
    Returns character dictionary if successful, None if not found.
    """
    if not os.path.exists(filename):
        print("File not found.")
        return None

    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    data = {}
    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            key, value = parts
            data[key] = value

    character = {
        "name": data["Character Name"],
        "class": data["Class"],
        "level": int(data["Level"]),
        "strength": int(data["Strength"]),
        "magic": int(data["Magic"]),
        "health": int(data["Health"]),
        "gold": int(data["Gold"])
    }

    return character


def display_character(character):
    """
    Prints formatted character sheet to console.
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


def level_up(character):
    """
    Increases character level and recalculates stats.
    """
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    print(f"{character['name']} leveled up to Level {character['level']}!")


if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    hero = create_character("Aria", "Mage")
    if hero:
        display_character(hero)
        save_character(hero, "aria.txt")
        loaded = load_character("aria.txt")
        print("\nLoaded Character:")
        display_character(loaded)

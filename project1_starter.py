"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Sydney Brown
Date: 10/25/2025

AI Usage: [AI created the entire code]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    if character_class not in valid_classes:
        print("Error: Invalid character class.")
        return None

    level = 1
    strength, magic, health = calculate_stats(character_class, level)
    gold = 100

    return {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": gold
    }

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
        strength = magic = health = 0

    return (strength, magic, health)

def save_character(character, filename):
    try:
        with open(filename, "w") as file:
            file.write(f"Character Name: {character['name']}\n")
            file.write(f"Class: {character['class']}\n")
            file.write(f"Level: {character['level']}\n")
            file.write(f"Strength: {character['strength']}\n")
            file.write(f"Magic: {character['magic']}\n")
            file.write(f"Health: {character['health']}\n")
            file.write(f"Gold: {character['gold']}\n")
        return True
    except PermissionError:
        print("Error: Permission denied when trying to save the file.")
        return False

def load_character(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            character = {}
            for line in lines:
                key, value = line.strip().split(": ")
                if key == "Level" or key == "Strength" or key == "Magic" or key == "Health" or key == "Gold":
                    character[key.lower()] = int(value)
                else:
                    character[key.lower().replace(" ", "_")] = value
            return {
                "name": character["character_name"],
                "class": character["class"],
                "level": character["level"],
                "strength": character["strength"],
                "magic": character["magic"],
                "health": character["health"],
                "gold": character["gold"]
            }
    except FileNotFoundError:
        print("Error: File not found.")
        return None

def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")

def level_up(character):
    character["level"] += 1
    strength, magic, health = calculate_stats(character["class"], character["level"])
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["gold"] += 50  # Bonus gold for leveling up

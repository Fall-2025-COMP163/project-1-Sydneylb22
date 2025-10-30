"""
COMP 163 - Project 1: Character Creator & Chronicles
Name: Sydney Brown
Date: 10/25/2025

AI Usage: ChatGPT helped write and refactor this code to meet COMP 163 specifications.
"""

# =======================
# Character Stat Function
# =======================
def calculate_stats(character_class, level):
    """Calculate stats based on class and level."""
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

    return strength, magic, health


# =======================
# Character Creation
# =======================
def create_character(name, character_class):
    """Create and return a new character dictionary."""
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]

    if character_class not in valid_classes:
        print("Error: Invalid class.")
        return {"name": name}

    level = 1
    gold = 100
    strength, magic, health = calculate_stats(character_class, level)

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


# =======================
# Display Character
# =======================
def display_character(character):
    """Display all character stats in the required format."""
    print(f"Character Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")


# =======================
# File Operations
# =======================
def save_character(character, filename):
    """Save the character data to a text file in the required format."""
    file = open(filename, "w")
    file.write(f"Character Name: {character['name']}\n")
    file.write(f"Class: {character['class']}\n")
    file.write(f"Level: {character['level']}\n")
    file.write(f"Strength: {character['strength']}\n")
    file.write(f"Magic: {character['magic']}\n")
    file.write(f"Health: {character['health']}\n")
    file.write(f"Gold: {character['gold']}\n")
    file.close()


def load_character(filename):
    """Load the character data from a text file."""
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    character = {}
    for line in lines:
        key, value = line.strip().split(": ")
        if key == "Character Name":
            character["name"] = value
        elif key == "Class":
            character["class"] = value
        elif key == "Level":
            character["level"] = int(value)
        elif key == "Strength":
            character["strength"] = int(value)
        elif key == "Magic":
            character["magic"] = int(value)
        elif key == "Health":
            character["health"] = int(value)
        elif key == "Gold":
            character["gold"] = int(valu

import random
import json
from smash import Character, Battle

def load_characters(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    characters = []
    for char in data:
        name = char['name']
        attacks = char['attacks']
        # Assuming each character starts with 100 health
        character = Character(name, 100, attacks)
        characters.append(character)
    return characters

def select_character(characters):
    print("Select your character:")
    for i, character in enumerate(characters):
        print(f"{i+1}. {character.name}")
    choice = input("Enter the number of your character: ")
    if choice.isdigit() and 1 <= int(choice) <= len(characters):
        return characters[int(choice) - 1]
    else:
        print("Invalid choice. A random character will be chosen for you.")
        return random.choice(characters)

def game():
    characters = load_characters('characters.json')
    user_character = select_character(characters)
    opponent_character = random.choice([char for char in characters if char != user_character])
    
    print(f"You chose {user_character.name}. Your opponent is {opponent_character.name}.")
    
    battle = Battle(user_character, opponent_character)
    winner = battle.fight()
    
    print(f"The winner is {winner}!")

if __name__ == "__main__":
    game()

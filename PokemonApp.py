import requests
import random

# To start the game with scores reset to 0 each time
global player_score, opponent_score
player_score = 0
opponent_score = 0

# Function to fetch data from API
def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
        }
    else:
        print(f"Failed to retrieve data for Pokemon with ID {pokemon_id}")
        return None


# Function to compare two Pokemon stats
def compare_pokemon(player, opponent, stat):
    global player_score, opponent_score
    player_stat = player[stat]
    opponent_stat = opponent[stat]
# player score and opponent scores are added here based on win, lose or draw
    if player_stat > opponent_stat:
        player_score += 1
        opponent_score += 0
        return "You win!"
        return f"Player Score = {player_score}"
        return f"Opponent Score = {opponent_score}"

    elif player_stat < opponent_stat:
        player_score += 0
        opponent_score += 1
        return "Opponent wins!"
        return f"Player Score = {player_score}"
        return f"Opponent Score = {opponent_score}"

    else:
        player_score += 0
        opponent_score += 0
        return "It's a tie!"
        return f"Player Score = {player_score}"
        return f"Opponent Score = {opponent_score}"

# Main game loop
def main():
    print("Welcome to Pokemon Top Trumps!")

    # Prompt the user to choose their Pokemon ID
    player_id = int(input("Enter the Pokemon ID you want to choose (1-151): "))

    # Randomly generate the opponent's Pokemon ID
    opponent_id = random.randint(1, 151)

    player_pokemon = get_pokemon_data(player_id)
    opponent_pokemon = get_pokemon_data(opponent_id)

    if player_pokemon and opponent_pokemon:
        # Users stats are visible but opponents stats are hidden, stats on new line
        print(f"Your Pokemon:\n{player_pokemon['name'].capitalize()}\n"
              f"ID: {player_pokemon['id']}\n"
              f"Height: {player_pokemon['height']}\n"
              f"Weight: {player_pokemon['weight']}")
        print(f"Opponent's Pokemon: {opponent_pokemon['name'].capitalize()} ")

        stat_choice = input("\nChoose a stat to compare (id, height, or weight): ").lower()
        # opponents stats become visible after players stat is chosen stats on new line
        if stat_choice in ["id", "height", "weight"]:
            print(f"\nOpponent's Stats:\n"
                  f"{opponent_pokemon['name'].capitalize()}\n"
                  f"ID:{opponent_pokemon['id']}\n"
                  f"Height:{opponent_pokemon['height']}\n"
                  f"Weight: {opponent_pokemon['weight']}")
            result = compare_pokemon(player_pokemon, opponent_pokemon, stat_choice)
            print(result)
            # player score and opponent scores are printed after each game
            print(f"Player Score = {player_score}")
            print(f"Opponent Score = {opponent_score}")
        else:
            print("Invalid stat choice. Choose 'id', 'height', or 'weight'.")

# Code to allow multiple plays
    play_again = input('Play again?(y/n): ')
    while play_again == 'y':
        main()
    else:
        print('Thanks for playing!')
        exit()


if __name__ == "__main__":
    main()
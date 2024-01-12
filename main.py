from mega_sena import generate_sequences_mega_sena
from lotofacil import generate_sequences_lotofacil


def checkLotteryGame(game, sequence_number):
    if game == "Mega-Sena":
        return generate_sequences_mega_sena(sequence_number)
    elif game == "Lotofácil":
        return generate_sequences_lotofacil(sequence_number)
    elif game == "Quina":
        return "You can become a mobile app developer"
    elif game == "Lotomania":
        return "You can become a mobile app developer"
    elif game == "Timemania":
        return "You can become a mobile app developer"
    elif game == "Dupla Sena":
        return "You can become a mobile app developer"

def main():
    options = ['Mega-Sena', 'Lotofácil', 'Quina', 'Lotomania', 'Timemania', 'Dupla Sena']
    print("Choose a Brazilian lottery game:")
    for i, game in enumerate(options, start=1):
        print(f"{i}. {game}")

    game_choice = input("Enter the number of your choice for the lottery game: ")

    if game_choice.isdigit() and 1 <= int(game_choice) <= len(options):
        chosen_game = options[int(game_choice)-1]
        print(f"You chose: {chosen_game}")
    else:
        print("Invalid choice. Please enter a valid number for the lottery game.")
        return

    sequence_number = input("Enter the number of sequences you want (maximum 20): ")

    if sequence_number.isdigit() and 1 <= int(sequence_number) <= 20:
        checkLotteryGame(chosen_game, int(sequence_number))
    else:
        print("Invalid choice. Please enter a valid number of sequences (1-20).")

if __name__ == "__main__":
    main()


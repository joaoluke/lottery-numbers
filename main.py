def main():
    # Define the Brazilian lottery game options
    options = ['Mega-Sena', 'Lotofácil', 'Quina', 'Lotomania', 'Timemania', 'Dupla Sena']
    print("Choose a Brazilian lottery game:")
    for i, game in enumerate(options, start=1):
        print(f"{i}. {game}")

    # Get the user's choice for the game
    game_choice = input("Enter the number of your choice for the lottery game: ")

    # Check and respond to the game choice
    if game_choice.isdigit() and 1 <= int(game_choice) <= len(options):
        chosen_game = options[int(game_choice)-1]
        print(f"You chose: {chosen_game}")
    else:
        print("Invalid choice. Please enter a valid number for the lottery game.")
        return

    # Ask for the number of sequences
    sequence_number = input("Enter the number of sequences you want (maximum 20): ")

    # Check and respond to the sequence number choice
    if sequence_number.isdigit() and 1 <= int(sequence_number) <= 20:
        print(f"You have chosen to generate {sequence_number} sequences for {chosen_game}.")
    else:
        print("Invalid choice. Please enter a valid number of sequences (1-20).")

if __name__ == "__main__":
    main()


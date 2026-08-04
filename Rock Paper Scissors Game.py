import random

CHOICES = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0

# Get number of rounds
while True:
    try:
        total_rounds = int(input("Enter the number of rounds: "))

        if total_rounds > 0:
            break

        print("Please enter a number greater than 0.")

    except ValueError:
        print("Please enter a valid number.")

# Play game
for round_number in range(1, total_rounds + 1):

    print("\n" + "=" * 40)
    print(f"Round {round_number} of {total_rounds}")
    print("=" * 40)

    # Player choice
    while True:
        player_choice = input("Choose Rock, Paper, or Scissors: ").strip().title()

        if player_choice in CHOICES:
            break

        print("Invalid choice. Please try again.")

    # Computer choice
    computer_choice = random.choice(CHOICES)

    # Determine winner
    if player_choice == computer_choice:
        pass

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        player_score += 1

    else:
        computer_score += 1

    # Round information
    print("-" * 40)
    print(f"You chose      : {player_choice}")
    print(f"Computer chose : {computer_choice}")
    print("-" * 40)

    print(f"Current Score")
    print(f"You      : {player_score}")
    print(f"Computer : {computer_score}")

# Final Result
print("\n" + "=" * 40)
print("GAME OVER")
print("=" * 40)

print(f"Final Score")
print(f"You      : {player_score}")
print(f"Computer : {computer_score}")
print("-" * 40)

if player_score > computer_score:
    print("Winner: You")

elif computer_score > player_score:
    print("Winner: Computer")

else:
    print("The game ended in a tie.")
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    print("--- Welcome to Rock, Paper, Scissors! ---")

    while True:
        # User Input
        user_choice = input("\nEnter rock, paper, or scissors (or 'q' to quit): ").lower().strip()
        
        if user_choice == 'q':
            break
        
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice! Please try again.")
            continue
            
        # Computer Selection
        computer_choice = get_computer_choice()
        
        # Display Choices
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        # Determine and Display Result
        result = determine_winner(user_choice, computer_choice)
        
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
            
        # Score Tracking
        print(f"Score -> You: {user_score} | Computer: {computer_score}")

    print("\n--- Final Score ---")
    print(f"Final Tally -> You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
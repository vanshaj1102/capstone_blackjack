import random
from art import logo

def deal_card():
    """Returns a card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculates the score for a given list of cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares user and computer scores to decide the result."""
    if user_score == computer_score:
        return "The game is a tie!"
    elif computer_score == 0:
        return "You lose! The computer has a blackjack."
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "You went over 21! You lose."
    elif computer_score > 21:
        return "The computer went over 21! You win."
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def playgame():
    print("logo")
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial two cards to both user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            next_move = input("Type 'y' to get another card, or 'n' to pass: ").lower()
            if next_move == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn
    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("do you wanna play BLACKJACK  , type 'y' or 'n' :") == "y":
    print("\n" * 50 )
    playgame()

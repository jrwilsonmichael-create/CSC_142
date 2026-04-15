# Blackjack background
import pygame
import os
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Blackjack Background")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font_large = pygame.font.Font(None, 48)
font_medium = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 24)

# Load the background image
try:
    BlackJack_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "BlackJack.png"))
    # Scale the image to fit the screen if needed
    BlackJack_image = pygame.transform.scale(BlackJack_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
except FileNotFoundError:
    print("BlackJack.png not found. Please ensure the image file is in the same directory as this script.")
    sys.exit(1)

# Button class
class Button:
    def __init__(self, x, y, width, height, text, color=GREEN):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surf = font_medium.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
VALUES = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

# Load card images
card_images = {}
card_dir = os.path.join(os.path.dirname(__file__), "BlackJackcards")
suit_index = {'Spades': 1, 'Hearts': 2, 'Clubs': 3, 'Diamonds': 4}
rank_index = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 11, 'Queen': 12, 'King': 13}
for suit in SUIT_TUPLE:
    for rank in RANK_TUPLE:
        filename = f"37631_r{suit_index[suit]}_c{rank_index[rank]}.png"
        try:
            img = pygame.image.load(os.path.join(card_dir, filename))
            img = pygame.transform.scale(img, (100, 140))  # Scale to standard card size
            card_images[f"{rank} of {suit}"] = img
        except FileNotFoundError:
            # If not found, use a placeholder or text
            pass

# Load back of card image
try:
    back_image = pygame.image.load(os.path.join(os.path.dirname(__file__), "Backofcards.png"))
    back_image = pygame.transform.scale(back_image, (100, 140))
except FileNotFoundError:
    back_image = None

# States
WELCOME = 'welcome'
RULES = 'rules'
GAME = 'game'

current_state = WELCOME

# Buttons
start_button = Button(300, 400, 200, 50, "Start")
hit_button = Button(200, 500, 100, 50, "Hit")
stand_button = Button(500, 500, 100, 50, "Stand")

# Rules text
rules_text = [
    "Welcome to Blackjack 2!",
    "",
    "Rules:",
    "- The goal is to get as close to 21 as possible without going over.",
    "- Cards are valued as follows: number cards are worth their face value,",
    "  face cards (Jack, Queen, King) are worth 10, and Aces are worth 11 or 1.",
    "- Players are dealt two cards initially.",
    "- Players can choose to 'Hit' (take another card) or 'Stand' (keep their current hand).",
    "- If a player's hand exceeds 21, they bust and lose the game.",
    "- The dealer must hit until their hand is at least 17.",
    "- If the dealer busts, all remaining players win.",
    "- If neither the player nor the dealer busts, the one with the higher hand value wins.",
    "",
    "Click Start to begin the game!"
]

# Game variables
deck = []
player_hand = []
dealer_hand = []
game_over = False
message = ""

def create_deck():
    deck = []
    for suit in SUIT_TUPLE:
        for rank in RANK_TUPLE:
            deck.append({'rank': rank, 'suit': suit})
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        value += VALUES[card['rank']]
        if card['rank'] == 'Ace':
            aces += 1
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def draw_card(card, x, y):
    card_name = f"{card['rank']} of {card['suit']}"
    if card_name in card_images:
        screen.blit(card_images[card_name], (x, y))
    else:
        # Draw text if no image
        text = font_small.render(card_name, True, WHITE)
        screen.blit(text, (x, y))

def start_game():
    global deck, player_hand, dealer_hand, game_over, message
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    game_over = False
    message = ""

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_state == WELCOME:
                if start_button.is_clicked(event.pos):
                    current_state = RULES
            elif current_state == RULES:
                if start_button.is_clicked(event.pos):
                    current_state = GAME
                    start_game()
            elif current_state == GAME and not game_over:
                if hit_button.is_clicked(event.pos):
                    player_hand.append(deal_card(deck))
                    if calculate_hand_value(player_hand) > 21:
                        message = "Bust! You lose."
                        game_over = True
                elif stand_button.is_clicked(event.pos):
                    # Dealer's turn
                    while calculate_hand_value(dealer_hand) < 17:
                        dealer_hand.append(deal_card(deck))
                    player_value = calculate_hand_value(player_hand)
                    dealer_value = calculate_hand_value(dealer_hand)
                    if dealer_value > 21:
                        message = "Dealer busts! You win!"
                    elif player_value > dealer_value:
                        message = "You win!"
                    elif player_value < dealer_value:
                        message = "Dealer wins!"
                    else:
                        message = "It's a tie!"
                    game_over = True

    # Draw the background
    screen.blit(BlackJack_image, (0, 0))

    if current_state == WELCOME:
        # Draw welcome text
        welcome_text = font_large.render("Welcome to BlackJack 2", True, WHITE)
        screen.blit(welcome_text, (SCREEN_WIDTH // 2 - welcome_text.get_width() // 2, 200))
        start_button.draw(screen)
    elif current_state == RULES:
        # Draw rules
        y_offset = 50
        for line in rules_text:
            text_surf = font_small.render(line, True, WHITE)
            screen.blit(text_surf, (50, y_offset))
            y_offset += 30
        start_button.draw(screen)
    elif current_state == GAME:
        # Draw game
        # Player's hand
        player_text = font_medium.render("Your hand:", True, WHITE)
        screen.blit(player_text, (50, 50))
        x = 50
        for card in player_hand:
            draw_card(card, x, 100)
            x += 120
        player_value = calculate_hand_value(player_hand)
        value_text = font_small.render(f"Value: {player_value}", True, WHITE)
        screen.blit(value_text, (50, 200))

        # Dealer's hand
        dealer_text = font_medium.render("Dealer's hand:", True, WHITE)
        screen.blit(dealer_text, (50, 250))
        x = 50
        for i, card in enumerate(dealer_hand):
            if not game_over and i == 0:
                # Show back image for hidden card
                if back_image:
                    screen.blit(back_image, (x, 300))
                else:
                    pygame.draw.rect(screen, BLACK, (x, 300, 100, 140))
            else:
                draw_card(card, x, 300)
            x += 120
        if game_over:
            dealer_value = calculate_hand_value(dealer_hand)
            value_text = font_small.render(f"Value: {dealer_value}", True, WHITE)
            screen.blit(value_text, (50, 450))

        # Buttons
        if not game_over:
            hit_button.draw(screen)
            stand_button.draw(screen)

        # Message
        if message:
            msg_text = font_medium.render(message, True, WHITE)
            screen.blit(msg_text, (SCREEN_WIDTH // 2 - msg_text.get_width() // 2, 550))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
sys.exit()


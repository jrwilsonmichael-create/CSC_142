# This will show the start button and rules for the blackjack game and the start button after the rules are shown it will start the game
import time
def show_start_button():
	# I will add the rules of blackjack 
	print("Welcome to Blackjack Fools!")
print("Rules:") 
print("- The goal is to get as close to 21 as possible without going over.")
print("- Cards are valued as follows: number cards are worth their face value, face cards (Jack, Queen, King) are worth 10, and Aces are worth 11 or 1.")
print("- Players are dealt two cards initially.")
print("- Players can choose to 'Hit' (take another card) or 'Stand' (keep their current hand).")
print("- If a player's hand exceeds 21, they bust and lose the game.")
print("- The dealer must hit until their hand is at least 17.")
print("- If the dealer busts, all remaining players win.")
print("- If neither the player nor the dealer busts, the one with the higher hand value wins.")
print("click the start button to start the game")
show_start_button()
time.sleep(5) # Wait for 5 seconds before starting the game

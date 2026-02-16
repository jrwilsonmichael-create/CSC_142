# I will be making a black Jack game class
import random 

# Card constants
SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 
'Queen', 'King')
NCARDS = 8
# Pass in a deck and this function returns a random card from the deck
def getCard(deckListIn):
    thisCard = deckListIn.pop() # pop one off the top of the deck and return
    return thisCard
# Pass in a deck and this function returns a shuffled copy of the deck    
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut
#  Main code
print('Welcome to BlackJack Fools.')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start.')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:  # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']    
    print('Starting card is:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):  # play one game of this many cards
        answer = input('Will the next card be higher or lower than the ' +
                        currentCardRank + ' of ' + 
                        currentCardSuit + '? (Enter H or L): ')
        answer = answer.casefold() # Make answer lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardValue = nextCardDict['value']
        print('Next card is:', nextCardRank + ' of ' + currentCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('Bout time you got it right. It was higher.')
                score = score + 20
            else:
                print('At this point, your just dumb. It was lower.')
                score = score - 15
        elif answer == 'l':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('Starting to think with that head of yours. It was lower.')
            else:
                score = score - 15
                print('Your brain must be room temperature. It was higher.')

        print('Your score is now:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

    goAgain = input('wanna go again? or rage quit? press Enter, ot Q to quit:')
    if goAgain == 'q':
        break
    print('Thanks for playing! I bet you rage quited mid game anyway.')
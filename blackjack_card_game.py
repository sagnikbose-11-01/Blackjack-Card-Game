


import random

suits = ('hearts', 'spades', 'clubs', 'diamonds')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'king', 'queen', 'jack', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'king': 10, 'queen': 10, 'jack': 10, 'ace': 11}


playing = True

class Card(): # parenthesis are mandatory only during inheritance but u can also you use it if u want to even if there is no inheritance

    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
        # self.value=values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


# new_card=Card('hearts', 'nine')
# print(new_card) 

class Deck():
    
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                card_created=Card(suit, rank)
                self.deck.append(card_created)

    def __str__(self):
        deck_comp=''

        for x in self.deck:
            deck_comp +='\n'+ x.__str__()
        return 'The deck contains: '+ deck_comp    

    def shuffle(self):
        random.shuffle(self.deck) 

    def deal(self):
        single_card=self.deck.pop()
        return single_card



# my_deck=Deck()

# print(my_deck)

# for x in my_deck.deck:
#     print(x) 


# print("\n \n \n")
# print(my_deck.deal())     

# my_deck.shuffle()
# print(my_deck)

# print(my_deck.deal())



class Hand():

    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0

    def add_card(self, card):

        # card from Deck.deal() ----> single card [Card(suit, rank)]
        self.cards.append(card) 
        self.value +=values[card.rank] 

        # track aces
        if card.rank == 'ace':
            self.aces += 1  

    def adjust_for_ace(self):

        # if the total value is greater than 21 and if I still have an ace than change my ace to be a one rather than 11
        while self.value > 21 and self.aces > 0:
            self.value -=10
            self.aces -=1



# test_deck = Deck()

# test_deck.shuffle()

# # player

# test_player = Hand()

# deal 1 card from the deck

# pulled_card = test_deck.deal()

# print(pulled_card)

# test_player.add_card(pulled_card)
# print(test_player.value)



class Chips():

    def __init__(self, total=100):
        self.total = total # this can be set to a default value or supplied by an user input
        self.bet = 0

    def win_bet(self):
        self.total +=self.bet

    def lose_bet(self):
        self.total -=self.bet      



def take_bet(chips):

    while True:

        try:
            chips.bet = int (input("How many chips would you like to bet? "))

        except:
            print('please provide an integer')    

        else:
            if chips.bet > chips.total:
                print('Sorry you do not have enough chips! You have: {}'.format(chips.total)) 
            else:
                break    



def hit (hand, deck):

    single_card = deck.deal()
    hand.add_card(single_card)            
    hand.adjust_for_ace()


def hit_or_stand(hand, deck):

    global playing

    while True:

        x = input("enter hit or stand? h or s") 

        if x[0].lower() == 'h':
            hit(hand, deck) 

        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn")
            playing = False
        
        else:
            print('sorry i did not understand that, please enter h or s only!')
            continue
        
        break



def show_some(player, dealer):
     
       # will show the dealer's one card
       

       print("\nDealer's hand:")
       print('First hand is hidden!')
       print(dealer.cards[1])

       # will show all the cards of the player

       print("\nPlayer's hand:")
       for card in player.cards:
           print(card)


def show_all(player, dealer):

        # will show all the cards of the dealer
        print("\nDealer's hand:")
        for card in dealer.cards:
           print(card)

        print(f"the Dealer's hand value: {dealer.value}")   

        # will show all the cards of the player
        print("\nPlayer's hand:")
        for card in player.cards:
           print(card)
        
        print(f"the Player's hand value: {player.value}")   



def player_busts(player, dealer, chips):
    print('BUST PLAYER')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('PLAYER WINS')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('DEALER BUSTED, PLAYER WINS!')
    chips.lose_bet()
    

def dealer_wins(player, dealer, chips):
    print('DEALER WINS, PLAYER BUSTED!')
    chips.win_bet()

def push(player, dealer):
    print('Dealer and Player tie! PUSH')











while True:
    # Print an opening statement
    print('WELCOME TO BLACKJACK')
    
    # Create & shuffle the deck, deal two cards to each player

    deck=Deck()
    deck.shuffle()

    player_hand= Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand= Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    
        
    # Set up the Player's chips
    
    player_chips= Chips()

    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(player_hand, deck)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

            

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(dealer_hand, deck)


    
        # Show all cards
        
        show_all(player_hand, dealer_hand)


        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)  

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            push(player_hand, dealer_hand)    
        
          
    
    # Inform Player of their chips total 

    print(f"Player total chips are at: {player_chips.total}")
    
    # Ask to play again

    new_game = input('Enter whether you want to continue the game or not? y/n')

    if new_game[0].lower() == 'y':
        
        playing = True

    else:
        print('Thank You for playing!')  
        break  

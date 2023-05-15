import random

def main():
  
    
    
    while play_blackjack():
        play_blackjack()
    
    print("goodbye")

def play_blackjack():
    fine = True
    player_hand, dealer_hand = deal_card([], [])
    print("You have been dealt", player_hand[0])
    print("The dealer's face-up card is", dealer_hand[0])
    
    while True:
        
        string = "Your cards are:" + str(player_hand)+ "Would you like to hit or stand? "
        decision = input(string)
       
        if decision.lower() == "hit":
            player_hand, dealer_hand = deal_card(player_hand, dealer_hand)
            print("You have been dealt a", player_hand[-1])
            print("The dealer's face-up card is", dealer_hand[0])
            if check_loss(player_hand):
                print("Your hand is greater than 21. You lose!")
            else:
                continue
                
        else:
            if sum(dealer_hand) > 21 or sum(player_hand) == 21:
                print("You win")
            else:    
                get_winner(player_hand, dealer_hand)
    
        comment = input("Would you like to play again? y/n")
        if comment == "y":
            return True
        else:
            return False
        

def deal_card(player, dealer):
    new_card_1 = random.randint(1, 11)
    new_card_2 = random.randint(1, 11)
    new_hand =[player + [new_card_1], dealer + [new_card_2]]
    
    return new_hand



def check_loss(hand):
    if sum(hand) > 21:
        return False
    else: 
        return True

def get_winner(player, dealer):
    if sum(player) > sum(dealer):
        print("You win!")
    elif sum(player) < sum(dealer):
        print("Dealer wins!")
    elif sum(player) == sum(dealer):
        print("It's a tie!")

if __name__ == '__main__':
    main()
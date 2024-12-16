# Students, fill out statement of work header
# Student Name in Canvas: Katie Wu
# Penn ID: 62427079
# Did you do this homework on your own (yes / no): Yes
# Resources used outside course materials: N/A

# import statements
from random import shuffle, choice, random




def get_user_input(question):
# Prompts the user with the given question and processes the input
# Parameters: question(str)
# Returns: the post-processed user input:
  # If input is empty, reprompt the question until input is valid.
  # If input is a number, cast it to an integer.
  # If input is a power card (SOH, DOT, DMT), return it as an uppercase string.
  # If input is any other string, return it as a lowercase string.


  # Asks user for input and ensures it's valid
  while True:

    # Prompts user to enter a value, then removes whitespace from the input string
    user_input = input(question).strip()


    # Invalidates an empty input and prompts the question again
    if len(user_input) == 0:
      print("Input cannot be empty. Please try again.")
      continue


    # Casts numerical inputs to an integer and exits the loop with valid input
    if user_input.isdigit():
      return int(user_input)


    # Returns power card input as an uppercase string and exits the loop with valid input
    if user_input.upper() in ['SOH', 'DOT', 'DMT']:
      return user_input.upper()


    # Returns all other string inputs as a lowercase string and exits the loop with valid input
    return user_input.lower()

      


def setup_water_cards():
# Creates and shuffles a list of water cards with (30x) 1 unit cards, (15x) 5 unit cards, (8x) 10 unit cards.
# Returns: A shuffled list of water card values.

  # Creates the list of water cards with specified values and quantities
  water_cards = [1] * 30 + [5] * 15 + [10] * 8


  # Shuffles the list of water cards
  shuffle(water_cards)


  # Returns the shuffled list
  return water_cards




def setup_power_cards():
# Creates and shuffles a list of power cards with (10x) SOH cards, (2x) DOT cards, (3x) DMT cards.
# Returns: A shuffled list of power cards.

  # Creates the list of power cards with specified values and quantities
  power_cards = ['SOH'] * 10 + ['DOT'] * 2 + ['DMT'] * 3


  # Shuffles the list of power cards
  shuffle(power_cards)


  # Returns the shuffled list
  return power_cards




def setup_cards():
# Sets up both the water card and power card piles.
# Returns: A 2-tuple containing the water cards pile and power cards pile, respectively.

  # Calls setup_water_cards() to get the shuffled water cards
  water_cards = setup_water_cards()


  # Calls setup_power_cards() to get the shuffled power cards
  power_cards = setup_power_cards()


  # Returns 2-tuple containing water cards and power cards piles
  return (water_cards, power_cards)




def get_card_from_pile(pile, index):
# Removes the entry at the specified index of the given pile (water or power) and modifies the pile by reference
# Parameters: pile(lst), index(int)
# Returns: Card removed from pile

  return pile.pop(index)




def arrange_cards(cards_list):
# Arranges player's cards such that: first (3) indices are water cards in ascending order and last (2) indices are power cards in alphabetical order.
# Parameters: cards_list(lst)
# Function does not return anything

  # Separate the water and power cards
  water_cards = [card for card in cards_list if isinstance(card, int)]
  power_cards = [card for card in cards_list if isinstance(card, str)]


  # Sorts the water cards in ascending order
  water_cards.sort()

  # Sorts the power cards in alphabetical order
  power_cards.sort()


  # Rearranges cards_list so that first (3) indices are water cards
  cards_list[:3] = water_cards[:3]

  # Rearranges cards_list so that last (2) indices are power cards
  cards_list[3:5] = power_cards[:2]




def deal_cards(water_cards_pile, power_cards_pile):
# Deals cards to player 1 and player 2, such that each player gets 3 water cards and 2 power cards.
# Cards are then arranged in each player's hand by using the arrange_cards function.
# Parameters: water_cards_pile(lst[int]), power_cards_pile(lst[str])
# Returns: A 2-tuple containing the hands of player 1 and player 2

  # Initialize player hands
  player_1_cards = []
  player_2_cards = []


  # Deals 3 water cards alternately to both players
  for i in range(3):
    player_1_cards.append(water_cards_pile.pop(0))
    player_2_cards.append(water_cards_pile.pop(0))


  # Deals 2 power cards alternately to both players
  for i in range(2):
    player_1_cards.append(power_cards_pile.pop(0))
    player_2_cards.append(power_cards_pile.pop(0))


  # Arranges the cards for both players
  arrange_cards(player_1_cards)
  arrange_cards(player_2_cards)


  # Returns both players' hands as a 2-tuple
  return (player_1_cards, player_2_cards)




def apply_overflow(tank_level):
# Applies the overflow rule to the given tank level if tank level exceeds max fill value (80 units).
# Overflow is calculated and the remaining water is adjusted accordingly.
# Parameters: tank_level(int)
# Returns: The adjusted tank level after applying the overflow rule, if necessary.

  # Defines the max fill value(constant)
  MAX_FILL_VALUE = 80


  # Checks if the tank level exceeds the max fill value and if overflow needs to be applied
  if tank_level > MAX_FILL_VALUE:

    # Calculates the overflow
    overflow = tank_level - MAX_FILL_VALUE

    # Applies the overflow rule
    return MAX_FILL_VALUE - overflow


  # Returns the adjusted tank level (or the original tank level if no overflow occurred)
  return tank_level




def use_card(player_tank, card_to_use, player_cards, opponent_tank):
# Uses a card from the player's hand, updates the player's and opponent's tank levels, and applies overflow if necessary.
# Parameters: player_tank(int), card_to_use(int or str), player_cards(lst), opponent_tank(int)
# Returns: A 2-tuple containing the updated player's tank and opponent's tank levels, respectively.

  # Removes the used card from the player's hand
  player_cards.remove(card_to_use)


  # If the card used is a water card(int), add its value to the player's tank
  if isinstance(card_to_use, int):
    player_tank += card_to_use


  # If the card used is a power card(str), apply the corresponding effect
  elif isinstance(card_to_use, str):


    # Steal Opponent's Half(SOH): steals half of the opponent's tank
    if card_to_use == 'SOH':
      stolen_water = opponent_tank // 2
      player_tank += stolen_water
      opponent_tank -= stolen_water

    # Drain Opponent's Tank(DOT): completely drains the opponent's tank
    if card_to_use == 'DOT':
      opponent_tank = 0

    # Double My Tank(DMT): doubles the level of the player's tank
    if card_to_use == 'DMT':
      player_tank *= 2


  # Apply overflow to the player's tank if necessary
  player_tank = apply_overflow(player_tank)


  # Returns the updated tank levels for the player and opponent as a 2-tuple
  return (player_tank, opponent_tank)  
  



def discard_card(card_to_discard, player_cards, water_cards_pile, power_cards_pile):
# Discards the given card from the player's hand and adds it to the bottom of the appropriate pile.
# Parameters: card_to_discard(int or str), player_cards(lst), water_cards_pile(lst[int]), power_cards_pile(lst[str])
# Function does not return anything

  # Removes the discarded card from the player's hand
  player_cards.remove(card_to_discard)


  # Checks if the discarded card is a water card(int) and adds it to the bottom of the water cards pile
  if isinstance(card_to_discard, int):
    water_cards_pile.append(card_to_discard)


  # Checks if the discarded card is a power card(str) and adds it to the bottom of the power cards pile
  if isinstance(card_to_discard, str):
    power_cards_pile.append(card_to_discard)




def filled_tank(tank):
# Determines if the tank level is between the min and max fill values (inclusive).
# Parameters: tank(int)
# Returns: Boolean representing whether the tank is filled

  # Defines the max and min fill values
  MIN_FILL_VALUE = 75
  MAX_FILL_VALUE = 80


  # Checks if the tank level is between the min and max fill values
  return (MIN_FILL_VALUE <= tank <= MAX_FILL_VALUE)




def check_pile(pile, pile_type):
# Checks if the given pile is empty and calls the appropriate setup function to replenish it.
# Parameters: pile(lst), pile_type(str)
# Function does not return anything

  # Checks if the pile is empty
  if len(pile) == 0:

    # Replenishes the water card pile
    if pile_type == 'water':
      pile.extend(setup_water_cards())

    # Replenishes the power card pile
    if pile_type == 'power':
      pile.extend(setup_power_cards())




def human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, opponent_tank):
# Executes the human player's turn. The human can choose to use or discard a card from their hand.
# Parameters: human_tank(int), human_cards(lst), water_cards_pile(lst[int]), power_cards_pile(lst[str]), opponent_tank(int)
# Returns: A 2-tuple containing the updated human tank level and opponent tank level

  # Displays the current tank levels of both players
  print("\n=== Human Player's turn ===")
  print(f"Your water level is at: {human_tank}")
  print(f"Computer's water level is at: {opponent_tank}")



  # Displays the human player's hand
  print(f"Your cards are: {human_cards}")



  # Asks the human player whether they want to use or discard a card
  action = get_user_input("Do you want to use or discard a card? (u / d): ").lower()

  # Reprompts the user if input is invalid
  while action not in ['u', 'd']:
      action = get_user_input("Invalid input. Please enter 'u' to use or 'd' to discard: ").lower()



  # Asks the human player to choose a card to use or discard
  card_to_play = get_user_input(f"Which card do you want to use?: {human_cards} ")

  # Reprompts the user if input is not in the human's hand
  while card_to_play not in human_cards:
      card_to_play = get_user_input(f"Invalid card. Please choose a valid card from your hand: {human_cards}: ")


  print(f"Playing with card: {card_to_play}")



  # Plays the card if the human player chose to use
  if action == 'u':
      human_tank, opponent_tank = use_card(human_tank, card_to_play, human_cards, opponent_tank)
      
  # Discards the card if the human player chose to discard
  else:
      print(f"You discarded the card: {card_to_play}")
      discard_card(card_to_play, human_cards, water_cards_pile, power_cards_pile)



  # Draws a new card of the same type they just used or discarded
  # Draws a new card from the water card pile
  if isinstance(card_to_play, int):

      # Checks if the pile is empty
      check_pile(water_cards_pile, 'water')

      new_card = get_card_from_pile(water_cards_pile, 0)
      print(f"Drawing water card: {new_card}")

  # Draws a new card from the power card pile
  else:

      # Checks if the pile is empty
      check_pile(power_cards_pile, 'power')

      new_card = get_card_from_pile(power_cards_pile, 0)
      print(f"Drawing power card: {new_card}") 



  # Adds the new card to the human's hand and arranges the hand
  human_cards.append(new_card)
  arrange_cards(human_cards)



  # Applies overflow to the human tank, if necessary
  human_tank = apply_overflow(human_tank)



  # Prints the updated tank levels for both players
  print(f"Your water level is now at: {human_tank}")
  print(f"Computer's water level is now at: {opponent_tank}")

  # Prints the updated hand
  print(f"Your cards are now: {human_cards}")



  # Returns the updated human and computer tank levels
  return (human_tank, opponent_tank)




def computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, opponent_tank):
# Executes the computer player's turn. The computer either uses or discards a card.
# Parameters: computer_tank(int), computer_cards(lst), water_cards_pile(lst[int]), power_cards_pile(lst[str]), opponent_tank(int)
# Returns: A 2-tuple containing the updated computer's tank level and human's tank level

  # Displays the current tank levels of both players
  print("\n=== Computer Player's turn ===")
  print(f"Computer's water level is at: {computer_tank}")
  print(f"Your water level is at: {opponent_tank}")

  

  # Defines the max and min fill values
  MIN_VALUE = 75
  MAX_VALUE = 80



  # First checks if there's a winning card in computer's hand
  winning_card, best_card = None, None
  for card in computer_cards:

    # Looks through the computer's water cards
    if isinstance(card, int):
      potential_tank = apply_overflow(computer_tank + card)

      # Looks at the ideal range for card to become a winning card
      if MIN_VALUE <= potential_tank <= MAX_VALUE:
        winning_card = card
        break

      # Looks for the next best card that doesn't cause overflow
      # Calculates which card is best_card given the situation 
      elif potential_tank <= MAX_VALUE:
        best_card = card


  # Plays the winning card if found
  if winning_card:
    print(f"Computer playing with winning card: {winning_card}")
    computer_tank = apply_overflow(computer_tank + winning_card)

    # Removes the used card and replenishes the hand
    computer_cards.remove(winning_card)

    replenish_computer_cards(computer_cards, water_cards_pile, power_cards_pile)
    
    arrange_cards(computer_cards)
    return (computer_tank, opponent_tank)
    



  # If no winning card is found, checks for beneficial power cards
  else:

    for card in computer_cards:

      # Steals half opponent's water if they have enough worth stealing
      if card == 'SOH' and opponent_tank >= 30:
        print(f"Computer playing with power card: {card}")
        computer_tank, opponent_tank = use_card(computer_tank, card, computer_cards, opponent_tank)
        computer_tank = apply_overflow(computer_tank)
        break

      # Drains opponent's tank if opponent is close to winning
      elif card == 'DOT' and opponent_tank >= 40:
        print(f"Computer playing with power card: {card}")
        computer_tank, opponent_tank = use_card(computer_tank, card, computer_cards, opponent_tank)
        computer_tank = apply_overflow(computer_tank)
        break

      # Doubles computer's tank if it brings it closer to winning
      elif card == 'DMT' and computer_tank >= 20:
        print(f"Computer playing with power card: {card}")
        computer_tank, opponent_tank = use_card(computer_tank, card, computer_cards, opponent_tank)

        # Handles any overflow if necessary
        computer_tank = apply_overflow(computer_tank)
        break



    # If no beneficial power card is found, use the best water card or discard the smallest water card
    else:

      # If a best card is determined, uses the selected water card
      if best_card and random() < 0.5:
        print(f"Computer playing with best card: {best_card}")
        computer_tank += best_card

        # Removes the used card
        computer_cards.remove(best_card)

      # If no best card is determined, play biggest card
      else:
        biggest_card = max([card for card in computer_cards if isinstance(card, int)], default=None)
        computer_tank += biggest_card
        computer_cards.remove(biggest_card)


      
  # Draws a new card of the same type computer just used or discarded
  # Draws a new card from the water card pile
  replenish_computer_cards(
    computer_cards, 
    water_cards_pile, 
    power_cards_pile)
  

  # Rearranges the computer's cards
  arrange_cards(computer_cards)

 
  # Prints the updated tank levels for both players
  print(f"Computer's water level is now at: {computer_tank}")
  print(f"Your water level is now at: {opponent_tank}")


  # Returns the updated computer and human tank levels
  return (computer_tank, opponent_tank)



# Everytime computer uses a card, replenish to 5 cards
#  1. Count how many water cards in computer_cards
#  2. Replenish # required of water cards
#  3. Replenish # of power cards
#  4. Return updated computer_cards pile, water_cards_pile, and power_cards_pile
def replenish_computer_cards(computer_cards, water_cards_pile, power_cards_pile):

  # Counter number of water cards in computer_cards
  water_card_count = 0
  for card in computer_cards:
    if isinstance(card, int):
      water_card_count += 1
  

  # Replenish # of required water cards (if needed)
  while water_card_count < 3:
    check_pile(water_cards_pile, 'water')
    new_card = get_card_from_pile(water_cards_pile, 0)
    computer_cards.append(new_card)
    water_card_count += 1


  # Replenish remaining card in computer's hand with 5
  i = 3
  while len(computer_cards) < 5 and i < 5:
    check_pile(power_cards_pile, 'power')
    new_card = get_card_from_pile(power_cards_pile, 0)
    computer_cards.append(new_card)
    i += 1




def main():

  # Sets up the game by setting up both card piles and dealing hands to both players
  water_cards_pile, power_cards_pile = setup_cards()
  human_cards, computer_cards = deal_cards(water_cards_pile, power_cards_pile)


  # Initialize tank levels for both players
  human_tank = 0
  computer_tank = 0


  # Prints game instructions
  print("Welcome to the WATER TANK game and play against the computer!")
  print("The first player to fill their tank wins the game.")
  print("Good luck!")


  # Randomly chooses who goes first
  current_player = choice(['Human', 'Computer'])
  print(f"The {current_player} Player has been selected to go first.")

  
    
  # Defines the round limit so game doesn't go on for infinite loops
  round_limit = 50  
  current_round = 0



  # Loops through both players' turns until the game is over or the round limit is reached
  while current_round < round_limit:

    # Increment the round counter
    current_round += 1
    


    # Human's turn
    if current_player == 'Human':
      human_tank, computer_tank = human_play(human_tank, human_cards, water_cards_pile, power_cards_pile, computer_tank)

      # Checks if the human player has won
      if filled_tank(human_tank):
        print("=== Game Over ===")
        print("Human Player won")
        break


    # Computer's turn
    else:
      computer_tank, human_tank = computer_play(computer_tank, computer_cards, water_cards_pile, power_cards_pile, human_tank)

      # Checks if the computer player has won
      if filled_tank(computer_tank):
        print("=== Game Over ===")
        print("Computer Player won")
        break



    # Alternate between both players
    current_player = "Computer" if current_player == "Human" else "Human"

  

  # If round limit is reached and no one has won, ends the game in a draw
  if current_round == round_limit:
    print("=== Game Over ===")
    print(f"No player won after {round_limit} rounds. The game ends in a draw.")



if __name__ == '__main__':
    main()

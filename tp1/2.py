# 2. Pegue um baralho de cartas: retire as 13 cartas de espadas, reserve o resto e embaralhe as cartas de espadas. Elabore um algoritmo para ordená-las por número sob as seguintes restrições:

# a. Todas as cartas devem ser seguradas em uma mão. Esta é a "primeira" mão.
# b. Inicialmente, as cartas embaralhadas estão todas empilhadas com as faces em uma direção, de modo que apenas uma carta seja visível.
# c. Inicialmente, todas as cartas são seguradas entre o polegar e o indicador da primeira mão.
# d. A carta visível na pilha pode ser retirada usando a outra mão e colocada entre quaisquer dedos da primeira mão. Ela só pode ser colocada na frente ou atrás das cartas na pilha de cartas entre esses dedos.
# e. A outra mão pode segurar apenas uma carta por vez e deve colocá-la em algum lugar na primeira mão antes de pegar outra carta visível de uma das pilhas.
# f. O algoritmo termina quando todas as cartas estão ordenadas em uma única pilha na mão.

import random

# Define the spade cards from Ace (1) to King (13)
cards = list(range(1, 14))

# Shuffle the cards to simulate the initial random stack
random.shuffle(cards)

# Simulate the initial state: All cards are in the unsorted pile (first hand), only the top card is visible
unsorted_pile = cards.copy()  # Held between thumb and forefinger of the first hand
sorted_pile = []              # The sorted pile starts empty

print("Initial shuffled pile (top to bottom):")
print(unsorted_pile)
print("\nSorting process begins...\n")

# Function to find the correct position to insert the card in the sorted pile
def find_insert_position(sorted_pile, card):
    # Since we cannot hold multiple cards in the other hand, we'll perform a linear search
    # Compare the card with each card in the sorted_pile to find its position
    for i, sorted_card in enumerate(sorted_pile):
        if card < sorted_card:
            return i
    return len(sorted_pile)  # If not less than any, it goes at the end

# Simulate the sorting process under the given constraints
while unsorted_pile:
    # Step 2a: Draw the top card from the unsorted pile using the other hand
    card_in_other_hand = unsorted_pile.pop(0)  # Remove the top card
    print(f"Picked up card: {card_in_other_hand}")

    # Step 2b: Find the correct position in the sorted pile
    position = find_insert_position(sorted_pile, card_in_other_hand)
    print(f"Card {card_in_other_hand} will be inserted at position {position} in the sorted pile.")

    # Step 2c: Insert the card into the sorted pile at the correct position
    sorted_pile.insert(position, card_in_other_hand)
    print(f"Sorted pile now: {sorted_pile}")

    # Step 2d: Adjust grip (no action needed in simulation)

    print("---")

print("\nAll cards sorted:")
print(sorted_pile)

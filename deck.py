from random import shuffle


def create_card(suit, rank, value):
	return {(suit, rank): value}


def create_deck():
	suits = ['spades', 'hearts', 'clubs', 'diamonds']
	ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
	cards = []
	for suit in suits:
		for rank in ranks:
			if rank == 'A':
				value = 11
			elif rank in ranks[0:9]:
				value = int(rank)
			else:
				value = 10
			card = create_card(suit, rank, value)
			cards.append(card)
	shuffle(cards)
	return cards


def deal_card(deck):
	return deck.pop()

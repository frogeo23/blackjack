from terminal_playing_cards import Card, View


def get_rank_suit_value(card):
	c = {k: v for k, v in card.items()}
	copied = c.popitem()
	return copied[0][1], copied[0][0], copied[1]


def display_hands(hand):
	res = []
	for _ in hand:
		rank, suit, value = get_rank_suit_value(_)
		res.append(Card(rank, suit, value))
	score = sum(res)
	print(View([res.pop() for c in range(len(res))]))
	return score

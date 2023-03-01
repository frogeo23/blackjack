@frogeo23

from deck import create_deck, deal_card
from game_logic import get_rank_suit_value, display_hands

card_deck = create_deck()

player_hand = []
dealer_hand = []

dealer_hand.append(deal_card(card_deck))
dealer_hand.append(deal_card(card_deck))
player_hand.append(deal_card(card_deck))
player_hand.append(deal_card(card_deck))

# player_score, player_display = get_score(player_hand)

# print(player_display, player_score)

value = display_hands(player_hand)
print(f"\nCard Value is {value}")
stand = 's'
hit = 'h'
a = input("hit(h) or stand(s)? ")
while hit == a.lower():
	if hit == a.lower():
		player_hand.append(deal_card(card_deck))
		value = display_hands(player_hand)
		print(f"\nCard Value is {value}")
		if value >21:
			break
	b = input("hit(h) or stand(s)? ")
	if hit == b.lower():
		player_hand.append(deal_card(card_deck))
		value = display_hands(player_hand)
		print(f"\nCard Value is {value}")
		if value >21:
			break
	if stand == b.lower():
		print('it dealer time bud')
		break
	c = input("hit(h) or stand(s)? ")
	if hit == c.lower():
		player_hand.append(deal_card(card_deck))
		value = display_hands(player_hand)
		print(f"\nCard Value is {value}")
		if value >21:
			break
	if stand == c.lower():
		print('buddy it dealer time')
		break
	d = input("hit(h) or stand(s)? ")
	if hit == d.lower():
		player_hand.append(deal_card(card_deck))
		value = display_hands(player_hand)
		print(f"\nCard Value is {value}")
		if value >21:
			break
	if stand == d.lower():
		print('da dealer turn')
		break
	e = input("hit(h) or stand(s)? ")
		
	if hit == e.lower():
		player_hand.append(deal_card(card_deck))
		value = display_hands(player_hand)
		print(f"\nCard Value is {value}")
		if value >21:
			break
	if stand == e.lower():
		print('d takes the move')
		break

v = display_hands(dealer_hand)
while v <17:
	if v < 17:
		dealer_hand.append(deal_card(card_deck))
		v = display_hands(dealer_hand)
		print(f"\nDealers Card Value is {v}")
	elif v >=17:
		break

v = display_hands(dealer_hand)
print(f"\nDealers Card Value is {v}")

if v >21:
	print('noice w')
elif v > value or value < 21:
	print('You lose bru')
elif value > v and value < 21:
	print ('Ay u win frfr')
elif v == value:
	print('U so baddddd bru')
elif v >21 and value >21:
	print('u just bad fr')
  

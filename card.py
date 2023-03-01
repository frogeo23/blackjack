# {(suit,rank): value}
class Card:
	def __int__(self, suit, rank, value):
		self.suit = suit
		self.rank = rank
		self.value = value

	@property
	def value(self):
		return self.value

	@property
	def rank(self):
		return self.rank

	@property
	def suit(self):
		return self.suit

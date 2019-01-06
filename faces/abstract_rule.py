class AbstractRule:
	'''
	`AbstractRule` is the base class for all CSS Rules.
	'''
	def __init__(self, name, value):
		self.name = name
		self.value = value
	
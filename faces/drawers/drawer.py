class Drawer:
	def prepare(self):
		'''
		`prepare` implement any logic necessary for
		preparing to draw elements on screen.

		'''
		raise NotImplementedError

	def draw_screen(self, abstract_screen):
		'''
		`draw_screen` should create a windows with widgets

		'''
		raise NotImplementedError

	def apply_style(self, abstract_style):
		'''
		`apply_style` should iterate over pre-mounted widgets and
		apply style to them.

		'''
		raise NotImplementedError

	def finish_setup(self):
		'''
		`finish_setup` is called after all elements are drawn on screen
		'''
		raise NotImplementedError
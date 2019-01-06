from collections import defaultdict

from faces import exceptions


class Widget:
	'''
	Base class for all Abstract Widgets.
	
	'''
	def __init__(self, name, id, cls, parent = None):
		self.name = name
		self.id = id
		self.cls = cls
		self.parent = parent
		self.events = defaultdict(list, {})

	def get_base_attrs(self):
		return self.name, self.id, self.cls, self.parent

	
	def bind_value(self, observable, key):
		raise NotImplementedError
	
	def add_event(self, event_name, func):
		self.events[event_name].append(func)

	def remove_event(self, event_name, func):
		try:
			self.events.get(event_name).remove(func)
		except KeyError:
			raise exceptions.EventNotFound(event_name=event_name)
		except ValueError:
			raise exceptions.FunctionNotBindedForEvent(event_name, func)

class Button(Widget):
	def __init__(self, text, id=None, cls=None):
		Widget.__init__(self, 'button', id, cls)

		self.text = text
		self.font = {
			'name': 'Calibri',
			'size': 11,
		}

	def bind_value(self, observable, key):
		self.observable.add_listener(key, self.set_text_from_observable)
	
	def set_text_from_observable(self, old_value, new_value):
		self.text = new_value



class Text(Widget):
	def __init__(self, text, id=None, cls=None):
		Widget.__init__(self, 'text', id, cls)
		
		self.text = text
		self.font = {
			'name': 'Calibri',
			'size': 11,
		}

	def bind_value(self, observable, key):
		self.observable.add_listener(key, self.set_text_from_observable)
	
	def set_text_from_observable(self, old_value, new_value):
		self.text = new_value

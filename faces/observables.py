from faces import exceptions

from collections import UserDict, defaultdict

class ObservableDict(UserDict):
	'''
	`ObservableDict` is a dict wrapper that emit
	events when dict values are changed.

	'''
	def __init__(self, initial_value = {}):
		self.data = initial_value
		
		self.setdefault(None)
		self.listeners = defaultdict(list, {})

	def add_listener(self, key, fn):
		self.listeners[key].append(fn)
	
	def remove_listener(self, key, fn):
		try:
			self.listeners[key].delete(fn)
		except KeyError:
			raise exceptions.EventNotFound(f'on_change__{key}')
		except ValueError:
			raise exceptions.FunctionNotBindedForEvent(f'on_change__{key}', fn)

	def __setitem__(self, key, new_value):
		if key:
			old_value = self.data[key]

			self.data[key] = new_value

			self.call_listeners(old_value, new_value)
	
	def call_listeners(self, old_value, new_value):
		for listener in listeners:
			listener(old_value, new_value)
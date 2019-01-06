class EntryPointNotFound(Exception):
    def __init__(self, entry_point):
        Exception.__init__(self, f'Entry point \'{entry_point}\' not found. Perharps you\'ll need to name your controller.')


class WidgetNotImplementedForTag(Exception):
    def __init__(self, element):
        Exception.__init__(self, f'Widget for element name {element.tag} not implemented yet.')
        self.element = element


class WidgetNotFound(Exception):
    def __init__(self, selector):
        Exception.__init__(self, f'Finder didn\'t found any widget for selector \'{selector}\' ')
        self.selector = selector


class EventNotFound(Exception):
    def __init__(self, event_name):
        Exception.__init__(self, f'Event \'{event_name}\' not found.')
        self.event_name = event_name

class FunctionNotBindedForEvent(Exception):
    def __init__(self, event_name, func):
        Exception.__init__(self, f'Function \'{func}\' not binded for event \'{event_name}\'.')
        self.event_name = event_name
        self.func = func
class DesignNotFound(Exception):
    def __init__(self, controller):
        Exception.__init__(
            self, f'Couldn\'t find a .design file or a design property for controller \'{controller}\'.')
        self.controller = controller


class EntryPointNotFound(Exception):
    def __init__(self, entry_point):
        Exception.__init__(
            self, f'Entry point \'{entry_point}\' not found. Perharps you\'ll need to name your controller.')
        self.entry_point = entry_point


class WidgetNotImplementedForTag(Exception):
    def __init__(self, element):
        Exception.__init__(
            self, f'Widget for element name \'{element.tag}\' not implemented yet.')
        self.element = element


class WidgetNotImplementedOnDrawer(Exception):
    def __init__(self, widget):
        Exception.__init__(
            self, f'Widget \'{widget.name}\' not implemented on Drawer.')
        self.widget = widget


class StyleNotImplemented(Exception):
    def __init__(self, widget, decl_name):
        Exception.__init__(
            self, f'Style rule \'{decl_name}\' not implemented for widget {widget}.')
        self.widget = widget


class WidgetNotFound(Exception):
    def __init__(self, selector):
        Exception.__init__(
            self, f'Finder didn\'t found any widget for selector \'{selector}\' ')
        self.selector = selector


class EventNotFound(Exception):
    def __init__(self, event_name):
        Exception.__init__(self, f'Event \'{event_name}\' not found.')
        self.event_name = event_name


class FunctionNotBindedForEvent(Exception):
    def __init__(self, event_name, fn):
        Exception.__init__(
            self, f'Function \'{fn}\' not binded for event \'{event_name}\'.')
        self.event_name = event_name
        self.fn = fn

class EventNotImplemented(Exception):
    def __init__(self, event_name, widget, fn):
        Exception.__init__(
            self, f'Event \'{event_name}\' not implemented on Drawer.')
        self.event_name = event_name
        self.widget = widget
        self.fn = fn
from collections import defaultdict

from faces import exceptions


class Widget:
    '''
    Base class for all Abstract Widgets.

    '''

    def __init__(self, tag, name, id, cls, redraw_method, parent=None):
        self.name = name
        self.id = id
        self.cls = cls
        self.tag = tag
        self.parent = parent
        self.events = defaultdict(list, {})
        self.redraw_method = redraw_method
    
    def get_base_attrs(self):
        return self.tag, self.name, self.id, self.cls, self.parent

    def request_redraw(self):
        self.redraw_method(self)

    def bind_value(self, observable, key):
        raise NotImplementedError

    def set_property(self, property_name, new_val):
        raise NotImplementedError

    def add_event(self, event_name, fn):
        '''
        Bind a function to an event on widget.

        '''
        self.events[event_name].append(fn)

    def remove_event(self, event_name, fn):
        try:
            self.events.get(event_name).remove(fn)
        except KeyError:
            raise exceptions.EventNotFound(event_name=event_name)
        except ValueError:
            raise exceptions.FunctionNotBindedForEvent(event_name, fn)


class Screen(Widget):
    def __init__(self, tag, id=None, cls=None, redraw_method=None):
        Widget.__init__(self, tag, 'screen', id, cls, redraw_method)


class Button(Widget):
    def __init__(self, tag, text, id=None, cls=None, redraw_method=None):
        Widget.__init__(self, tag, 'button', id, cls, redraw_method)

        self.text = text

    def bind_value(self, observable, key):
        self.observable.add_listener(key, self.set_text_from_observable)

    def set_text_from_observable(self, old_value, new_value):
        self.text = new_value
    
    def set_property(self, property_name, new_val):
        if property_name == 'text':
            self.text = new_val
            self.request_redraw()
        else:
            raise NotImplementedError


class Text(Widget):
    def __init__(self, tag, text, id=None, cls=None, redraw_method=None):
        Widget.__init__(self, tag, 'text', id, cls, redraw_method)

        self.text = text

    def bind_value(self, observable, key):
        self.observable.add_listener(key, self.set_text_from_observable)

    def set_text_from_observable(self, old_value, new_value):
        self.text = new_value

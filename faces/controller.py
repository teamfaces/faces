'''
controller.py

- Read XML and prepare tree of AbstracWidgets

'''
from faces import exceptions, widget_creators

from faces.abstract_rule import AbstractRule
from faces.abstract_widgets_collection import AbstractWidgetsCollection

import xml.etree.ElementTree as ET
import tinycss
from collections import defaultdict


class Controller():
    '''
    This class is responsible for parsing a .design file, prepare some dicts containing
    abstractions of the widgets and styles that are in the .design file
    so that the `App` class can mount the windows with the aid of
    a `drawer` instance.

    '''

    def __init__(self):
        self._xml_design_root = None
        self._abstract_screen = None

        self._css_style = None
        self._abstract_style = None

        self.redraw_method = None

    @property
    def widget_creators(self):
        '''
        `widget_creators` is a property that maps an element tag from .design file with a
        function that generates an abstraction of this element.

        '''
        return {
            'screen': widget_creators.create_abstract_screen,
            'button': widget_creators.create_abstract_button,
            'text': widget_creators.create_abstract_text,
        }

    def widget_not_implemented(self, tag):
        '''
        Raises a `WidgetNotImplementedForTag`
        '''

        raise exceptions.WidgetNotImplementedForTag(tag)

    def _create_tree_of_abstract_widgets(self):
        '''
        Creates a generator that returns a pair of ElementTree `element`
        with corresponding AbstractWidget reference.

        '''
        for element in self._xml_design_screen.iter():
            if element.tag not in ('style'):
                yield element, self.widget_creators.get(element.tag, self.widget_not_implemented)(element, self.redraw_method)

    @property
    def abstract_screen(self):
        '''
        Returns a AbstractScreen that maps an `xml.etree.ElementTree` with
        an `AbstractWidgetsCollection` instance.
        '''
        if not self._abstract_screen:
            self._abstract_screen = AbstractWidgetsCollection(
                self._create_tree_of_abstract_widgets())

        return self._abstract_screen

    def find_style_for(self, selector):
        '''
        Iterates over CSS rules and returns all declarations of that rule.
        Returns an empty list if selector is not found on CSS.

        '''
        rules = []

        for rule in self.css_style.rules:
            if rule.selector.as_css() == selector:
                for declaration in rule.declarations:
                    rules.append(AbstractRule(
                        declaration.name, declaration.value))

        return rules

    def _create_dict_of_styling(self):
        '''
        For every widget on AbstractScreen, creates a mapping of which styles
        need to be applied to it

        '''
        final_style = defaultdict(list, {})

        for _, widget in self.abstract_screen.items():
            _, name, id, cls, _ = widget.get_base_attrs()

            final_style[widget] += self.find_style_for(f'#{id}')
            final_style[widget] += self.find_style_for(f'.{cls}')
            final_style[widget] += self.find_style_for(name)

        return final_style

    @property
    def abstract_style(self):
        '''
        `abstract_style` returns an defaultdict object that maps
        an `AbstractWidget` with it corresponding styling rules.

        '''
        if not self._abstract_style:
            self._abstract_style = self._create_dict_of_styling()

        return self._abstract_style

    @property
    def css_style(self):
        '''
        `css_style` returns a tinycss's set of tokens based on
        style text from .design file.

        '''
        if not self._css_style:
            self._css_style = tinycss.make_parser().parse_stylesheet(self._xml_design_style.text)

        return self._css_style

    @property
    def xml_design_root(self):
        '''
        Parses the .design file or a design string and returns a xml.etree.ElementTree root element
        '''

        if not self._xml_design_root:
            # Tries to load design from `design` propery

            if getattr(self, 'design', None):
                root = ET.fromstring(self.design)
                self._xml_design_root = root
            else:

                # if `design` property isn't found, then tries to load from a .design file
                if getattr(self, 'design_path', None):
                    tree = ET.parse(self.design_path)
                    self._xml_design_root = tree.getroot()
                else:
                    raise exceptions.DesignNotFound(self.name)

        return self._xml_design_root

    @property
    def _xml_design_screen(self):
        '''
        Returns an ElementTree instance of `screen` tag.
        '''
        return self.find_tag('screen')

    @property
    def _xml_design_style(self):
        '''
        Returns an ElementTree instance of `style` tag.
        '''
        return self.find_tag('style')

    def find_tag(self, tag_name):
        '''
        Find a tag called `tag_name` on the `xml_design_root`.
        '''
        return self.xml_design_root.findall(tag_name)[0]

    def find_widget(self, selector):
        '''
        Find a widget based on CSS selector.
        '''

        for element, widget in self.abstract_screen.items():

            # Find based on id
            if selector.startswith('#'):
                id = selector[1:]
                if f'{element.attrib.get("id", "")}' == id:
                    return widget

            # Find based on class name
            if selector.startswith('.'):
                cls = selector[1:]
                if f'{element.attrib.get("class", "")}' == cls:
                    return widget

            # Find based on name
            if element.tag == selector:
                return widget

        raise exceptions.WidgetNotFound(selector)

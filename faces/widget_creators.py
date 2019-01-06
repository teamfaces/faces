'''
widget_creators.py

- Creates an `AbstractWidget` instance based on ElementTree attribs.

'''

from faces import abstract_widgets as abstracts

def create_abstract_button(tag):
    '''
    Creates an instance of `AbstractButton`
    '''
    return abstracts.Button(
        id=tag.attrib.get('id'),
        cls=tag.attrib.get('class'),
        text=tag.text.strip(),
    )

def create_abstract_text(tag):
    '''
    Creates an instance of `AbstractText`
    '''
    return abstracts.Text(
        id=tag.attrib.get('id'),
        cls=tag.attrib.get('class'),
        text=tag.text.strip(),
    )

def create_abstract_screen(tag):
    '''
    Creates an instance of `AbstractScreen`
    '''
    return abstracts.Screen()
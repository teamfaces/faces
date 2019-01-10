'''
widget_creators.py

- Creates an `AbstractWidget` instance based on ElementTree attribs.

'''

from faces import abstract_widgets as abstracts

def create_abstract_button(tag, redraw_method):
    '''
    Creates an instance of `AbstractButton`
    '''
    return abstracts.Button(
        tag=tag,
        id=tag.attrib.get('id'),
        cls=tag.attrib.get('class'),
        text=tag.text.strip(),
        redraw_method=redraw_method,
    )

def create_abstract_text(tag, redraw_method):
    '''
    Creates an instance of `AbstractText`
    '''
    return abstracts.Text(
        tag=tag,
        id=tag.attrib.get('id'),
        cls=tag.attrib.get('class'),
        text=tag.text.strip(),
        redraw_method=redraw_method,
    )

def create_abstract_screen(tag, redraw_method):
    '''
    Creates an instance of `AbstractScreen`
    '''
    return abstracts.Screen(tag=tag, redraw_method=redraw_method)
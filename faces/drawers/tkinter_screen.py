import tkinter
from faces import exceptions
from faces.utilities import parse_metrics


class TkinterScreen(tkinter.Frame):
    def __init__(self, screen, title, master=None):
        tkinter.Frame.__init__(self, master)
        self.screen = screen

        self.master = master
        self.master.title(title)

        self.abstract_mapping_with_tk_widget = {}
        self.abstract_style_with_tk_widget = {}

        self.pack(fill=tkinter.BOTH, expand=1)

    # Widget drawers

    def draw_widgets(self, widgets):
        for element, widget in widgets.items():
            tkinter_widget = self.widget_drawers.get(
                widget.name, self.raise_widget_not_implemented)(widget)

            self.abstract_mapping_with_tk_widget[widget] = tkinter_widget

            tkinter_widget.pack()

    # @todo: Refactor...
    def redraw(self, widget):
        # Recreates widget 
        old_tk_widget = self.abstract_mapping_with_tk_widget[widget]

        new_tk_widget = self.draw_button(widget)

        new_tk_widget.pack()

        # Reapplies a style

        styles_to_apply = self.abstract_style_with_tk_widget[old_tk_widget]

        for style in styles_to_apply:
            self.apply_style_for_widget(
                new_tk_widget, style.name, style.value.as_css())
        
        old_tk_widget.destroy()

        self.abstract_mapping_with_tk_widget[widget] = new_tk_widget
        self.abstract_style_with_tk_widget[new_tk_widget] = styles_to_apply

        # Reapplies events
        self.apply_events_for_widget(widget)
        

    def draw_screen(self, widget):
        return self

    def draw_button(self, widget):
        widget = tkinter.Button(self, text=widget.text)

        return widget

    def draw_text(self, widget):
        widget = tkinter.Label(self, text=widget.text)

        return widget

    @property
    def widget_drawers(self):
        return {
            'screen': self.draw_screen,
            'button': self.draw_button,
            'text': self.draw_text,
        }

    def raise_widget_not_implemented(self, widget):
        raise exceptions.WidgetNotImplementedOnDrawer(widget)

    # Styling

    def apply_style_for_screen(self, abstract_style):
        for _, widget in self.screen.items():
            tk_widget = self.abstract_mapping_with_tk_widget[widget]

            styles_to_apply = abstract_style[widget]

            self.abstract_style_with_tk_widget[tk_widget] = styles_to_apply

            for style in styles_to_apply:
                self.apply_style_for_widget(
                    tk_widget, style.name, style.value.as_css())

    def apply_style_for_widget(self, widget, decl_name, decl_value):
        self.style_appliers.get(
            decl_name, self.raise_style_not_implemented)(widget, decl_name, decl_value)

    # Style appliers

    @property
    def style_appliers(self):
        return {
            'background-color': self.apply_background_color,
            'width': self.apply_width,
            'height': self.apply_height,
            'font-family': self.apply_font_family,
            'font-size': self.apply_font_size,
            'font': self.apply_font,
            'color': self.apply_color,
            'size': self.apply_size,
        }

    def apply_background_color(self, widget, rule, value):
        widget.config(bg=value)

    def apply_size(self, widget, rule, value):

        width, height = parse_metrics(value)

        if widget == self:
            self.master.geometry(f'{width}x{height}')
        else:
            self.apply_width(widget, rule, width)
            self.apply_height(widget, rule, height)

    def apply_width(self, widget, rule, value):
        widget.config(width=value)

    def apply_height(self, widget, rule, value):
        widget.config(height=value)

    def apply_font_family(self, widget, rule, value):
        widget.config(font=value)

    def apply_font_size(self, widget, rule, value):
        value = parse_metrics(value)
        widget.config(font=(None, value))

    def apply_font(self, widget, rule, value):
        value = parse_metrics(value)

        if len(value) == 2:
            font_size, font_family = value
            widget.config(font=(font_family, font_size))

        if len(value) == 3:
            font_weight, font_size, font_family = value
            widget.config(font=(font_family, font_size, font_weight))

    def apply_color(self, widget, rule, value):
        widget.config(fg=value)

    def raise_style_not_implemented(self, widget, decl_name, decl_value):
        raise exceptions.StyleNotImplemented(widget, decl_name)

    def apply_events_for_widget(self, widget):
        tk_widget = self.abstract_mapping_with_tk_widget[widget]

        for event_name, fns in widget.events.items():
            for fn in fns:
                self.event_appliers.get(event_name, self.raise_event_not_implemented)(
                    event_name, tk_widget, fn)

    def apply_events(self, screen):
        for _, widget in screen.items():
            self.apply_events_for_widget(widget)


    # Event appliers

    @property
    def event_appliers(self):
        return {
            'click': self.apply_evt_click,
        }
    

    def apply_evt_click(self, event_name, tk_widget, fn):
        def evt_click(event):
            fn()
        
        tk_widget.bind('<Button-1>', evt_click)


    def raise_event_not_implemented():
        raise exceptions.EventNotImplemented(event_name, tk_widget, fn)

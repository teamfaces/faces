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
                widget.name, self.raise_not_implemented)(widget)

            self.abstract_mapping_with_tk_widget[widget] = tkinter_widget

            tkinter_widget.pack()

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

    def raise_not_implemented(self, widget):
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
            decl_name, self.raise_not_implemented)(widget, decl_name, decl_value)

    # Style appliers

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

    def raise_not_implemented(self, widget, decl_name, decl_value):
        raise exceptions.StyleNotImplemented(widget, decl_name)

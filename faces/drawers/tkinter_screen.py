import tkinter


class TkinterScreen(tkinter.Frame):
    def __init__(self, screen, title, master=None):
        tkinter.Frame.__init__(self, master)
        self.screen = screen

        self.master = master
        self.master.title = title

        self.abstract_mapping_with_tk_widget = {}

        self.pack(fill=tkinter.BOTH, expand=1)

    # Widget drawers

    def draw_widgets(self, widgets):
        for element, widget in widgets.items():
            tkinter_widget = self.widget_drawers.get(
                widget.name, self.raise_not_implemented)(widget)

            self.abstract_mapping_with_tk_widget[widget] = tkinter_widget

            tkinter_widget.pack()

    def draw_button(self, widget):
        widget = tkinter.Button(self, text=widget.text)

        return widget

    def draw_text(self, widget):
        widget = tkinter.Label(self, text=widget.text)

        return widget

    @property
    def widget_drawers(self):
        return {
            'button': self.draw_button,
            'text': self.draw_text,
        }

    # Styling

    def apply_style_for_screen(self, abstract_style):
        for _, widget in self.screen.items():
            tk_widget = self.abstract_mapping_with_tk_widget[widget]

            styles_to_apply = abstract_style[widget]

            for style in styles_to_apply:
                self.apply_style_for_widget(
                    tk_widget, style.name, style.value.as_css())

    def apply_style_for_widget(self, widget, decl_name, decl_value):
        self.style_appliers.get(
            decl_name, self.raise_not_implemented)(widget, decl_value)

    # Style appliers

    def apply_background_color(self, widget, value):
        widget.config(bg=value)

    def apply_width(self, widget, value):
        widget.config(width=value)

    def apply_height(self, widget, value):
        widget.config(height=value)

    def apply_font_family(self, widget, value):
        widget.config(font=value)

    def apply_font_size(self, widget, value):
        widget.config(font=(None, value[:-2]))

    def apply_color(self, widget, value):
        widget.config(fg=value)

    @property
    def style_appliers(self):
        return {
            'background-color': self.apply_background_color,
            'width': self.apply_width,
            'height': self.apply_height,
            'font-family': self.apply_font_family,
            'font-size': self.apply_font_size,
            'color': self.apply_color,
        }

    def raise_not_implemented(self, *args, **kwargs):
        raise NotImplementedError
import tkinter
from faces.drawers.tkinter_screen import TkinterScreen
from faces.drawers import Drawer


class TkinterDrawer(Drawer):

    def prepare(self):
        self.root = tkinter.Tk()

    def finish_setup(self):
        self.root.mainloop()

    def redraw(self, widget):
        self.tkinter_screen.redraw(widget)

    def draw_screen(self, title, screen):
        self.tkinter_screen = TkinterScreen(screen, title, self.root)

        self.tkinter_screen.draw_widgets(screen)

    def apply_events(self, screen):
        self.tkinter_screen.apply_events(screen)

    def apply_style(self, abstract_style):
        self.tkinter_screen.apply_style_for_screen(abstract_style)

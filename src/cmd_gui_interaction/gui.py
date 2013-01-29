import os
import sys
import runsuite
import logging
from user_prompt import GUIUserPromptBinary
from cStringIO import StringIO
from gi.repository import Gtk, GObject
from subprocess import Popen, PIPE

class Gui(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("delete_event", Gtk.main_quit)
        self.set_border_width(10)
        self.set_size_request(700, 600)
        notebook = Gtk.Notebook()
        notebook.set_tab_pos(Gtk.PositionType.TOP)
        notebook.append_page(MyTab(), Gtk.Label("Run Tests"))
        self.add(notebook)
        notebook.show_all()
        self.show()

class MyTab(Gtk.VBox):
    def __init__(self):
        super(MyTab, self).__init__()
        self.go_button = Gtk.Button()
        self.go_button.add(Gtk.Image().new_from_stock(Gtk.STOCK_APPLY,
                                                 Gtk.IconSize.BUTTON))
        top_box = Gtk.HBox()
        top_box.pack_start(self.go_button, False, True, 5)

        # build text console
        self.text_view = Gtk.TextView()
        self.text_view.set_editable(False)
        self.text_view.set_cursor_visible(True)

        self.buffer_ = self.text_view.get_buffer()
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_hexpand(False)
        scrolled_window.set_vexpand(True)
        scrolled_window.add(self.text_view)
        self.pack_start(top_box, False, True, 5)
        self.pack_start(Gtk.HSeparator(), False, True, 5)
        self.pack_start(scrolled_window, True, True, 5)

        # setup callbacks
        self.stream = StringIO()
        handler = logging.StreamHandler(self.stream)
        root = logging.getLogger()
        root.addHandler(handler)
        self.go_button.connect("clicked", self._go)
        GObject.timeout_add(100, self._process_log, None)
        self.i = 0
        #GObject.io_add_watch(self.stream, GObject.IO_IN, self._process_log)

    def _process_log(self, _):
        char = self.stream.getvalue()
        #self.buffer_.insert_at_cursor(char)
        self.buffer_.set_text(char)
        end = self.buffer_.get_end_iter()
        self.text_view.scroll_to_iter(end, 0, False, 0, 1)
        return True
        
    def _go(self, _):
        runsuite.run(GUIUserPromptBinary())

def main():
    """
    Main entry point.
    """
    logging.basicConfig(format='%(levelname)s: %(message)s')
    logging.root.setLevel(logging.INFO)
    Gui()
    Gtk.main()

if __name__ == "__main__":
    main()

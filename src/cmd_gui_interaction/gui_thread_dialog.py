import os
import sys
import runsuite
import logging
from interaction.harness import gui_interaction
from cStringIO import StringIO
from gi.repository import Gtk, GObject
from subprocess import Popen, PIPE
import threading

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
        self.pack_start(top_box, False, True, 5)

        # setup callbacks
        self.go_button.connect("clicked", self._go)
        
        
    def _go(self, _):
        self.thread = MyThread()
        self.thread.start()
#        runsuite.run(gui_interaction)
        GObject.timeout_add(100, self._check_job_thread, None)
        print "left _go"
        
    def _check_job_thread(self, _):
        """
        Shows terminal output from a command when 'GO' is clicked
        """
        if self.thread.is_alive():
            return True
        else:
            print "thread is dead"
            return False
    
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        #runsuite.run(gui_interaction)
        print "entering run of thread"
        for i in range(10):
            print "thread loop # " + str(i)

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

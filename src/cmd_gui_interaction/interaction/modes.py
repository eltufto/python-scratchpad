from gi.repository import Gtk
from distutils.util import strtobool
from modes_base import QuestionBase

class CmdLineBinaryQuestion(QuestionBase):
    def response(self, cmd):
        while True:
            response = raw_input("RESPONSE REQUIRED: " 
                                  + cmd +
                                 " [(Y)es/(N)o]: ")
            try:
                bool_response = strtobool(response)
                break
            except ValueError:
                print "Sorry, not a valid choice.  Try again..."
        return bool_response
    
class GUIBinaryQuestion(QuestionBase):
    def response(self, cmd):
        dialog = Gtk.MessageDialog(None, 
                                   Gtk.DialogFlags.MODAL,
                                   Gtk.MessageType.QUESTION,
                                   Gtk.ButtonsType.YES_NO,
                                   "RESPONSE REQUIRED")
        dialog.format_secondary_text(cmd)
        response = dialog.run()
        dialog.destroy()
        if response == Gtk.ResponseType.YES:
            return True
        else:
            return False
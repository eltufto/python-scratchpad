import abc
from gi.repository import Gtk
from distutils.util import strtobool

class UserPromptBase(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def response(self, cmd):
        pass

class CmdLineUserPromptBinary(UserPromptBase):    
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
    
class GUIUserPromptBinary(UserPromptBase):
   
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

from harness_base import HarnessBase
from modes import GUIBinaryQuestion, CmdLineBinaryQuestion

gui_interaction = HarnessBase()
gui_interaction.binary_question = GUIBinaryQuestion()

cmdline_interaction = HarnessBase()
cmdline_interaction.binary_question = CmdLineBinaryQuestion()

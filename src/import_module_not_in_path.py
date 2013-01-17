import os
import imp
from xdg.BaseDirectory import xdg_cache_home
CACHE_PATH = os.path.join(xdg_cache_home, 'scratchpad')
standalone_file = 'import_from_cache'


import sys
attempt_1 = os.path.dirname('/some/path/')
attempt_2 = os.path.dirname('/some/path')
attempt_3 = os.path.abspath(os.path.join('/some/path', os.path.pardir))
attempt_4 = os.path.abspath(os.path.join('/some/path/', os.path.pardir))
#sys.path.append(to_add_to_sys_path)
sys.path.append(xdg_cache_home)
scratchpad_module = __import__('scratchpad')
print scratchpad_module

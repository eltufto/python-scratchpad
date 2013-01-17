import os
import imp
from xdg.BaseDirectory import xdg_cache_home
CACHE_PATH = os.path.join(xdg_cache_home, 'scratchpad')
standalone_file = 'import_from_cache'
directory_test_file = "sub_dir.catalina_test"


import sys
attempt_1 = os.path.dirname('/some/path/')
attempt_2 = os.path.dirname('/some/path')
attempt_3 = os.path.abspath(os.path.join('/some/path', os.path.pardir))
attempt_4 = os.path.abspath(os.path.join('/some/path/', os.path.pardir))
#sys.path.append(to_add_to_sys_path)
sys.path.append(xdg_cache_home)
scratchpad_module = __import__('scratchpad')
#test_definition = __import__(standalone_file)
#test_definition.run()
#print("SJT - importing test %s" % directory_test_file)
#try:
#    test_definition = __import__(directory_test_file)
#except ImportError:
#    print("SJT - Unknown test %s" % directory_test_file)
#test_definition.run()
print scratchpad_module

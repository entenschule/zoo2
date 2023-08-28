import sys

from .function import prop_fun


action, path_string, name = sys.argv[1:4]
prop_fun(action, path_string, name)

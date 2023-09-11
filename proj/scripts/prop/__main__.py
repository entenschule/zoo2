import sys

from .function import create_or_delete_property


action, path_string, name = sys.argv[1:4]
create_or_delete_property(action, path_string, name)

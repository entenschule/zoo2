import os
import sys
from bottle import template
from datetime import datetime
from importlib import import_module


# preparations #########################################################################################################

# command line arguments
path_string, name = sys.argv[1:3]
path_list = path_string.split('.')

this_folder = os.path.dirname(__file__)
proj_folder = os.path.dirname(os.path.dirname(this_folder))
root_folder = os.path.dirname(proj_folder)
view_folder = os.path.join(this_folder, 'views')

# existing properties folder, in which the target folder will be created
properties_folder_list = [proj_folder, 'classes'] + path_list + ['properties']
properties_folder = os.path.join(*properties_folder_list)

sys.path.append(root_folder)  # add proj folder to path, so the import of names will work

# current names (to which the new name will be added)
names_file = os.path.join(properties_folder, 'names.py')
names_module = import_module(f'proj.classes.{path_string}.properties.names')
names_list = getattr(names_module, 'names')

# target folder, in which the target files will be created or deleted
target_folder = os.path.join(properties_folder, name)

# files
target_init_file = os.path.join(target_folder, '__init__.py')
target_test_file = os.path.join(target_folder, '_test.py')
update_names_file = os.path.join(properties_folder, 'names.py')
update_imports_file = os.path.join(properties_folder, '__init__.py')
log_file = os.path.join(this_folder, 'log.md')

# views
target_init_view = os.path.join(view_folder, 'target_init.tpl')
target_test_view = os.path.join(view_folder, 'target_test.tpl')
update_names_view = os.path.join(view_folder, 'update_names.tpl')
update_imports_view = os.path.join(view_folder, 'update_imports.tpl')


context = {
    'name': name,
    'class_name': path_list[-1].title(),  # class name should be folder name in title case
    'path_dots': path_string,
    'path_slashes': path_string.replace('.', '/'),
    'time': datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
    'names': names_list,
}
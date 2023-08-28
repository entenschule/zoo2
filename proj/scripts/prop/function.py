import os
import shutil
from bottle import template
from datetime import datetime
from importlib import import_module


def prop_fun(action, path_string, name):

    assert action in ['create', 'delete']
    create = action == 'create'

    path_list = path_string.split('.')

    ####################################################################################################################

    this_folder = os.path.dirname(__file__)
    proj_folder = os.path.dirname(os.path.dirname(this_folder))
    view_folder = os.path.join(this_folder, 'views')

    # existing properties folder
    properties_folder_list = [proj_folder, 'classes'] + path_list + ['properties']
    properties_folder = os.path.join(*properties_folder_list)

    # current names
    # (The import works because of the -m switch. Without it, one would have to add the root folder to `sys.path`.)
    names_module = import_module(f'proj.classes.{path_string}.properties.names')
    names_list = getattr(names_module, 'names')

    # target folder
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

    ####################################################################################################################

    context = {
        'name': name,
        'class_name': path_list[-1].title(),  # class name is folder name in title case
        'path_dots': path_string,
        'path_slashes': path_string.replace('.', '/'),
        'time': datetime.now().strftime("%Y-%m-%d, %H:%M:%S"),
        'names': names_list
    }

    ####################################################################################################################

    if create:

        assert name not in names_list
        names_list.append(name)
        os.mkdir(target_folder)

        with open(target_init_file, 'x') as f:
            f.write(template(target_init_view, context))

        with open(target_test_file, 'x') as f:
            f.write(template(target_test_view, context))

    else:

        assert name in names_list
        names_list.remove(name)
        shutil.rmtree(target_folder)

    ####################################################################################################################

    with open(update_names_file, 'w') as f:
        f.write(template(update_names_view, context))

    with open(update_imports_file, 'w') as f:
        f.write(template(update_imports_view, context))

    action = 'create' if create else 'delete'
    log_view = os.path.join(view_folder, f'log_{action}.tpl')

    with open(log_file, 'a') as f:
        f.write(template(log_view, context))

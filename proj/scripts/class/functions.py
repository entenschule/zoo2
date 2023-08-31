import os
import shutil
from bottle import template


this_folder = os.path.dirname(__file__)
proj_folder = os.path.dirname(os.path.dirname(this_folder))
target_folder = os.path.join(proj_folder, 'classes', 'animals', 'dog')
target_file = os.path.join(target_folder, '__init__.py')
view_file = os.path.join(this_folder, 'view.tpl')


def class_fun(action):
    assert action in ['create', 'delete']
    if action == 'create':
        os.mkdir(target_folder)
        with open(target_file, 'x') as f:
            f.write(template(view_file))
    else:
        shutil.rmtree(target_folder)


def attr_fun():
    with open(target_file, 'a') as f:
        f.write("    ability = 'fetch stick'\n")

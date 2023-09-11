import os
import shutil
from bottle import template


this_folder = os.path.dirname(__file__)
proj_folder = os.path.dirname(os.path.dirname(this_folder))
views_folder = os.path.join(this_folder, 'views')

class_folder = os.path.join(proj_folder, 'classes', 'animals', 'dog')
class_init_file = os.path.join(class_folder, '__init__.py')
class_init_view = os.path.join(views_folder, 'class_init.tpl')

props_folder = os.path.join(class_folder, 'properties')
props_init_file = os.path.join(props_folder, '__init__.py')
props_init_view = os.path.join(views_folder, 'props_init.tpl')
props_names_file = os.path.join(props_folder, 'names.py')
props_names_view = os.path.join(views_folder, 'props_names.tpl')

prop_folder = os.path.join(props_folder, 'clawnum')
prop_init_file = os.path.join(prop_folder, '__init__.py')
prop_init_view = os.path.join(views_folder, 'prop_init.tpl')


def create_class():

    os.mkdir(class_folder)
    with open(class_init_file, 'x') as f:
        f.write(template(class_init_view))

    os.mkdir(props_folder)
    with open(props_init_file, 'x') as f:
        f.write(template(props_init_view))
    with open(props_names_file, 'x') as f:
        f.write(template(props_names_view))

    os.mkdir(prop_folder)
    with open(prop_init_file, 'x') as f:
        f.write(template(prop_init_view))


def delete_class():
    shutil.rmtree(class_folder)


def add_attribute():
    with open(class_init_file, 'a') as f:
        f.write("    ability = 'fetch stick'\n")

from ._prepare import *
from ._update_and_log import update_and_log



# add property name to list, which will be used to update the name and import file
assert name not in names_list
names_list.append(name)


# create target folder
os.mkdir(target_folder)


# create target files
with open(target_init_file, 'x') as f:
    f.write(template(target_init_view, context))

with open(target_test_file, 'x') as f:
    f.write(template(target_test_view, context))


update_and_log('create')

import shutil
from ._prepare import *
from ._update_and_log import update_and_log


# remove property name from list, which will be used to update the name and import file
assert name in names_list
names_list.remove(name)


# remove target files and folder
shutil.rmtree(target_folder)


update_and_log('delete')

from ._prepare import *


def update_and_log(action):

    with open(update_names_file, 'w') as f:
        f.write(template(update_names_view, context))

    with open(update_imports_file, 'w') as f:
        f.write(template(update_imports_view, context))

    log_view = os.path.join(view_folder, f'log_{action}.tpl')

    with open(log_file, 'a') as f:
        f.write(template(log_view, context))

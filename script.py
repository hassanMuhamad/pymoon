from pymoon.core.entities import Directory
from pymoon.core.algorithms.observer import Observer
from pymoon.core.wenv.environment import Environment

wenv = Environment()

working_directory = wenv.CURRENT_USER_DOCUMENT_DIR
print('wenv:', working_directory)
dir = Directory(working_directory)
print(dir.list_contents())
detective = Observer(dir)

detective.hire()

detective.cleanup()


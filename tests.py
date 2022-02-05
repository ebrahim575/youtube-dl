import os
from sys import platform

if platform == 'win32':
    print('windows')
elif platform == 'darwin':
    print('mac')
else:
    print('idk')
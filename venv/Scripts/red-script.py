#!F:\Python\Django\���˼���\mysite\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'red==0.2.2','console_scripts','red'
__requires__ = 'red==0.2.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('red==0.2.2', 'console_scripts', 'red')()
    )

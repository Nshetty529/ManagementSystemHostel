import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\HP\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\HP\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("HMS.py", base=base, icon="logo3.png")]


cx_Freeze.setup(
    name = "Hostel Management Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["logo3.png",'tcl86t.dll','tk86t.dll', 'images','database']}},
    version = "1.0",
    description = "Hostel Managemnt System for Maintaining Data",
    executables = executables
    )

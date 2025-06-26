
from cx_Freeze import setup, Executable

files = ['database_manager/', 'gui/', 'scheduler_module/', 'app.py', 'qt_core.py', 'test_explorations.py']

target = Executable(
    script="app.py",
    base="Win32GUI"
)

setup(
    name="ExplorationRovers",
    version="1.0",
    description="Planning System for Exploring Rovers",
    author="Clara Miranda Garcia",
    options={'build_exe': {'include_files': files}},
    executables=[target]

)

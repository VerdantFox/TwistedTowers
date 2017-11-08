import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\Teddy\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Teddy\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("main.py", base="Win32GUI")]

# to run, go to directory in cmd prompt
# python setup.py build

cx_Freeze.setup(
    name="Twisted Towers",
    version="1.0",
    author="Theodore_Williams",
    description="Tower Defense Game built in Python's Pygame",
    options={"build_exe": {
        "excludes": ["ctypes",
                     "email",
                     "html",
                     "http",
                     "json",
                     "lib2to3",
                     "logging",
                     "multiprocessing",
                     "OpenGl",
                     "pkg_resources",
                     "pydoc_data",
                     "tcl",
                     "test",
                     "tk,",
                     "tkinter",
                     "unittest",
                     "urlib",
                     "xml",
                     "xmlrpc"
                     ],
        "packages": ["pygame",
                     "sys",
                     "effects",
                     "Enemies",
                     "Enemies.dragon",
                     "Enemies.orc",
                     "Enemies.spider",
                     "Enemies.turtle",
                     "Enemies.wolf",
                     "music",
                     "soundEffects",
                     "soundEffects.Deaths",
                     "soundEffects.TowerShots",
                     "towers"
                     ],
        "include_files":   ["acknowledgements.txt",
                            "definitions.py",
                            "enemies.py",
                            "gameBackDrop.png",
                            "gameParameters.py",
                            "gameText.py",
                            "generalClass.py",
                            "helpers.py",
                            "lists.py",
                            "main.py",
                            "setup.py",
                            "sounds.py",
                            "towerClass.py"
                            ],
        "optimize": 2}},
    executables=executables
)

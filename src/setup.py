# filepath: /c:/Users/vivek/Documents/dev/webcam/setup.py
from setuptools import setup

APP = ['src/gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['cv2', 'numpy', 'PyQt6', 'schedule', 'pystray', 'Pillow'],
    'iconfile': 'icon.icns',  # Optional: Add an icon file for the app
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
)
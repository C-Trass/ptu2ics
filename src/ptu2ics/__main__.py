from qtpy.QtWidgets import QApplication
import numpy as np
from ptufile import PtuFile
from .save_functions.save_as_tif import save2tif
from .save_functions.save_as_ics import save2ics
from .model import FileConverterModel
from .view import FileConverterView
from .controller import FileConverterController


# Example of usage:
loader_function = PtuFile
saver_functions = {".tif": save2tif, ".ics": save2ics}

app = QApplication([])
model = FileConverterModel()
view = FileConverterView()
controller = FileConverterController(view, model, loader_function, saver_functions)

from pathlib import Path
# Get the absolute path of the current script (__main__.py)
base_dir = Path(__file__).resolve().parent
# Construct the absolute path to the stylesheet
stylesheet_path = base_dir / "stylesheets" / "ElegantDark.qss"
try:
    with open(stylesheet_path, "r") as file:
        qss = file.read()
        app.setStyleSheet(qss)
except FileNotFoundError:
    print(f"Could not load stylesheet: {stylesheet_path}")
    
view.show()
app.exec()
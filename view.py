from qtpy.QtWidgets import (
    QTextEdit, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QFileDialog, QComboBox, QRadioButton, QGroupBox, QListWidget, QSpinBox
)
from qtpy.QtCore import Qt
from qtpy import QtGui
from pathlib import Path
import os


class FileConverterView(QWidget):

    def __init__(self):
        super().__init__()
        self.advanced_settings = {"time_binning": 1}
        self.init_ui()

        base_dir = Path(__file__).resolve().parent
        icon_path = base_dir / "icon" / "icon-red.ico"
        self.setWindowIcon(QtGui.QIcon(str(icon_path)))
        self.setWindowTitle('MIC file converter')
        self.resize(500, 700)

        self.delete_button.clicked.connect(self.delete_selected_files)
        self.clear_button.clicked.connect(self.clear_all_files)

    def init_ui(self):
        bold_font = QtGui.QFont()
        bold_font.setBold(True)

        layout = QVBoxLayout()

        self.load_label = QLabel("Load ptu data")
        self.load_label.setFont(bold_font)
        layout.addWidget(self.load_label)

        # Radio buttons
        self.radio_group = QGroupBox("Options")
        radio_layout = QVBoxLayout()

        self.radio1 = QRadioButton("Select ptu files")
        self.radio2 = QRadioButton("Load all ptu's in folder")
        self.radio3 = QRadioButton("Load all ptu's in folder and subfolders")
        self.radio1.setChecked(True)

        radio_layout.addWidget(self.radio1)
        radio_layout.addWidget(self.radio2)
        radio_layout.addWidget(self.radio3)
        self.radio_group.setLayout(radio_layout)
        layout.addWidget(self.radio_group)

        # File/folder buttons
        button_layout = QHBoxLayout()
        self.new_paths_btn = QPushButton("Choose new files/folder")
        self.add_paths_btn = QPushButton("Add files/folder")
        button_layout.addWidget(self.new_paths_btn)
        button_layout.addWidget(self.add_paths_btn)
        layout.addLayout(button_layout)

        # File list
        self.file_list = QListWidget()
        self.file_list.setSelectionMode(QListWidget.MultiSelection)
        layout.addWidget(self.file_list)

        # Delete/Clear buttons
        delete_clear_layout = QHBoxLayout()
        self.clear_button = QPushButton("Clear all files")
        self.delete_button = QPushButton("Delete files")
        delete_clear_layout.addWidget(self.delete_button)
        delete_clear_layout.addWidget(self.clear_button)
        layout.addLayout(delete_clear_layout)

        # Format dropdown and toggle in a row
        format_layout = QHBoxLayout()
        self.format_combo = QComboBox()
        self.format_combo.addItems([".tif", ".ics"])

        self.advanced_toggle_btn = QPushButton("Show advanced settings")
        self.advanced_toggle_btn.setCheckable(True)
        self.advanced_toggle_btn.clicked.connect(self.toggle_advanced_settings)

        format_layout.addWidget(self.format_combo)
        format_layout.addWidget(self.advanced_toggle_btn)
        layout.addLayout(format_layout)

        # Advanced settings container (initially hidden)
        self.advanced_settings_container = QWidget()
        advanced_layout = QVBoxLayout()

        self.binning_label = QLabel("Temporal binning:")
        self.binning_spinbox = QSpinBox()
        self.binning_spinbox.setMinimum(1)
        self.binning_spinbox.setValue(self.advanced_settings["time_binning"])
        self.binning_spinbox.valueChanged.connect(self.update_binning_setting)

        advanced_layout.addWidget(self.binning_label)
        advanced_layout.addWidget(self.binning_spinbox) 

        

        self.advanced_settings_container.setLayout(advanced_layout)
        self.advanced_settings_container.setVisible(False)
        layout.addWidget(self.advanced_settings_container)

        #Convert and save label
        self.convert_and_save_label = QLabel("Convert and save data")
        self.convert_and_save_label.setFont(bold_font)
        layout.addWidget(self.convert_and_save_label)

        # Convert button
        self.convert_and_save_button = QPushButton("Convert and save files")
        layout.addWidget(self.convert_and_save_button)

        # Terminal output
        self.terminal_output = QTextEdit()
        self.terminal_output.setReadOnly(True)
        self.terminal_output.setPlaceholderText("Terminal output...")
        layout.addWidget(self.terminal_output)

        # Abort button
        self.abort_button = QPushButton("Abort conversion job")
        layout.addWidget(self.abort_button)

        self.setLayout(layout)

    def toggle_advanced_settings(self):
        visible = self.advanced_toggle_btn.isChecked()
        self.advanced_settings_container.setVisible(visible)
        self.advanced_toggle_btn.setText(
            "Hide advanced settings" if visible else "Show advanced settings"
        )
        if visible:
            current_width = self.width()
            self.advanced_settings_container.adjustSize()
            self.resize(current_width, self.sizeHint().height())
        else:
            current_width = self.width()
            self.resize(current_width, self.sizeHint().height())
        
    def update_binning_setting(self, value):
        self.advanced_settings["time_binning"] = value
        self.print_to_terminal(f"Binning set to {value}")

    def get_open_file_paths(self):
        file_paths, _ = QFileDialog.getOpenFileNames(self, "Open File/s")
        return file_paths

    def get_open_folder_path(self):
        return QFileDialog.getExistingDirectory(self, "Choose Folder")

    def get_save_folder(self, selected_format):
        return QFileDialog.getExistingDirectory(self, "Save File")

    def add_files_to_list(self, file_paths, replace_files=True):
        if replace_files:
            self.file_list.clear()
        if not file_paths:
            self.print_to_terminal('No files found')
        else:
            for file_path in file_paths:
                self.file_list.addItem(os.path.basename(file_path))

    def delete_selected_files(self):
        for item in self.file_list.selectedItems():
            self.file_list.takeItem(self.file_list.row(item))

    def clear_all_files(self):
        self.file_list.clear()

    def print_to_terminal(self, message):
        self.terminal_output.append(message)
        QtGui.QGuiApplication.processEvents()

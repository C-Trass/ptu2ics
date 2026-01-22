

class FileConverterController:
    def __init__(self, view, model, loader_function, saver_functions):
        self.view = view
        self.model = model
        self.loader_function = loader_function
        self.saver_functions = saver_functions
        self.view.new_paths_btn.clicked.connect(lambda: self.choose_path(replace_files=True))
        self.view.add_paths_btn.clicked.connect(lambda: self.choose_path(replace_files=False))
        self.view.convert_and_save_button.clicked.connect(self.convert_and_save_files)
        self.file_paths = None
        

    def choose_path(self, replace_files=True):
        if self.view.radio1.isChecked():
            self.file_paths = self.view.get_open_file_paths()
        else:
            self.loaded_path = self.view.get_open_folder_path()
            if self.view.radio2.isChecked():
                self.file_paths = self.model.find_ptu_files_in_folder(self.loaded_path)
            elif self.view.radio3.isChecked():
                self.file_paths = self.model.find_ptu_files_in_subfolders(self.loaded_path)
        self.view.add_files_to_list(self.file_paths, replace_files=replace_files)
        # self.model.load_file(self.loaded_path, self.loader_function)
        # self.view.update_label(self.loaded_path)
        # self.view.fileLoaded.emit(self.loaded_path)

    def convert_and_save_files(self):
        selected_format = self.view.format_combo.currentText()
        folder_path = self.view.get_save_folder(selected_format)
        if self.file_paths and folder_path and selected_format in self.saver_functions:
            nr_files_to_convert = len(self.file_paths)
            i = 1
            for path in self.file_paths:
                self.view.print_to_terminal(f'Converting file %d out of %d' %(i, nr_files_to_convert))
                file_name = path.rsplit('.', 1)[0].split('/')[-1]
                self.model.convert_and_save_file(path, 
                                                 self.loader_function, 
                                                 self.saver_functions[selected_format], 
                                                 folder_path, 
                                                 file_name, 
                                                 self.view.advanced_settings)
                self.view.print_to_terminal(f'Finished converting and saving file %d out of %d' %(i, nr_files_to_convert))
                i += 1
            self.view.print_to_terminal(f'Finished converting and saving all files')
        else:
            self.view.print_to_terminal(f'Cannot perform conversion')
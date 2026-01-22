import os

class FileConverterModel:
    
    def convert_and_save_file(self, file_path, loader_function, saver_function, save_folder_path, save_folder_name, advanced_settings):
        """Load the file using an external loader function."""
        print('Loading file', file_path)
        file = loader_function(file_path)
        """Saves the numpy array using an external saver function."""
        if file is not None:
            print('Saving file')
            saver_function(file, save_folder_path, save_folder_name, advanced_settings)
        else:
            print('Cannot save empty file')

    def find_ptu_files_in_subfolders(self, folder_path):
        """Returns a list of all .ptu file paths in the given folder and its subfolders."""
        ptu_files = []
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(".ptu"):
                    ptu_files.append(os.path.join(root, file))
        return ptu_files
    
    def find_ptu_files_in_folder(self, folder_path):
        """Returns a list of all .ptu file paths in the given folder (excluding subfolders)."""
        file_list = [os.path.join(folder_path, file) for file in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, file)) and file.lower().endswith(".ptu")]
        if file_list != '':
            return file_list
        else:
            return []

from .save_data import save_data
from .save_ptufile_metadata_as_json import save_ptufile_metadata_as_json
from .save_advanced_settings_as_json import save_advanced_settings_as_json
import time
import numpy as np
import os

def save2tif(ptufile, save_folder_path, save_folder_name, advanced_settings):
    """First axis (frames) contains all the repeated scans performed to accumulate more signal. 
    We here sum over those repetitions"""
    #Exreact advanced settings
    time_bin = advanced_settings['time_binning']
    print('Saving to TIF with temporal binning = ', time_bin)
    decoded = ptufile.decode_image([Ellipsis, slice(None, None, time_bin)], frame=-1, asxarray=False)
    print('Shape of decoded = ', decoded.shape)
    """Add format to folder name"""
    save_folder_name += '_TIF'
    folderpath = os.path.join(save_folder_path, save_folder_name+'_'+time.strftime("%Y-%m-%d_%Hh%Mm%Ss"))

    os.makedirs(folderpath)

    data_save_path = os.path.join(folderpath, 'FLIM_data.tif')
    metadata_save_path = os.path.join(folderpath, 'metadata.json')
    adv_settings_save_path = os.path.join(folderpath, 'conversion_settings.json')

    allowed_types = [int, float, str, list]

    save_data(decoded, data_save_path, dtype=np.uint8)
    save_advanced_settings_as_json(advanced_settings, adv_settings_save_path, allowed_types=allowed_types)
    save_ptufile_metadata_as_json(ptufile, metadata_save_path, allowed_types=allowed_types)
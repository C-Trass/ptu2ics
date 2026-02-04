from .save_ICS import save_ics
from .save_ptufile_metadata_as_json import save_ptufile_metadata_as_json
from .save_advanced_settings_as_json import save_advanced_settings_as_json
import time
import numpy as np
import os

def save2ics(ptufile, save_folder_path, save_folder_name, advanced_settings):
    """First axis (frames) contains all the repeated scans performed to accumulate more signal. 
    We here sum over those repetitions"""
    #Exreact advanced settings
    time_bin = advanced_settings['time_binning']
    print('Saving to ICS with temporal binning = ', time_bin)
    decoded = ptufile.decode_image([Ellipsis, slice(None, None, time_bin)], frame=-1, asxarray=False)
    print('Shape of decoded = ', decoded.shape)
    """Add format to folder name"""
    save_folder_name += '_ICS'
    folderpath = os.path.join(save_folder_path, save_folder_name+'_'+time.strftime("%Y-%m-%d_%Hh%Mm%Ss"))

    os.makedirs(folderpath)

    metadata_save_path = os.path.join(folderpath, 'metadata.json')
    adv_settings_save_path = os.path.join(folderpath, 'conversion_settings.json')

    allowed_types = [int, float, str, list]

    for c in range(ptufile.number_channels):
        data_save_path = os.path.join(folderpath, f'FLIM_data_channel_%s.ics' % c)
        transposed_channel_data_item = np.transpose(decoded[0,:,:,c,:], axes=(0, 1, 2))#Does this do anything?
        save_ics(data_save_path, transposed_channel_data_item, ptufile.tcspc_resolution)
    save_advanced_settings_as_json(advanced_settings, adv_settings_save_path, allowed_types=allowed_types)
    save_ptufile_metadata_as_json(ptufile, metadata_save_path, allowed_types=allowed_types)
import json
import numpy as np

def save_advanced_settings_as_json(settings_dict, output_path, allowed_types):
    """Takes a settings dict and saves to a json file
    
    Input
    - settings_dict: the dict containing the advanced settings
    - output_path: path where to save the json
    - allowed_types: a list of the data types to save
    
    """
    # settings = {}

    # for key in dir(settings_dict):
    #     if not key.startswith("__") and not callable(getattr(settings_dict, key)):
    #         value = getattr(settings_dict, key)
            
    #         # Include only allowed types
    #         if isinstance(value, tuple(allowed_types)):
    #             # Convert NumPy arrays to lists
    #             if isinstance(value, np.ndarray):
    #                 settings[key] = value.tolist()
    #             else:
    #                 settings[key] = value
    # print(settings_dict)
    # # print(settings)  

    
    with open(output_path, "w") as f:
        json.dump(settings_dict, f, indent=4)
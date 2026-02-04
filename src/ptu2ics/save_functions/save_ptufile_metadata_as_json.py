import json
import numpy as np

def save_ptufile_metadata_as_json(file, output_path, allowed_types):
    """Takes a ptufile instance (from ptufile library) and saves 
    predefined metadata field types to a json file
    
    Input
    - file: the ptu file to same metadata from
    - output_path: path where to save the json
    - allowed_types: a list of the data types to save
    
    """
    metadata = {}

    for key in dir(file):
        if not key.startswith("__") and not callable(getattr(file, key)):
            value = getattr(file, key)
            
            # Include only allowed types
            if isinstance(value, tuple(allowed_types)):
                # Convert NumPy arrays to lists
                if isinstance(value, np.ndarray):
                    metadata[key] = value.tolist()
                else:
                    metadata[key] = value
    
    with open(output_path, "w") as f:
        json.dump(metadata, f, indent=4)
"""
@author: andreas.boden
"""
import os

import tifffile as tiff
import numpy as np



def reshape_to_5d(array, target_order):
    """
    Reshape an n-dimensional numpy array into a 5-dimensional array,
    adding empty dimensions where needed.
    
    Parameters:
        array (numpy.ndarray): The input n-dimensional array.
    
    Returns:
        numpy.ndarray: A 5-dimensional array.
    """
    array = np.array(array)

    # Get the shape of the original array
    shape = array.shape
    
    # Add 1s to the shape until it has 5 dimensions
    new_shape = shape + (1,) * (5 - len(shape))
    
    # Reshape the array
    reshaped = array.reshape(new_shape)

    # Reorder axes according to target_order
    result = np.transpose(reshaped, axes=target_order)
    return result

def save_data(data, path=None, dtype=None, vx_size=None, unit='px'):

    data = reshape_to_5d(data, [4,0,3,1,2])
    print('Data shape after reshape is: ', data.shape)
    if not dtype is None:
        try:
            data = data.astype(dtype)
        except:
            print('Could not convert data to specified type')
    else:
        data = data.astype(np.float32)

    if data.dtype == np.float64:
        data = data.astype(np.float32)
        print('WARNING: Converted float64 data to float32 to enable saving')

    if path is None:
        print('No file path given')

    print('Saving data in: ' + path)

    if vx_size is None:
        tiff.imwrite(path, data,
            imagej=True, metadata={'unit': unit,
                                   'axes': 'TZCYX'})
    else:
        vx_size = np.asarray(vx_size)
        if len(vx_size) == 1:
            tiff.imwrite(path, data, resolution=(1/vx_size[0], 1/vx_size[0]),
                imagej=True, metadata={'unit': unit,
                                       'axes': 'TZCYX'})
            print('Finished saving')
        elif len(vx_size) == 2:
            tiff.imwrite(path, data, resolution=(1/vx_size[0], 1/vx_size[1]),
                imagej=True, metadata={'unit': unit,
                                       'axes': 'TZCYX'})
            print('Finished saving')
        elif len(vx_size) == 3:
            tiff.imwrite(path, data, resolution=(1/vx_size[0], 1/vx_size[1]),
                imagej=True, metadata={'spacing': vx_size[2],
                                       'unit': unit,
                                       'axes': 'TZCYX'})
            print('Finished saving')
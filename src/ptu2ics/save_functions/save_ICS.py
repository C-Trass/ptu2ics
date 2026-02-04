import numpy as np
import gzip
import os

def save_ics(filename, data, micro_window_size, description="", origin=(0.0, 0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0, 1.0)):
    
    if not isinstance(data, np.ndarray): # Code for now tested on numpy arrays
        data = np.asarray(data)

    if not data.dtype == np.uint32: #TRI2 seems to want 32-bit integer data
        data = np.astype(data, np.uint32)

    shape = data.shape

    # Define the ICS header
    header = f'\t\nics_version\t2.0\n'
    header += f'filename\t{os.path.splitext(filename)[0]}\n'
    header += f'layout\tparameters\t4\n'
    header += f'layout\torder\tbits\tt\tx\ty\n'
    header += f'layout\tsizes\t32\t{shape[2]}\t{shape[0]}\t{shape[1]}\n'
    header += f'layout\tcoordinates\tvideo\n'
    header += f'layout\tsignificant_bits\t32\n'
    header += f'representation\tformat\tinteger\n'
    header += f'representation\tsign\tunsigned\n'
    header += f'representation\tcompression\tgzip\n'
    header += f'representation\tbyte_order\t1\t2\t3\t4\n'
    header += f'parameter\torigin\t{origin[0]}\t{origin[1]}\t{origin[2]}\t{origin[3]}\n'
    header += f'parameter\tscale\t{scale[0]}\t{scale[1]}\t{scale[2]}\t{scale[3]}\n'
    header += f'parameter\tunits\trelative\tns\tmicrons\tmicrons\n'
    header += f'parameter\tlabels\tmicro-time\tx-position\ty-position\n'
    header += f'history\tsoftware\tDIPlib 3.0.alpha\n'
    header += f'history\ttype\tTime Resolved\n'
    header += f'history\tlabels\tt x y\n'
    header += f'history\textents\t{micro_window_size} 0.000512 0.000512\n'
    header += f'history\tunits s m m\n'
    header += f'history\tdimensions\t{shape[0]}\t{shape[1]}\t{shape[2]}\n'
    header += f'end\t\n'

    # Write the header to the file
    with open(filename, 'wb') as f:
        f.write(header.encode('utf-8'))

    # Compress the data using gzip and append it to the file
    with gzip.open(filename, 'ab') as f:
        f.write(data.tobytes())
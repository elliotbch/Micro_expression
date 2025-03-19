from dv import AedatFile
import numpy as np
import struct
import os
import pandas as pd

aedat = True

# Transform from AEDAT4 to text file
if aedat:

    with open('test.txt', 'w') as out_file:
        with AedatFile('sourire2.aedat4') as f:
            # Access DVS events
            for event in f['events']:

                out_file.write(f"{event.timestamp} {event.x} {event.y} {int(event.polarity)}\n")        

# Transform from .csv to text file
else:

    df = pd.read_csv('demo3.csv', dtype={'timestamp': np.int64})  
    data_string = '\n'.join(df.apply(lambda x: ' '.join(x), axis=1))
    with open('myra_demo_csv.txt', 'w') as out_file:
        out_file.write(data_string)

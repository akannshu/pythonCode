""" wget https://www.dropbox.com/s/48gztwptustkqay/train.csv.zip  
    unzip train.csv.zip
"""

import pandas as pd
df = pd.read_csv('train.csv')
print(df.head())
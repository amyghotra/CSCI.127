#program 39

import pandas as pd

fileIn = input()
collision = pd.read_csv(fileIn)
print((collision["CONTRIBUTING FACTOR VEHICLE 1"].value_counts()[:3]))

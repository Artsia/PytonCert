# retieve data from file 
import json
import pandas as pd

with open('data.json') as f:
    data = json.load(f)



# list info about data before cleaning
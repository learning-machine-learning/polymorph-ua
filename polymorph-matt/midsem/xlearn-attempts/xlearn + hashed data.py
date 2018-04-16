import numpy as np
import pandas as pd
import xlearn as xl

table = pd.read_pickle("../data/Day1")

filtered = table[(~np.isnan(table["c_cnt"]))]

filtered.c_cnt.value_counts()

CLICKED_CNT = filtered.c_cnt.value_counts()[1]

# Getting number of elements in each column to determine whether we need the column
# If only one element in a column, we can delete it
# We can also use this info later to figure out how to discretize numerical data

# for col in filtered.columns:
#     try:
#         print(col, end=": ")
#         print(len(set(filtered[col])))
#     except TypeError as e:
#         print(e)

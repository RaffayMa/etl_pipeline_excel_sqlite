import pandas as pd
import sqlite3 as sql

# Load the data from the csv
df = pd.read_csv('messy-data.csv')
# Examine shape
print(df.shape)


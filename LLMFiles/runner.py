
import pandas as pd

df = pd.read_csv("demo-audio-data.csv", header=None)
cutoff = 58462

# Assuming the numbers are in the first (and only) column
# The first row was read as a header, so it's actually the first data point.
# I will rename the column to 0 for easier access.
df.columns = [0]

numbers_above_cutoff = df[df[0] > cutoff][0].sum()

print(f"Sum of numbers above cutoff: {numbers_above_cutoff}")

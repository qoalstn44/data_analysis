import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("./Regression2.xlsx", engine = "openpyxl")
print(df.describe())
df.groupby("female")
df.groupby("marry")
# gstat = df.groupby("retired")['total'].describe()
gstat = df.groupby("retire").describe()
df.iloc[:,]


print(gstat)
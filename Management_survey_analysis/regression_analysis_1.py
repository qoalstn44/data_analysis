import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
print(df.describe())
df.groupby("gender")
df.groupby("service")
# gstat = df.groupby("retired")['total'].describe()
gstat = df.groupby("edu").describe()
df.iloc[:,]


print(gstat)
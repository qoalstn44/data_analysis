import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
plt.scatter(df.edu, df.H003003)
plt.ylabel("H003003")
plt.xlabel("edu")
plt.title("Correlation between edu and H003003")
plt.show()

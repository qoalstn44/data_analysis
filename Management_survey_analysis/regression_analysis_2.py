import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
plt.scatter(df.gender, df.workperiod14)
plt.title("Correlation between gender and workperiod14")
plt.xlabel("gender")
plt.ylabel("workperiod14")
plt.show()

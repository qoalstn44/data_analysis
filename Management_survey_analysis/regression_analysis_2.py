import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
# plt.scatter(df.disa15, df.H003003)
# plt.title("Correlation between disa15 and H003003")
# plt.xlabel("disa15")
# plt.ylabel("H003003")
# plt.show()
import numpy as np
r = np.corrcoef(df.disa15, df.H003003)
print(r)
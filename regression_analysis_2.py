import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("./Regression2.xlsx", engine = "openpyxl")
plt.scatter(df.totexp, df.income)
plt.title("Correlation between medical expenditure (totexp) and income")
plt.xlabel("totexp")
plt.ylabel("income")
plt.show()
# import numpy as np
# r = np.corrcoef(df.totexp, df.income)
# print(r)
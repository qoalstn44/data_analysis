import numpy as np
import pandas as pd
import statsmodels.api as sm
df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
model = sm.OLS.from_formula('edu  ~ H002001 + H001001', data=df).fit()
print(model.summary())
model.summary()
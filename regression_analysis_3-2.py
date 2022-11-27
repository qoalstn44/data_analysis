import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
import statsmodels.formula.api as ols
import researchpy as rp
df = pd.read_excel("./Regression2.xlsx", engine = "openpyxl")
# X_cols = ['phylim','actlim','totchr','age','female','income']
X_cols = ['totchr','age','income']
X = df[X_cols]

model = ols('time ~ C(poison) * C(treat)', dat).fit()
anova_lm(model)
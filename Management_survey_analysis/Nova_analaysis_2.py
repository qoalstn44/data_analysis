import pandas as pd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
model = ols('gender ~ C(age4) * C(edu)', df).fit()
print(anova_lm(model))
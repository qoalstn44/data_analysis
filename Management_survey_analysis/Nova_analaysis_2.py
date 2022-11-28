from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import pandas as pd
df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
model = ols('age4 ~ C(service) * C(G005002)', df).fit()
print(anova_lm(model))
# # 경고 메세지 무시하기
# import pandas as pd
# from statsmodels.stats.anova import anova_lm
# from statsmodels.formula.api import ols
# import warnings
# warnings.filterwarnings('ignore')
# df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
# # the "C" indicates categorical data
# model = ols('disa15 ~ C(G012003)', df).fit()
# print(anova_lm(model))

# 경고 메세지 무시하기
import pandas as pd
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
formula = 'gender ~ C(disa15) + C(G012003) + C(disa15):C(G012003)'
lm = ols(formula, df).fit()
print(anova_lm(lm))
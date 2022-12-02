import scipy.stats as stats
import pandas as pd
import urllib
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import matplotlib.pyplot as plt
import numpy as np
import warnings
df = pd.read_excel("./2022F_IntroBusinessAnalytics_Data.xlsx", engine = "openpyxl")
warnings.filterwarnings('ignore')
df = pd.DataFrame(df, columns=['age4', 'G005001'])    
model = ols('G005001 ~ C(age4)', data=df).fit()
print(anova_lm(model))
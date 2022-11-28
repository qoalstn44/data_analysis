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

df = pd.DataFrame(df, columns=['age4', 'H003001'])    

# the "C" indicates categorical data


print(anova_lm(model))
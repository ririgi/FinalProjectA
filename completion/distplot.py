import warnings
warnings.filterwarnings("ignore")

import sys
sys.path.append('../')

import os
import time
import pandas as pd
import numpy as np

from utils import readChunk
from matplotlib import pyplot as plt
import seaborn as sns

import matplotlib.style as style

sns.set()
style.use('seaborn-poster')

df = readChunk("../sql/query_results/all_session_completion.csv")
df.dropna(subset = ['COMPLETION'], inplace = True)
df.COMPLETION = df.COMPLETION.astype(float)

plot = sns.distplot(df.COMPLETION.values)
plt.show()
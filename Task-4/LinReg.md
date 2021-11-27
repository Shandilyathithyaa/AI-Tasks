Importing Packages:
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from pydataset import data
import seaborn as sns

Code:
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X = diabetes_X[:, np.newaxis, 2]
plt.plot(diabetes_X,diabetes_y,'ro',alpha=0.5)

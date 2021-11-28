**Importing Packages:**  
```py
import numpy as np  
import pandas as pd  
from sklearn import datasets, linear_model  
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score  
from sklearn.model_selection import train_test_split  
from matplotlib import pyplot as plt  
from pydataset import data  
import seaborn as sns  
```

**Loading data and plotting it(one feature):**
```py
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)  
diabetes_X = diabetes_X[:, np.newaxis, 2]  
plt.plot(diabetes_X,diabetes_y,'ro',alpha=0.5)
```
![Image](Graphs/1.png)


The linear regression is a technique to model a given set of data to a corresponding label or quantity such that the model can be used later to predict a new set of data that falls under/similar set to the ones with which the model has been trained. It is generally used to predict a dataset that is distributed continuously over a range.
The object model creates a hypothesis by training using the training set passed to the `fit()` function. Then the predictions are obtained using `predict()`. Finally for result analysis we find Coefficients, MeanSquaredError and Coefficient of Determination.

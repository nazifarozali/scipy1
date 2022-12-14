# -*- coding: utf-8 -*-
"""exercise.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x8bScTBIRMrYE-R1quO7rB7okCT5zAUJ

Task for your group discussion
Part A
1. Load your own group data
2. EDA
3. Choose any ML model
4. Split the data into training and test dataframes
5. Perform ML
6. Given report

Part B
1. save as a python code
2. load into Github
3. update the libraries used in the requirements file
4. Deploy
"""

!pip install sweetviz

import pandas as pd

pen = pd.read_csv('/content/penguins.csv')
pen.head()

df=pen.dropna()
print(df)

# importing sweetviz library
import sweetviz as sv

#analyzing the dataset
advert_report = sv.analyze(df)

#display the report
advert_report.show_html('/content/penguins.csv')

advert_report.show_notebook()

X_pen = df.drop(['species','island','sex'], axis=1)  
y_pen = df['species']

df.shape

len(df.columns)

df.info()

df.describe()

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X_pen, y_pen,random_state=50)
Xtrain.head()

Xtrain.shape

Xtest.shape

from sklearn.naive_bayes import GaussianNB # 1. choose model class
model = GaussianNB()                       # 2. instantiate model
model.fit(Xtrain, ytrain)                  # 3. fit model to data
y_model = model.predict(Xtest)#output      # 4. predict on new data

from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)

from sklearn.metrics import classification_report

print(classification_report(ytest, y_model))

# Confusion Matrix
from sklearn.metrics import confusion_matrix 
confusion_matrix(ytest, y_model)

#Confusion Matrix
import matplotlib.pyplot as plt
from sklearn import metrics
import numpy as np
confusion_matrix = metrics.confusion_matrix(ytest, y_model)

print(confusion_matrix)

cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix,display_labels=np.unique(y_pen))

cm_display.plot()
plt.show()

from sklearn.metrics import classification_report
# F1 score = 2 / [ (1/precision) + (1/ recall)]
print(classification_report(ytest, y_model))


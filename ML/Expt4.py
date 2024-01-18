import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


df = pd.read_csv("mushrooms.csv")
print(df.head())

data = pd.get_dummies(df, df.columns[df.dtypes == "object"])
print(data.head())

X = data.drop(columns=["class_p", "class_e"])
y = data["class_e"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
y_p = dtc.predict(X_test)
print(y_p)
print("Accuracy of Model::", accuracy_score(y_test, y_p))

plot_tree(dtc)
plt.show()

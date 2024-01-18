import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("mushrooms.csv")
print(df.head())

data = pd.get_dummies(df, df.columns[df.dtypes == "object"])
print(data.head())

X = data.drop(columns=["class_p", "class_e"])
y = data["class_e"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

xgc = XGBClassifier().fit(X_train, y_train)
y_p = xgc.predict(X_test)
print(y_p)
print("Accuracy of Model::", accuracy_score(y_test, y_p))

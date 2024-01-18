import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sb

df = pd.read_csv("mushrooms.csv")
print(df.head())

data = pd.get_dummies(df, df.columns[df.dtypes == "object"])
print(data.head())

X = data.drop(columns=["class_p", "class_e"])
y = data["class_e"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

gnb = GaussianNB().fit(X_train, y_train)
y_p = gnb.predict(X_test)
print(y_p)
print("Accuracy of Model::", accuracy_score(y_test, y_p))
sb.heatmap(confusion_matrix(y_test, y_p), cmap="viridis_r", annot=True, fmt="d")

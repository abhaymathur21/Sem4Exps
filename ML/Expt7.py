import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier


df = pd.read_csv("mushrooms.csv")
print(df.head())

data = pd.get_dummies(df, df.columns[df.dtypes == "object"])
print(data.head())

X = data.drop(columns=["class_p", "class_e"])
y = data["class_e"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)

dtc = DecisionTreeClassifier().fit(X_train, y_train)
xgc = XGBClassifier().fit(X_train, y_train)
rfc = RandomForestClassifier().fit(X_train, y_train)
gnb = GaussianNB().fit(X_train, y_train)

k = 5

dtc_score = cross_val_score(dtc, X, y, cv=k)
xgc_score = cross_val_score(xgc, X, y, cv=k)
rfc_score = cross_val_score(rfc, X, y, cv=k)
gnb_score = cross_val_score(gnb, X, y, cv=k)

print(
    "Decision Tree:",
    dtc_score,
    "Accuracy:",
    accuracy_score(y_test, dtc.predict(X_test)),
)
print("XGBoost:", xgc_score, "Accuracy:", accuracy_score(y_test, xgc.predict(X_test)))
print(
    "Random Forest:",
    rfc_score,
    "Accuracy:",
    accuracy_score(y_test, rfc.predict(X_test)),
)
print(
    "Gaussian Naive Bayes:",
    gnb_score,
    "Accuracy:",
    accuracy_score(y_test, gnb.predict(X_test)),
)

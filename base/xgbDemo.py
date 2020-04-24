import numpy as np
import scipy.sparse
import pickle
import xgboost as xgb
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
from sklearn.metrics import confusion_matrix, mean_squared_error

readFileName = "german_credit.csv"

df = pd.read_csv(readFileName)
list_columns = list(df.columns[:-1])
x = df.iloc[:, 1:]
y = df.iloc[:, 0]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=0.2)

param = {'max_depth': 2, 'eta': 1, 'silent': 1, }
# XGBoost训练过程
xgb.XGBRegressor
model = xgb.XGBClassifier(max_depth=5, learning_rate=0.1, n_estimators=160)
model.fit(x_train, y_train)

print(cross_val_score(model, x_test, y_test, cv=10))
print(model.score(x_train, y_train))
print(model.score(x_test, y_test))

tr = []
te = []
rangeIndex = 501

for i in range(rangeIndex):
    clf = xgb.XGBClassifier(random_state=25
                            , criterion="entropy"
                            , n_estimators=i + 1
                            )
    clf = clf.fit(x_train, y_train)
    score_tr = clf.score(x_train, y_train)
    score_te = cross_val_score(clf, x_test, y_test, cv=10).mean()
    tr.append(score_tr)
    te.append(score_te)
print(max(te))
plt.plot(range(1, rangeIndex), tr, color="red", label="train")
plt.plot(range(1, rangeIndex), te, color="blue", label="test")
plt.xticks(range(1, rangeIndex))
plt.legend()
plt.show()

# 对测试集进行预测
# ans = model.predict(x_test,y_test)

# print(ans)
# print(y_test)

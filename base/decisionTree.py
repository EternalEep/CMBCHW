from sklearn import tree
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd
from sklearn.metrics import confusion_matrix, mean_squared_error

readFileName = "german_credit.csv"
# 读取数据
df = pd.read_csv(readFileName)
list_columns = list(df.columns[:-1])
x = df.iloc[:, 1:]
y = df.iloc[:, 0]
# 训练集合 测试集合
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)

# 模型参数控制
clf = tree.DecisionTreeClassifier(max_depth=10000, criterion='entropy')
# 训练模型
clf.fit(x_train, y_train)
# 测试模型在测试集合表现
result = clf.score(x_test, y_test)

#
print(cross_val_score(clf, x_test, y_test, cv=10))

print(result)

import graphviz
from sklearn import tree

n_features = x.columns
dot_data = tree.export_graphviz(clf, out_file=None
                                , feature_names=n_features
                                , class_names=["good", "bad"]
                                , filled=True

                                )
graph = graphviz.Source(dot_data)
graph.view()

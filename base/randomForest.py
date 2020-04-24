import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import pandas as pd

trees = 1000
readFileName = "german_credit.csv"

df = pd.read_csv(readFileName)
X = df.iloc[:, 1:]
y = df.iloc[:, 0]
#
# print(X)
# print(y)
names = X.columns
# default=0.25
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.4, )
forest = RandomForestClassifier(n_estimators=100)  # 默认值为10
forest.fit(x_train, y_train)

print(cross_val_score(forest, x_test, y_test, cv=10))
print(cross_val_score(forest, x_test, y_test, cv=10).mean())

print(forest.score(x_train, y_train))
print(forest.score(x_test, y_test))

n_features = X.shape[1]
plt.barh(range(n_features), forest.feature_importances_, align="center")
plt.yticks(np.arange(n_features), names)
plt.title("random forest %d trees:" % trees)
plt.xlabel("Feature Importances")
plt.ylabel("Feature")
plt.show()



import graphviz
from sklearn.tree import export_graphviz


dot_data = export_graphviz(forest.estimators_[44]

                              ,feature_names = names

                                , class_names=["good", "bad"]
                                ,rounded = True, proportion = False,
                                 precision = 2, filled = True
                                )


graph = graphviz.Source(dot_data)
graph.view()

# Convert to png using system command (requires Graphviz)
# from subprocess import call
# call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])
#
# # Display in jupyter notebook
# from IPython.display import Image
# Image(filename = 'tree3.png')


# from sklearn import datasets
# from sklearn.ensemble import RandomForestClassifier
# from IPython.display import Image
# from sklearn import tree
# import pydotplus
# import os
# Estimators = classifier.estimators_
# for index, model in enumerate(Estimators):
#     filename = 'iris_' + str(index) + '.pdf'
#     dot_data = tree.export_graphviz(model , out_file=None,
#                          feature_names=iris.feature_names,
#                          class_names=iris.target_names,
#                          filled=True, rounded=True,
#                          special_characters=True)
#     graph = pydotplus.graph_from_dot_data(dot_data)
#     # 使用ipython的终端jupyter notebook显示。
#     Image(graph.create_png())
#     graph.write_pdf(filename)
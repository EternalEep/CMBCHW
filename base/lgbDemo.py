import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import lightgbm as lgb
import pandas as pd
from sklearn.metrics import mean_squared_error

trees = 1000
readFileName = "german_credit.csv"

df = pd.read_csv(readFileName)
X = df.iloc[:, 1:]
y = df.iloc[:, 0]
#
# print(X)
# print(y)
names = X.columns
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=0)
# 构建lgb中的Dataset格式
lgb_train = lgb.Dataset(x_train, y_train)
lgb_eval = lgb.Dataset(x_test, y_test, reference=lgb_train)

# 敲定好一组参数
params = {
    'task': 'train',
    'boosting_type': 'gbdt',
    'objective': 'regression',
    'metric': {'l2', 'auc'},
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0
}

print('开始训练...')
# 训练
gbm = lgb.train(params,
                lgb_train,
                num_boost_round=20,
                valid_sets=lgb_eval,
                early_stopping_rounds=5)

# 保存模型
print('保存模型...')
# 保存模型到文件中
gbm.save_model('model.txt')


print('开始预测...')
# 预测
y_pred = gbm.predict(x_test, num_iteration=gbm.best_iteration)
# 评估
# print(gbm.score(x_train, y_train))
# print(gbm.score(x_test, y_test))
print('预估结果的rmse为:')
print(mean_squared_error(y_test, y_pred) ** 0.5)

ax = lgb.plot_importance(gbm, max_num_features=20)
plt.savefig('lgbPicture')
plt.show()
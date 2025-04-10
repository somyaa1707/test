import xgboost as xgb
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
X, y = make_classification(n_samples=1000, n_features=20, 
                           n_informative=15, n_redundant=5,
                           random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X, y, 
                                                  test_size=0.2, 
                                                  random_state=42)
dtrain = xgb.DMatrix(X_train, label=y_train)
dval = xgb.DMatrix(X_val, label=y_val)
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'logloss',
    'learning_rate': 0.1,
    'max_depth': 3,
    'seed': 42
}
evals = [(dtrain, 'train'), (dval, 'validation')]
evals_result = {}
model = xgb.train(params=params,
                  dtrain=dtrain,
                  num_boost_round=500,
                  evals=evals,
                  early_stopping_rounds=10,
                  evals_result=evals_result,
                  verbose_eval=False)
epochs = len(evals_result['train']['logloss'])
x_axis = range(epochs)
plt.figure(figsize=(10, 6))
plt.plot(x_axis, evals_result['train']['logloss'], label='Train')
plt.plot(x_axis, evals_result['validation']['logloss'], label='Validation')
plt.xlabel('Boosting Rounds')
plt.ylabel('Log Loss')
plt.title('XGBoost Log Loss vs Iterations')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
bagging = BaggingClassifier(estimator=DecisionTreeClassifier(), n_estimators=50, random_state=42)
adaboost = AdaBoostClassifier(estimator=DecisionTreeClassifier(max_depth=1), n_estimators=50, random_state=42)
bagging.fit(X_train, y_train)
adaboost.fit(X_train, y_train)
y_pred_bagging = bagging.predict(X_test)
y_pred_adaboost = adaboost.predict(X_test)
print("BaggingClassifier:")
print(f"  Accuracy:  {accuracy_score(y_test, y_pred_bagging):.4f}")
print(f"  Precision: {precision_score(y_test, y_pred_bagging):.4f}")
print(f"  Recall:    {recall_score(y_test, y_pred_bagging):.4f}")

print("\nAdaBoostClassifier:")
print(f"  Accuracy:  {accuracy_score(y_test, y_pred_adaboost):.4f}")
print(f"  Precision: {precision_score(y_test, y_pred_adaboost):.4f}")
print(f"  Recall:    {recall_score(y_test, y_pred_adaboost):.4f}")

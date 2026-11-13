
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from imblearn.over_sampling import SMOTENC
from imblearn.pipeline import Pipeline as ImbPipeline


# 1. Load Dataset
df = pd.read_csv("ecommerce_delivery_predictions.csv")


# 2. EDA
print("Dataset Shape:", df.shape)
print(df.head())
print(df.info())
print(df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print(df.describe())

print("\nTarget Distribution:")
print(df['late_delivery'].value_counts())

sns.countplot(data=df, x='late_delivery')
plt.title("Late Delivery Distribution")
plt.show()

plt.figure(figsize=(12, 8))
sns.heatmap(df.select_dtypes(include=np.number).corr(), cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


# 3. Preprocessing
df.drop(['seller_id', 'order_id', 'customer_id'],
        axis=1, inplace=True)

df['order_date'] = pd.to_datetime(df['order_date'])

df['order_year'] = df['order_date'].dt.year
df['order_month'] = df['order_date'].dt.month
df['order_day'] = df['order_date'].dt.day
df['order_dayofweek'] = df['order_date'].dt.dayofweek

df.drop('order_date', axis=1, inplace=True)

df.dropna(subset=['late_delivery'], inplace=True)


# 4. X and y
X = df.drop('late_delivery', axis=1)
y = df['late_delivery'].astype(int)

cat_cols = X.select_dtypes(include='object').columns.tolist()
num_cols = X.select_dtypes(include=np.number).columns.tolist()


# 5. Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 6. Preprocessing
cat_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

num_pipe = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

preprocessor = ColumnTransformer([
    ('cat', cat_pipe, cat_cols),
    ('num', num_pipe, num_cols)
])


# 7. SMOTENC
smote = SMOTENC(
    categorical_features=cat_cols,
    random_state=42
)


# 8. Logistic Regression Model
model = ImbPipeline([
    ('smote', smote),
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000))
])


# 9. Hyperparameter Tuning
param_grid = {
    'classifier__C': [0.01, 0.1, 1, 10, 100],
    'classifier__solver': ['lbfgs', 'liblinear'],
    'classifier__l1_ratio': [0]
}

grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=3,
    scoring='accuracy',
    n_jobs=1,
    pre_dispatch=1,
    verbose=1
)


# 10. Training
grid.fit(X_train, y_train)


# 11. Best Parameters
print("\nBest Parameters:", grid.best_params_)
print("Best CV Score:", grid.best_score_)


# 12. Best Model
best_lr = grid.best_estimator_


# 13. Prediction
y_pred = best_lr.predict(X_test)


# 14. Evaluation
print("\nAccuracy:", accuracy_score(y_test, y_pred) * 100)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# 15. Actual and Predicted Values
print("\nActual Test Values:")
print(y_test.value_counts())

print("\nPredicted Test Values:")
print(pd.Series(y_pred).value_counts())


# 16. Save Model
joblib.dump(best_lr, "ecommerce_delivery_predictions.pkl")

print("\nBest Model Saved Successfully!")

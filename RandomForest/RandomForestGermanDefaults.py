# Fetch repo from https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data 
from ucimlrepo import fetch_ucirepo 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
import numpy as np


# Fetch dataset 
statlog_german_credit_data = fetch_ucirepo(id=144)

# Combine features and targets into one DataFrame
df = pd.concat([statlog_german_credit_data.data.features, 
                statlog_german_credit_data.data.targets], axis=1)

# Rename target column and convert to binary (1 = Bad, 0 = Good)
df = df.rename(columns={'class': 'target'})
df['target'] = df['target'].replace({1: 0, 2: 1})  # 1=Default (Bad), 0=No Default (Good)

# Verify the data
print(df.head())
# Counts Defaults and No defaults
print("\nTarget distribution:")
print(df['target'].value_counts())

# EDA (Exploratory Data Analysis:) Plot target distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='target', data=df)
plt.title('Distribution of Credit Defaults (0=Good, 1=Bad)')
plt.show()

# Show categorical columns
cat_cols = df.select_dtypes(include=['object']).columns

# Preprocessing: encode categorical variables 
# Creates True/False values for each categorical variable with
# each Attribute Code
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)

# Split data for training and testing
# Independent variables
X = df_encoded.drop('target', axis=1)
# Dependent variable
y = df_encoded['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
cost_matrix = {0: 1, 1: 5}
rf = RandomForestClassifier(
    n_estimators=100,  # Number of trees
    max_depth=5,       # Control tree depth (avoid overfitting)
    class_weight= cost_matrix,  # or use cost_matrix = {0: 1, 1: 5}
    random_state=42,
    min_samples_split=2
)
rf.fit(X_train, y_train)

# Predictions
y_pred = rf.predict(X_test)
y_proba = rf.predict_proba(X_test)[:, 1]  # Probabilities for Class 1 (Bad)

print(classification_report(y_test, y_pred))

# Confusion matrix
xAxisLabels = ['Predicted: Good (0)', 'Predicted: Bad (1)']
yAxisLabels = ['Actual: Good (0)', 'Actual: Bad (1)']
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', 
            xticklabels=xAxisLabels,  yticklabels=yAxisLabels)
plt.title('Confusion Matrix')
plt.show()

print(f"ROC-AUC: {roc_auc_score(y_test, y_proba):.2f}")

# Plot top 10 important features
importances = pd.Series(rf.feature_importances_, index=X.columns)
importances.nlargest(10).sort_values(ascending=True).plot(kind='barh')
plt.title('Top 10 Feature Importances')
plt.show()

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 7],
    'min_samples_split': [2, 5]
}

grid_search = GridSearchCV(rf, param_grid, cv=5, scoring='roc_auc')
grid_search.fit(X_train, y_train)
print(f"Best params: {grid_search.best_params_}")

# Extract results from GridSearchCV
results = pd.DataFrame(grid_search.cv_results_)
params = ['param_max_depth', 'param_n_estimators', 'param_min_samples_split']
mean_scores = results['mean_test_score']
# print(results.head(10))
# Pivot for heatmap
heatmap_data = results.pivot_table(index='param_max_depth', 
                                   columns='param_n_estimators', 
                                   values='mean_test_score',
                                   aggfunc='mean')

plt.figure(figsize=(10, 6))
sns.heatmap(heatmap_data, annot=True, fmt=".3f", cmap="YlGnBu", cbar_kws={'label': 'ROC-AUC'})
plt.title("GridSearchCV Results: Max Depth vs. N Estimators")
plt.show()
# Fetch repo from https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data 
from ucimlrepo import fetch_ucirepo 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

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

# Show categorical variables
cat_vars = df.select_dtypes(include=['object', 'category']).columns
print("Categorical variables:")
print(cat_vars)
# Show numerical variables
num_vars = df.select_dtypes(exclude=['object', 'category']).columns
num_vars = num_vars.drop('target')
print("Numerical variables:")
print(num_vars)

# Preprocessing: encode categorical variables 
# Creates True/False values for each categorical variable with
# each Attribute Code
df_encoded = pd.get_dummies(df, columns=cat_vars, drop_first=True)

# Split data for training and testing
# Independent variables
X = df_encoded.drop('target', axis=1)
# Dependent variable
y = df_encoded['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit and transform X_train from numerical variables
scaler = StandardScaler()
# we cannot use the fit() method on the test dataset, because it will be the wrong 
# approach as it could introduce bias to the testing dataset.
# converts the column of interest by transforming it to a range of numbers with 
# mean = 0 and standard deviation = 1.
X_train[num_vars] = scaler.fit_transform(X_train[num_vars])
X_test[num_vars] = scaler.transform(X_test[num_vars])
# Define custom class weights based on cost matrix
cost_matrix = {0: 1, 1: 5}  # Weighting misclassification cost
# Fit logistic regression
model = LogisticRegression(class_weight=cost_matrix)  # Uses cost_matrix to weigh classifications
# model = LogisticRegression(class_weight='balanced')  # replicates the smaller class until you have as many samples as in the larger one
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Classification report
print(classification_report(y_test, y_pred))
xAxisLabels = ['Predicted: Good (0)', 'Predicted: Bad (1)']
yAxisLabels = ['Actual: Good (0)', 'Actual: Bad (1)']

# Confusion matrix
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', 
            xticklabels=xAxisLabels,  yticklabels=yAxisLabels)
plt.title('Confusion Matrix')
plt.show()

# ROC-AUC score
# Get predicted probabilities for class 1 (Default/Bad Credit)
y_probs = model.predict_proba(X_test)[:, 1]

# Calculate ROC-AUC
auc_score = roc_auc_score(y_test, y_probs)

# Print formatted result with 2 decimals
print(f"ROC-AUC Score: {auc_score:.2f}")
# Plot coefficients (top 10)
coef_df = pd.DataFrame({'feature': X_train.columns, 'coef': model.coef_[0]})
coef_df = coef_df.sort_values(by=['coef'], ascending=True).head(10)
sns.barplot(x='coef', y='feature', data=coef_df)
plt.title('Top 10 Features Influencing Default Risk')
plt.show()

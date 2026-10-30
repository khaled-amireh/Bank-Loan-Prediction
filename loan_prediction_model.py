import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.svm import SVC

# 1. Import the Dataset
df = pd.read_csv('credit_risk_dataset.csv')
X = df.drop(['loan_status'], axis=1)
y = df['loan_status']

# 2. Exploratory Data Analysis (EDA)
print('--- Dataset Info ---')
df.info()

print('\n--- Dataset Description ---')
print(df.describe())

print('\n--- Missing Values Count ---')
pd.set_option('display.max_rows', None)
print(df.isnull().sum().sort_values(ascending=False))

# 3. Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Data Preprocessing - Handling Missing Values
missing_cols = ['loan_int_rate', 'person_emp_length']
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X_train[missing_cols] = imputer.fit_transform(X_train[missing_cols])
X_test[missing_cols] = imputer.transform(X_test[missing_cols])

print('\n--- Missing Values Verification ---')
print(pd.DataFrame({'train': X_train.isnull().sum(), 'test': X_test.isnull().sum()}))

# 5. Encoding Categorical Data
categorical_columns = [
    'person_home_ownership',
    'loan_intent',
    'loan_grade',
    'cb_person_default_on_file',
]
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), categorical_columns)],
    remainder='passthrough',
)
X_train = ct.fit_transform(X_train)
X_test = ct.transform(X_test)

# 6. Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 7. Train the Model
classifier = SVC(kernel='rbf', class_weight='balanced', random_state=42)
classifier.fit(X_train, y_train)

# 8. Predicting Test Results
y_pred = classifier.predict(X_test)

# 9. Evaluation
print('\n--- Model Performance Evaluation ---')
print('Accuracy Score:', accuracy_score(y_test, y_pred))
print('\nClassification Report:\n', classification_report(y_test, y_pred))

# Plot Visual Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['Approved (0)', 'Defaulted (1)'],
    yticklabels=['Approved (0)', 'Defaulted (1)'],
)
plt.title('Confusion Matrix - Kernel SVM')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tight_layout()
plt.show()

# 10. Single Applicant Prediction
sample_applicant = X_test[0].reshape(1, -1)
prediction = classifier.predict(sample_applicant)
print(
    '\nLoan Decision:',
    'Approved' if prediction[0] == 0 else 'Default Risk / Rejected',
)

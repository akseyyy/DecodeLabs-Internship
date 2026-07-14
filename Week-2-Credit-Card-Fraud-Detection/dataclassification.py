# ==========================================
# Project 2: Credit Card Fraud Detection
# Classification using Decision Tree
# ==========================================

# Import Libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ------------------------------------------
# Step 1: Load Dataset
# ------------------------------------------
df = pd.read_csv("credit_card_fraud_10k.csv")

# ------------------------------------------
# Step 2: Understand Dataset
# ------------------------------------------
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# ------------------------------------------
# Step 3: Data Cleaning
# ------------------------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# ------------------------------------------
# Step 4: Encode Categorical Data
# ------------------------------------------
encoder = LabelEncoder()

if "merchant_category" in df.columns:
    df["merchant_category"] = encoder.fit_transform(df["merchant_category"])

# ------------------------------------------
# Step 5: Feature Selection
# ------------------------------------------
X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

# ------------------------------------------
# Step 6: Split Dataset
# ------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# ------------------------------------------
# Step 7: Train Model
# ------------------------------------------
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

# ------------------------------------------
# Step 8: Prediction
# ------------------------------------------
y_pred = model.predict(X_test)

# ------------------------------------------
# Step 9: Model Evaluation
# ------------------------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ------------------------------------------
# Step 10: Predict New Transaction
# ------------------------------------------

print("\nPredicting First Test Record...")

sample = X_test.iloc[[0]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("Prediction: Fraud Transaction")
else:
    print("Prediction: Not Fraud Transaction")
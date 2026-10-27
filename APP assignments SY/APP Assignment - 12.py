import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample customer churn dataset
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Age': [25, 35, np.nan, 45, 30, 50, 40, 35],
    'MonthlyCharges': [500, 700, 600, np.nan, 800, 900, 650, 700],
    'Tenure': [2, 12, 5, 24, 36, 48, 6, 18],
    'Contract': ['Monthly', 'Yearly', 'Monthly', 'Yearly',
                 'Monthly', 'Yearly', 'Monthly', 'Yearly'],
    'Churn': ['Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Display original dataset
print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values using column means
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['MonthlyCharges'] = df['MonthlyCharges'].fillna(
    df['MonthlyCharges'].mean()
)

# Remove duplicate records
df = df.drop_duplicates()

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df)

# Generate summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Calculate churn percentage
churn_percentage = (df['Churn'] == 'Yes').mean() * 100
print("\nCustomer Churn Percentage:", churn_percentage, "%")

# Visualize churn distribution
df['Churn'].value_counts().plot(kind='bar')
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

# Compare tenure for churned and retained customers
df.boxplot(column='Tenure', by='Churn')
plt.title("Tenure vs Customer Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Tenure (Months)")
plt.tight_layout()
plt.show()

# Compare monthly charges for churned and retained customers
df.boxplot(column='MonthlyCharges', by='Churn')
plt.title("Monthly Charges vs Customer Churn")
plt.suptitle("")
plt.xlabel("Churn")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.show()

# Analyze contract type and churn
pd.crosstab(df['Contract'], df['Churn']).plot(kind='bar')
plt.title("Contract Type vs Customer Churn")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

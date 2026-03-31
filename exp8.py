import pandas as pd

# Load dataset
data = pd.read_csv("employee_data.csv")

print("Original Dataset:\n")
print(data)

# -------- Test Case 1 --------
# Replace missing salary values with column mean
mean_salary = data["Salary"].mean()
data["Salary"] = data["Salary"].fillna(round(mean_salary,2))

print("\nAfter replacing missing Salary values with mean:\n")
print(data)

# -------- Test Case 2 --------
# Remove duplicate records
data = data.drop_duplicates()

print("\nAfter removing duplicate entries:\n")
print(data)

# -------- Data Transformation --------
# Convert Date column to datetime format
data["Date"] = pd.to_datetime(data["Date"])

# Convert Performance Score to numeric (if needed)
data["Score"] = pd.to_numeric(data["Score"])

print("\nFinal Cleaned Dataset:\n")
print(data)
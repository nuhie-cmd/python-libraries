import pandas as pd   # Import pandas library

# -----------------------------
# Test Case 1: Sales Data
# -----------------------------

# Create sample sales dataset
sales_data = {
    "Region": ["North", "South", "East", "West", "North", "South", "East"],
    "Product": ["A", "B", "A", "B", "C", "A", "C"],
    "Revenue": [2000, 1500, 1800, 2200, 2500, 1700, 2100]
}

sales_df = pd.DataFrame(sales_data)

print("Sales Data:")
print(sales_df)

# Group sales by Region and calculate total revenue
region_sales = sales_df.groupby("Region")["Revenue"].sum()

print("\nTotal Revenue by Region:")
print(region_sales)


# -----------------------------
# Test Case 2: Student Data
# -----------------------------

student_data = {
    "Name": ["Rahul", "Anita", "Kiran", "Meena", "Arjun", "Sneha"],
    "Department": ["CS", "IT", "CS", "ECE", "IT", "CS"],
    "Marks": [85, 78, 90, 88, 76, 92]
}

student_df = pd.DataFrame(student_data)

print("\nStudent Data:")
print(student_df)

# Group students by department and find average marks
avg_marks = student_df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(avg_marks)
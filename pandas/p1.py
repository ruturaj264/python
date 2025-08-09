import pandas as pd

# data = [10, 20, 30, 40]
# s = pd.Series(data)
# print(s)

# Output
# 0    10
# 1    20
# 2    30
# 3    40

# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35]
# }
# df = pd.DataFrame(data)
# print(df)

# Output
#       Name  Age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35

# df = pd.read_csv("C:/Users/rrutu/Desktop/DataBricks/Indian_Kids_Screen_Time.csv")

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35, 25, 30, 35, 25, 30, 35, 25, 30, 35],
    'Gender' : ['M', 'F', 'F', 'M', 'F', 'F', 'M', 'F', 'F', 'M', 'F', 'F']
}
df = pd.DataFrame(data)

# print(df.head())              # Returns first 5 rows
# print(df.tail())              # Returns last 5 rows
# print(df.shape)               # (rows, columns)
# print(df.columns)             # Index(['Name', 'Age', 'Gender'], dtype='object')
# print(list(df.columns))       # ['Name', 'Age', 'Gender']
# print(df.info())              # For each column, returns number of non-null values and datatype
# print(df.describe())          # For numeric columns, returns summary like count, mean, min, max etc

# print(df['Name'])             # Returns only Name column
# print(df[['Name', 'Gender']]) # Returns only Name and Gender column
# print(df.iloc[0:4])           # Returns first 4 rows

# print(df['Age'] > 30)         # For each row, returns True or False based on condition
# print(df[df['Age'] > 30])     # returns only rows where condition matches

# Adds new column as Salary and assign given values in sequence

# df['Salary'] = [50000, 60000, 70000, 50000, 60000, 70000, 50000, 60000, 70000, 50000, 60000, 70000]
# print(df)

# print(df.sort_values('Age', ascending=False))   # Return new dataframe by sorting previous as per condition

# print(df.groupby('Gender')['Age'].sum())    # Group the dataframe based on input

# Creates new csv/exel file from dataframe. index=False means dont include index as a column

# df.to_csv("C:/Users/rrutu/Desktop/DataBricks/output1.csv", index=False)
# df.to_excel("C:/Users/rrutu/Desktop/DataBricks/output2.xlsx", index=False)

# -*- coding: utf-8 -*-
"""Exploratory Data Analysis of a Car Dataset.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lfN3D5neYUGvqJwS-CSLq0uEmSbmsosW
"""

import pandas as pd
import numpy as np

# reading our dataset

data= pd.read_csv("/content/Cars_data.csv")
data.head()

# total row and columns

data.shape

# basic statistics

data.describe()

# all columns

columns = list(data)
print(columns)

# chacking null values

data.isnull().sum()

# calculating total zero in ['Make', 'Model', 'Year', 'Transmission Type', 'Driven_Wheels', 'Number of Doors', 'Vehicle Size', 'Vehicle Style', 'highway MPG', 'city mpg', 'Popularity', 'MSRP']

(data[columns[1:16]] == 0).sum()

# replace statement

data[columns[1:16]]= data[columns[1:16]].replace(0, np.nan)

data.isnull().sum()

data.shape

data.dropna(inplace=True)

data.shape

# chacking nan and zero value
data.isnull().sum()

"""# Task
Tell me about this dataset.

Here is all the data you need:
"Cars_data.csv"

## Data loading

### Subtask:
Load the data from "Cars_data.csv" into a dataframe.

**Reasoning**:
Import the pandas library, read the CSV file into a DataFrame, and display the first 5 rows.
"""

import pandas as pd
df = pd.read_csv('Cars_data.csv')
display(df.head())

"""## Data exploration

### Subtask:
Explore the dataset to understand its structure, columns, data types, and summary statistics.

**Reasoning**:
Display the shape of the dataframe, print the information about the dataframe, and generate descriptive statistics for both numerical and non-numerical columns to understand the dataset's structure, data types, and summary statistics.
"""

display(df.shape)
df.info()
display(df.describe())
display(df.describe(include='object'))

"""## Data analysis

### Subtask:
Analyze key aspects of the dataset, such as the distribution of different car attributes.

**Reasoning**:
Calculate the number of unique values and the most frequent values for each categorical column, then calculate the average MSRP for each make, and finally calculate the correlation matrix for numerical columns.
"""

categorical_cols = ['Make', 'Model', 'Engine Fuel Type', 'Transmission Type', 'Driven_Wheels', 'Market Category', 'Vehicle Size', 'Vehicle Style']
for col in categorical_cols:
    unique_count = df[col].nunique()
    most_frequent = df[col].value_counts().nlargest(1)
    print(f"Column: {col}")
    print(f"Number of unique values: {unique_count}")
    print(f"Most frequent value and count:\n{most_frequent}\n")

avg_msrp_by_make = df.groupby('Make')['MSRP'].mean().sort_values(ascending=False)
print("Average MSRP by Make:\n")
print(avg_msrp_by_make)

numerical_cols = ['Year', 'Engine HP', 'Engine Cylinders', 'Number of Doors', 'highway MPG', 'city mpg', 'Popularity', 'MSRP']
correlation_matrix = df[numerical_cols].corr()
print("\nCorrelation Matrix of Numerical Columns:\n")
print(correlation_matrix)

"""## Data visualization

### Subtask:
Create visualizations to help understand the data distributions and relationships between variables.

**Reasoning**:
Generate histograms for numerical columns to visualize their distributions and bar plots for categorical columns to show the frequency of each category.
"""

import matplotlib.pyplot as plt
import seaborn as sns

numerical_cols = ['Year', 'Engine HP', 'Engine Cylinders', 'Number of Doors', 'highway MPG', 'city mpg', 'Popularity', 'MSRP']
categorical_cols = ['Engine Fuel Type', 'Transmission Type', 'Driven_Wheels', 'Vehicle Size', 'Vehicle Style']

# Histograms for numerical columns
df[numerical_cols].hist(figsize=(15, 10))
plt.tight_layout()
plt.suptitle("Histograms of Numerical Columns", y=1.02)
plt.show()

# Bar plots for selected categorical columns (limiting to top 10 for readability)
for col in categorical_cols:
    plt.figure(figsize=(10, 6))
    df[col].value_counts().nlargest(10).plot(kind='bar')
    plt.title(f"Frequency of Top 10 {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

"""**Reasoning**:
Create scatter plots to explore relationships between key numerical variables and generate a heatmap of the correlation matrix to visualize relationships between numerical variables.


"""

# Scatter plots for relationships between numerical variables
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Engine HP', y='MSRP')
plt.title('Engine HP vs MSRP')
plt.xlabel('Engine HP')
plt.ylabel('MSRP')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='highway MPG', y='city mpg')
plt.title('Highway MPG vs City MPG')
plt.xlabel('Highway MPG')
plt.ylabel('City MPG')
plt.show()

# Heatmap of the correlation matrix
numerical_cols = ['Year', 'Engine HP', 'Engine Cylinders', 'Number of Doors', 'highway MPG', 'city mpg', 'Popularity', 'MSRP']
correlation_matrix = df[numerical_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Columns')
plt.show()

"""## Summary:

### Data Analysis Key Findings

*   The dataset contains 11914 rows and 16 columns.
*   Columns such as 'Engine Fuel Type', 'Engine HP', 'Engine Cylinders', 'Number of Doors', and 'Market Category' have missing values.
*   The dataset includes 8 object type columns, 5 integer type columns, and 3 float type columns.
*   'Make' has 48 unique values, with 'Chevrolet' being the most frequent.
*   'Transmission Type' has 5 unique values, with 'AUTOMATIC' being the most frequent.
*   The average MSRP varies significantly by make, with luxury brands like Bugatti, Maybach, and Rolls-Royce having the highest averages.
*   There is a strong positive correlation (0.91) between 'Engine HP' and 'Engine Cylinders'.
*   There is a moderate positive correlation (0.66) between 'Engine HP' and 'MSRP'.
*   There are negative correlations between MPG values ('highway MPG' and 'city mpg') and 'Engine HP' and 'Engine Cylinders'.

### Insights or Next Steps

*   Address missing values in relevant columns before further analysis or modeling.
*   Explore the relationships between categorical variables and numerical variables like MSRP using appropriate visualizations or statistical tests.

"""
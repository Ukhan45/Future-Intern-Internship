import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

def visualize_dataframe(df, numeric_columns, categorical_column=None, title_prefix=""):
    sns.set(style="whitegrid")
    
    plt.figure(figsize=(12, 10))
    for i, column in enumerate(numeric_columns, 1):
        plt.subplot(2, 2, i)
        sns.histplot(df[column], kde=True, bins=20, color='skyblue')
        plt.title(f'{title_prefix} Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    if categorical_column:
        plt.figure(figsize=(8, 6))
        sns.countplot(data=df, x=categorical_column, palette="pastel")
        plt.title(f'{title_prefix} Count of {categorical_column}')
        plt.xlabel(categorical_column)
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

iris_df = pd.read_csv("Iris.csv")
iris_numeric = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
visualize_dataframe(iris_df, iris_numeric, categorical_column='Species', title_prefix="Iris -")

conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
table_name = tables[0][0]

db_df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
conn.close()

numeric_cols = db_df.select_dtypes(include='number').columns.tolist()
categorical_cols = db_df.select_dtypes(include='object').columns.tolist()
cat_col = categorical_cols[0] if categorical_cols else None

visualize_dataframe(db_df, numeric_cols[:4], categorical_column=cat_col, title_prefix=f"{table_name} -")

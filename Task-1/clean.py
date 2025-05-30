import os
import zipfile
import pandas as pd

zip_path = "titanic.zip"
extract_path = "extracted/"
output_path = "cleaned/"
os.makedirs(output_path, exist_ok=True)

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

def report_missing_values(df, filename):
    print(f"\n Missing Value Report for: {filename}")
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100
    report = pd.DataFrame({
        'Missing Values': missing_count,
        'Percent (%)': missing_percent.round(2)
    })
    print(report[report['Missing Values'] > 0])

def clean_dataframe(df):
    
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    categorical_cols = df.select_dtypes(include='object').columns
    for col in categorical_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower) & (df[col] <= upper)]

    return df

csv_files = ["train.csv", "test.csv", "gender_submission.csv"]

for file in csv_files:
    file_path = os.path.join(extract_path, file)
    df = pd.read_csv(file_path)

    print(f"\n Cleaning {file}... Original shape: {df.shape}")
    report_missing_values(df, file)

    cleaned_df = clean_dataframe(df)
    print(f"Cleaned shape: {cleaned_df.shape}")

    cleaned_file_path = os.path.join(output_path, file.replace('.csv', '_cleaned.csv'))
    cleaned_df.to_csv(cleaned_file_path, index=False)
    print(f"Saved: {cleaned_file_path}")

# Call the function to import and export CSV files
# Clean_Data.py
import pandas as pd
import os

def import_and_export_csv(input_folder, temp_folder):
    # Import train.csv into a DataFrame
    train_file = os.path.join(input_folder, 'training.csv')
    train_df = pd.read_csv(train_file)

    # Import test.csv into a DataFrame
    test_file = os.path.join(input_folder, 'test.csv')
    test_df = pd.read_csv(test_file)

    # Convert all columns to lower case
    train_df.columns = train_df.columns.str.lower()
    test_df.columns = test_df.columns.str.lower()

    # Export the modified DataFrames as train.csv and test.csv in the temp folder
    train_export_file = os.path.join(temp_folder, 'train.csv')
    test_export_file = os.path.join(temp_folder, 'test.csv')
    
    train_df.to_csv(train_export_file, index=False)
    test_df.to_csv(test_export_file, index=False)
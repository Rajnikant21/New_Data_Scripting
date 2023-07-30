from Clean_Data import import_and_export_csv

def main():
    # Define input and temp folders
    input_folder = 'input'
    temp_folder = 'temp'

    # Call the function to import and export CSV files
    import_and_export_csv(input_folder, temp_folder)

if __name__ == "__main__":
    main()

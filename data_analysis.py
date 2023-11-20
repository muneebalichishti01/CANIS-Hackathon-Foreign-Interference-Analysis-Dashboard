'''
Module imports:
1. pandas: for data manipulation and analysis
'''

# Importing the required modules
import pandas as pd
import main

# Loading the data from the Excel file
def load():
    '''
    The data is loaded from the Excel file using pandas library.
    return: data
    '''
    data = pd.read_excel("CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx")
    return data

    
# Show the basic structure of data for testing purposes
def structure(data):
    '''
    The structure of the data is shown using built-in pandas library commands.
    return: None
    '''
    print("-" * 40)
    
    # First few rows
    print("First 4 rows:")
    print(data.head(4))
    
    # Last few rows
    print("\nLast 4 rows:")
    print(data.tail(4))
    
    # Shape of the data
    print("\nDataset Information:")
    print(data.info())
    
    # Statistical Summary
    print("\nStatistical Summary:")
    print(data.describe().round())
    
    # Data Types
    print("\nData Types:")
    print(data.dtypes)
    
    # Missing Values
    print("\nMissing Values:")
    print(data.isnull().sum())
    
    # Unique Values in each column
    print("\nUnique Values:")
    for col in data.columns:
        print(f"{col}: {data[col].nunique()}")
    
    print("-" * 40)

# Calling the main function
if __name__ == "__main__":
    main.main()

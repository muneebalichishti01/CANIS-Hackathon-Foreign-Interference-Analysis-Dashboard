'''
Module imports:
1. pandas: for data manipulation and analysis
'''

# Importing the required modules
import pandas as pd
import io
import os

# Loading the data from the Excel file
def load():
    '''
    The data is loaded from the Excel file using pandas library.
    return: data
    '''
    data = pd.read_excel("CANIS_PRC_state_media_on_social_media_platforms-2023-11-03.xlsx")
    return data

    
# Show the basic structure of data on terminal
def structure_to_terminal(data):
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

# Save the basic structure of data to a text file
def structure_to_file(data, count):
    """
    The structure of the data is analyzed and the results are saved to a text file.
    return: none
    """
    
    folder_path = 'AnalysisOutputs/'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_name = 'data_structure_report_' + str(count) + '.txt'
    new_path = folder_path + file_name
    
    with open(new_path, 'w', encoding='utf-8-sig') as file:
        file.write("-" * 40 + "\n")
        
        # First few rows
        file.write("First 4 rows:\n")
        file.write(data.head(4).to_string() + "\n\n")
        
        # Last few rows
        file.write("Last 4 rows:\n")
        file.write(data.tail(4).to_string() + "\n\n")
        
        # Shape of the data
        file.write("Dataset Information:\n")
        buffer = io.StringIO()
        data.info(buf=buffer)
        file.write(buffer.getvalue() + "\n")
        
        # Statistical Summary
        file.write("Statistical Summary:\n")
        file.write(data.describe().round().to_string() + "\n\n")
        
        # Data Types
        file.write("Data Types:\n")
        file.write(data.dtypes.to_string() + "\n\n")
        
        # Missing Values
        file.write("Missing Values:\n")
        file.write(data.isnull().sum().to_string() + "\n\n")
        
        # Unique Values in each column
        file.write("Unique Values in each column:\n")
        for col in data.columns:
            file.write(f"{col}: {data[col].nunique()}\n")
        
        file.write("-" * 40 + "\n")

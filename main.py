'''
Module/File imports:
1. data_analysis: for data structure analysis
2. data_cleaning: for data cleaning
3. data_modeling: for data modeling
'''

# Importing the required modules
import data_analysis as analysis
import data_cleaning as cleaning
import data_modeling as modeling


# Main function to call all the other functions and run the program
def main():
    '''
    The main function is called to run the program.
    return: None
    '''
    orig_data = analysis.load()                         # Loading the data
    analysis.structure_to_file(orig_data, 1)            # Saving the basic structure of data before cleaning

    cleaned_data = cleaning.clean(orig_data)            # Cleaning the data
    analysis.structure_to_file(cleaned_data, 2)         # Saving the basic structure of data after cleaning

    modelized_data = modeling.model(cleaned_data)       # Modeling the data
    analysis.structure_to_file(modelized_data, 3)       # Saving the new structure of data after modeling
    
    
# Calling the main function
if __name__ == "__main__":
    main()

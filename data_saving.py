'''
Module/File imports:
1. os: for creating folders
'''

# Importing the required modules
import os


# Save the test data to a csv file
def save_test(data):
    '''
    The data is saved to a corresponding csv file.
    return: data
    '''
    folder_path = 'TestOutputs/'
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    for i in range(1, 5):
        file_name = 'test_' + str(i) + '.csv'
        new_path = folder_path + file_name
        data.to_csv(new_path, index=False, encoding='utf-8-sig')
    return data

# Save the model data to a csv file
def save_model(data):
    '''
    The data is saved to a corresponding csv file.
    return: data
    '''
    folder_path = 'ModelOutputs/'
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    for i in range(1, 4):
        file_name = 'model_' + str(i) + '.csv'
        new_path = folder_path + file_name
        data.to_csv(new_path, index=False, encoding='utf-8-sig')
    return data
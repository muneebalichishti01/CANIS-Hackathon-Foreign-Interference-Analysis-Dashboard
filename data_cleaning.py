'''
Module/File imports:
1. data_saving: for saving the data to a csv file
'''
 
# Importing the required modules
import data_saving as saving

   
# Test 1 - Drop the columns with 'Chinese' in their names
def test1(data):
    '''
    Test 1 - The data is cleaned by dropping the columns that are NOT required for the analysis
    return: data
    '''
    # drop_chinese = [col for col in data.columns if 'Chinese' in col]
    drop_url = [col for col in data.columns if 'URL' in col]
    # data.drop(columns=drop_chinese, inplace=True)    # Drop columns with 'Chinese'
    data.drop(columns=drop_url, inplace=True)        # Drop columns with 'URL'
    
    return saving.save_test(data)                         # Save the data to a csv file


# Test 2 - Convert followers to integers & fill the missing values with 'Unknown'
def test2(data):
    '''
    Test 2 - The data is cleaned by converting followers to integers & filling the missing values with 'Unknown'
    return: data
    '''
    follower_cols = ['X (Twitter) Follower #', 'Facebook Follower #', 'Instagram Follower #', 'Threads Follower #', 'YouTube Subscriber #', 'TikTok Subscriber #']
    for col in follower_cols:
        data[col] = data[col].fillna(0).astype(int)     # Converting all follower counts to integers from int64
    for col in data.columns:
        data[col].fillna('Unknown', inplace=True)       # Replacing NaN in each column
    
    return saving.save_test(data)                         # Save the data to a csv file



# Test 3 - Rename the columns to make them more readable/understandable
def test3(data):
    '''
    Test 3 - The data is cleaned by renaming the columns to make them more readable/understandable
    return: data
    '''
    data.rename(columns={
    'Name (English)': 'Name EN',
    'Name (Chinese)': 'Name CN',
    'Region of Focus': 'Focus Region',
    'Entity owner (English)': 'Entity Owner EN',
    'Entity owner (Chinese)': 'Entity Owner CN',
    'Parent entity (English)': 'Parent Entity EN',
    'Parent entity (Chinese)': 'Parent Entity CN',
    
    'X (Twitter) handle': 'X (Twitter) Handle',
    'X (Twitter) Follower #': 'X (Twitter) Followers',
    'Facebook page': 'Facebook Handle',
    'Facebook Follower #': 'Facebook Followers',
    'Instragram page': 'Instagram Handle',
    'Instagram Follower #': 'Instagram Followers',
    'Threads account': 'Threads Handle',
    'Threads Follower #': 'Threads Followers',
    'YouTube account': 'YouTube Handle',
    'YouTube Subscriber #': 'YouTube Followers',
    'TikTok account': 'TikTok Handle',
    'TikTok Subscriber #': 'TikTok Followers',
    }, inplace=True)
    
    return saving.save_test(data)                         # Save the data to a csv file


# Test 4 - Identify actors with both English and Chinese names
def test4(data):
    '''
    Test 4 - The data is cleaned by identifying actors with both English and Chinese names
    return: overlap_actors
    '''
    # overlap_actors = data[(data['Name EN'].notnull()) & (data['Name CN'] != 'Unknown')]

    return saving.save_test(data)                         # Save the data to a csv file


# Clean the data by calling the required functions
def clean(data):
    '''
    The data is cleaned by calling the required functions.
    return: cleaned_data
    '''
    test_data_1 = test1(data)                    # Test 1
    test_data_2 = test2(test_data_1)             # Test 2
    test_data_3 = test3(test_data_2)             # Test 3
    cleaned_data = test4(test_data_3)            # Test 4
    
    print("-" * 40)
    print("\nSuccessfully cleaned the data!\n")
    print("-" * 40)
    return cleaned_data


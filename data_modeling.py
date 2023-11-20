'''
Module/File imports:
1. pandas: for data manipulation and analysis
2. data_saving: for saving the data to a csv file
'''

# Importing the required modules
import pandas as pd
import data_saving as saving

# Model 1 - Create a new column for total social media presence
def model1(data):
    '''
    Model 1 - The data is modelled to create a new column for total social media presence
    return: data
    '''
    def has_presence(row, handles, followers):
        presence_count = 0
        for handle, followers in zip(handles, followers):
            if pd.notna(row[handle]) and row[followers] > 0:
                presence_count += 1
        return presence_count
    
    handles = ['X (Twitter) Handle', 'Facebook Handle', 'Instagram Handle', 'Threads Handle', 'YouTube Handle', 'TikTok Handle']
    followers = ['X (Twitter) Followers', 'Facebook Followers', 'Instagram Followers', 'Threads Followers', 'YouTube Followers', 'TikTok Followers']
    data['Total Social Media Presence'] = data.apply(lambda row: has_presence(row, handles, followers), axis=1)
    data['Platform Presence Category'] = pd.cut(data['Total Social Media Presence'], bins=[0, 1, 3, 6], labels=['Low', 'Medium', 'High'], include_lowest=True)

    return saving.save_model(data)                         # Save the data to a csv file

    

# Model 2 - Create a new column for total followers & dominance
def model2(data):
    '''
    Test 5 - The data is modelled to create a new column for total followers & dominance
    return: data
    '''
    data['Total Followers'] = data[['X (Twitter) Followers', 'Facebook Followers', 'Instagram Followers', 'Threads Followers', 'YouTube Followers', 'TikTok Followers']].sum(axis=1)
    def calculate_dominance(row, platform_followers):
        if row['Total Followers'] > 0:
            return (row[platform_followers] / row['Total Followers']) * 100
        else:
            return 0
    
    data['Twitter Dominance'] = data.apply(lambda row: calculate_dominance(row, 'X (Twitter) Followers'), axis=1).round(1)
    data['Facebook Dominance'] = data.apply(lambda row: calculate_dominance(row, 'Facebook Followers'), axis=1).round(1)
    data['Instagram Dominance'] = data.apply(lambda row: calculate_dominance(row, 'Instagram Followers'), axis=1).round(1)
    data['Threads Dominance'] = data.apply(lambda row: calculate_dominance(row, 'Threads Followers'), axis=1).round(1)
    data['YouTube Dominance'] = data.apply(lambda row: calculate_dominance(row, 'YouTube Followers'), axis=1).round(1)
    data['TikTok Dominance'] = data.apply(lambda row: calculate_dominance(row, 'TikTok Followers'), axis=1).round(1)

    return saving.save_model(data)                         # Save the data to a csv file



# Model 3 - Identify outliers in key columns
def model3(data):
    """
    Model 3 - The data is modelled to identify outliers in key columns
    return: data
    """
    columns_to_check = ['X (Twitter) Followers', 'Facebook Followers', 'Instagram Followers', 'YouTube Followers', 'TikTok Followers', 'Threads Followers']
    data['IQR based Outlier'] = False
    
    for col in columns_to_check:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        data['IQR based Outlier'] = data['IQR based Outlier'] | ~data[col].between(lower_bound, upper_bound)

    return saving.save_model(data)                         # Save the data to a csv file



# Model the data by calling the required functions
def model(data):
    '''
    The data is cleaned by calling the required functions.
    return: cleaned_data
    '''
    model_data_1 = model1(data)                       # Model 1
    model_data_2 = model2(model_data_1)               # Model 2
    modelled_data = model3(model_data_2)              # Model 3
    
    print("-" * 40)
    print("\nSuccessfully modelled the data!\n")
    print("-" * 40)
    return modelled_data


## prepare and clean my data
import acquire
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split



def prep_telco_data(df):
    '''
    This function prepares and cleans the telco dataframe imported from sql.
    '''
#     df = acquire.get_new_telco_churn_data()

    # get rid of duplicate columns from the sql join
    df = df.loc[:, ~df.columns.duplicated()]

    # this is to adress the blank in total_charges. Here we replace the blank with a nan, and then drop our nulls
    df = df.replace(' ', np.nan)
    df.dropna(inplace=True)
    # change our total_charges from a string to a float
    df.total_charges = df.total_charges.astype('float')
    
    # drop the columns that do not appear to have any association to churn
    df = df.drop(columns=['streaming_movies', 'streaming_tv', 'multiple_lines', 'gender',
                         'contract_type_id', 'internet_service_type_id', 'payment_type_id'])
    
    # rename my tenure column
    df = df.rename(columns={'tenure': 'tenure_in_months'})

    # this change all of my yes and no columns to binary columns
    columns = ['partner', 'dependents', 'phone_service', 'online_security', 'online_backup', 
               'device_protection', 'tech_support', 'paperless_billing', 'churn']

    for cols in columns:
        df[cols] = np.where(df[cols] == 'Yes', 1, 0)

    return df



def create_dummies(df):
    '''
    This function is used to create dummy columns for my non binary columns
    '''
    
    # create dummies for payment_type, internet_service_type, and contract_type
    payment_dummies = pd.get_dummies(df.payment_type, drop_first=True)
    internet_dummies = pd.get_dummies(df.internet_service_type, drop_first=False)
    contract_dummies = pd.get_dummies(df.contract_type, drop_first=True)
    
    # now we concatenate our dummy dataframes with the original
    df = pd.concat([df, payment_dummies, internet_dummies, contract_dummies], axis=1)
    
    # now I am dropping all my original string columns that I made dummies with and dropping 
    #the type_id columns since they are duplicates of the string column
    df = df.drop(columns=['None', 'payment_type', 'contract_type', 'internet_service_type'])
    
    return df


def telco_split(df):
    '''
    This function takes in a dataframe and splits it into train, test, and validate dataframes for my model
    '''

    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123)
    return train, validate, test
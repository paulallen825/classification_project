import acquire
import prepare

import pandas as pd
import numpy as np



columns = ['payment_type', 'gender', 'senior_citizen', 'partner', 'dependents', 'phone_service', 'multiple_lines', 
           'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies',
           'paperless_billing', 'churn', 'internet_service_type', 'contract_type']
def value_counts(df):
    for col in columns:
        print(col)
        print(df[col].value_counts())
        print('-------------')
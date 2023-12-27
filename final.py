import pandas as pd 
import numpy as np 
import random
 
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


def one_hot_display(our_dict, value):
    new_dict = our_dict.copy()
    for k, v in new_dict.items():
        if k == value:
            new_dict[k].append(1)
        else:
            new_dict[k].append(0)
    return new_dict
    


def generate_dataFrame(our_dict, columns, cur_df):
    new_dict_for_frame = {**our_dict}
    for i in columns:
        for i, row in enumerate(cur_df[i]):
           new_dict_for_frame = one_hot_display(new_dict_for_frame, row) 

    return pd.DataFrame(new_dict_for_frame)

def generate_dict(keys_array):
    dict_for_df = { key: [] for key in keys_array}
    return dict_for_df

def custom_get_dummies(df):
    df_columns = df.columns
    unique_values = []
    for column in df_columns:
       unique_values = [*unique_values, *df[column].unique()]

    dict_for_frame = generate_dict(unique_values)

    return generate_dataFrame(dict_for_frame, df_columns, df)
    

one_hot_data = custom_get_dummies(data)

print(data)
print('-------')
print(one_hot_data)

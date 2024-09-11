import pandas as pd

df = pd.read_csv('mock_data.csv')

data_dictionary = pd.DataFrame(df.dtypes, columns=['data_type'])

isnull_list = []
count_list = []
max_list = []
min_list = []
median_list = []

for column in df.columns:
    isnull_count = df[column].isnull().sum()
    count = df[column].count()

    isnull_list.append(isnull_count)
    count_list.append(count)

    max_value, min_value, median_value = None, None, None

    if pd.api.types.is_numeric_dtype(df[column]):
        max_value = df[column].max()
        min_value = df[column].min()
        median_value = df[column].median()

        if isinstance(max_value, float):
            max_value = round(max_value, 2)
        if isinstance(min_value, float):
            min_value = round(min_value, 2)
        if isinstance(median_value, float):
            median_value = round(median_value, 2)

    max_list.append(max_value)
    min_list.append(min_value)
    median_list.append(median_value)

data_dictionary['notnull_aantal'] = count_list
data_dictionary['null_aantal'] = isnull_list
data_dictionary['maximum'] = max_list
data_dictionary['minimum'] = min_list
data_dictionary['mediaan'] = median_list

data_dictionary.to_csv('data_dictionary.csv', sep=',')

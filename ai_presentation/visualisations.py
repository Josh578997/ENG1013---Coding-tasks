import pandas as pd

data = pd.read_csv('ai_presentation.data.csv')
print(f'{data.info()} \n{data.describe()}\n{data.head}\n{data.isnull().sum()}')


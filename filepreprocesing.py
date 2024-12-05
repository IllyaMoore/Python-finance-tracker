
import pandas as pd 
  
# read contents of csv file 
file_path = 'TransactionTracker/income.csv'
try:
    file = pd.read_csv(file_path)
except pd.errors.EmptyDataError:
    print(f"Файл {file_path} порожній!")
    file = pd.DataFrame(columns=['idnum', 'amount', 'date', 'category', 'description', 'account_id'])

  
# adding header 
headerList = ['idnum', 'amount', 'date', 'category', 'description', 'account_id'] 
  
# converting data frame to csv 
file.to_csv(file_path, header=headerList, index=False) 
  
# display modified csv file 
file2 = pd.read_csv(file_path) 
print('\nModified file:') 
print(file2)  
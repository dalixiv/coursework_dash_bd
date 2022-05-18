from glob import glob
import pandas as pd
import re
import sqlite3 
from tqdm.notebook import tqdm


data_path = '../report data/'
db_path = './'


list_of_pathes = glob(f'{data_path}*.xlsx')
list_of_pathes += glob(f'{data_path}*.csv')
list_of_pathes.remove(f'{data_path}Publication Word Cloud - Development.xlsx')
list_of_pathes.remove(f'{data_path}Publication Word Cloud - Development.csv')
list_of_pathes.remove(f'{data_path}ikt.xlsx')


con = sqlite3.connect(f'{db_path}data.db')


for path in list_of_pathes:
    name, ext = path[2:].split('.')
    if ext == 'xlsx':
      df = pd.read_excel(path)
    elif ext == 'csv':
      df = pd.read_csv(path)
    else:
      continue

    name = re.sub(r'[^\w\s]','',name)
    name = ''.join(name.split(' '))

    df.to_sql(name, con=con, if_exists='replace', index=False)

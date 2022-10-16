import pandas as pd

read_file=pd.read_excel(r'inventory_lab1a1b.xlsx')
read_file.to_csv(r'inventory_lab1a1b.csv', index=None,header=True)
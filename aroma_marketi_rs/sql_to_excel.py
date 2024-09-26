from db_config import DbConfig
import pandas as pd

obj = DbConfig()

qr = f'SELECT * FROM {obj.data_with_duplicates_table}'
obj.cur.execute(qr)
results = obj.cur.fetchall()

df = pd.read_sql(qr, obj.con)
excel_file_path = 'aroma_marketi_rs.xlsx'
df.to_excel(excel_file_path, index=False)
print("Data exported to Excel file successfully.")

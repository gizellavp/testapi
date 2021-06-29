import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("testapi.json", scope)

gc = gspread.authorize(creds)

wk = gc.open("Data").sheet1

data = wk.get_all_records() 

df = pd.DataFrame(data)
#df[['Timestamp', 'Nama', 'Email', 'Usia', 'Jenis Kelamin', 'Tempat Lahir', 'Tanggal Lahir']]
print(df[['Nama', 'Usia', 'Jenis Kelamin']])

#print(df['Nama'])

from oauth2client.service_account import ServiceAccountCredentials
import gspread

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("......json", scopes) #access the json key you downloaded earlier
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
workbook = file.open("DGT_Sheet") #open sheet
sheet = workbook.sheet1


def Sheet(email,nom,prenom,niveau,numero) :
    sheet.append_row([email,nom,prenom,niveau,numero])
    sheet.update_acell('G4', str(int(sheet.acell('G4').value) + 1))

def Numero() :
    return int(sheet.acell('G4').value)




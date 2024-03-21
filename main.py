from Sheet import Sheet
from Send_Mail import Send_Mail
from QR_Code import QR_Code



def main(email,nom,prenom,niveau,numero):
    if ("@" in email):
        QR_Code(nom, prenom)
        Sheet(email,nom,prenom,niveau,numero)
        Send_Mail(email,nom,prenom)




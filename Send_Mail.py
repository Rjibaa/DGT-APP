import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def Send_Mail(receiver_email,nom,prenom):

    subject = "VOTRE TICKET DGT "
    sender_email = "......@gmail.com"
    password =".........."
    message = MIMEMultipart()
    message["From"] = sender_email
    message["Subject"] = subject



    Main_Message="Cher(e) amoureux(se) du DGT ,\n" \
                  "Bienvenue à la 10ème édition du fameux Doctor's Got Talent ! Ce mail représente votre ticket d'accès "+\
                 "à la grande finale.""Ci-joint vous trouverez l'innovation de cette édition : le ticket numérique , comportant un QR "+\
                 "code. Ce code sera votre identifiant personnel et privé," +"et sera scanné à l'entrée .Ce ticket est nominatif, et n'est donc pas échangeable avec une autre personne."+"Le jour J, les portes ouvriront à 13h30 et fermeront à 14h, veillez donc à être bien à l'heure."+"Nous comptons sur vous pour passer un après-midi exceptionnel, dans le cadre du respect mutuel et de la bonne ambiance."+"Au plaisir de vous retrouver, le 21/02/2023, à la cité de la culture.\n"\
                "Promo Spéciale : Présentez ce ticket numérique à la boutique JRIBI OPTIC Tunis et bénéficiez de 30% de réduction sur toute la boutique, avec la facilité du paiement ! retrouvez leur collection sur \n"\
                "facebook : \n"\
                "https://www.facebook.com/jribi.imtithel \n" \
                "et sur instagram: \n"\
                "https://www.instagram.com/jribi_optic_tunis/"
    # Create a multipart message and set headers
    message["To"] = receiver_email
    message["Bcc"] = receiver_email  # Recommended for mass emails
    file = "Tickets\{}{}.jpeg".format(nom,prenom)
    filename="{}{}.jpeg".format(nom,prenom)
    file1="promo-min.jpg"

    # Add body to email
    message.attach(MIMEText(Main_Message, "plain"))

    # Open PDF file in binary mode
    with open(file, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    with open(file1, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part1 = MIMEBase("application", "octet-stream")
        part1.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)
    encoders.encode_base64(part1)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    part1.add_header(
        "Content-Disposition",
        f"attachment; filename= {file1}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    message.attach(part1)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


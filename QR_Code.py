import qrcode
from PIL import Image, ImageDraw, ImageFont
from Sheet import Numero



def QR_Code(nom,prenom):
    image = Image.open('LA FINALE ticket.png')
    # numero=Numero()
    numero=272
    qr = qrcode.QRCode(box_size=13)
    # Data to be encoded
    data = nom + prenom
    qr.add_data(data)
    qr.make()
    code=qr.make_image()
    code_sized = code.resize((410, 405))
    pos=(1560,65)
    image.paste(code_sized, pos)
    title_font = ImageFont.truetype('ARIAL.ttf', 50)
    image_editable = ImageDraw.Draw(image)
    image_editable.text((1700, 10), "QR-{}".format(numero), (168, 168, 168), font=title_font)
    rgb_im = image.convert('RGB')
    rgb_im.save(r'Tickets\\{}.jpeg'.format(data),optimize=True)

QR_Code("Hanneshi","oussema")

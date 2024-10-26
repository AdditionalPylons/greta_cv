import qrcode
from PIL import Image

qr = qrcode.QRCode(box_size=5)
qr.add_data("www.bytesitesolutions.com")
qr.make(fit=True)
img = qr.make_image(fill_color='white', back_color='black')
img.show()
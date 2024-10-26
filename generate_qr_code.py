import qrcode
from PIL import Image

qr = qrcode.QRCode(box_size=5)
qr.add_data("https://github.com/AdditionalPylons/greta_cv/blob/main/Greta%20Leroux%20Biomagnetismo.pdf?raw=true")
qr.make(fit=True)
img = qr.make_image(fill_color='white', back_color='black')
img.show()
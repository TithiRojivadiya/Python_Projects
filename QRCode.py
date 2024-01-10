# method 1::::::::::::::::
# import qrcode
# import PIL
#
# img = qrcode.make("https://www.hackerrank.com/dashboard")
#
# img.save("HakerRank.png")

import qrcode
import PIL

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=8)
qr.add_data("https://www.hackerrank.com/dashboard")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("New.png")

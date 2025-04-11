import qrcode as qr
i=qr.make("name")  #simple code for creating qr
i.save("name.png")

# advance code for creating qrcode

from PIL import Image  # formatting the qrcode we use pil

q=qr.QRCode(version=1,                                         #for handling error ,body,format
            error_correction=qr.constants.ERROR_CORRECT_H,
            box_size=15,
            border=2,
            )
q.add_data("hello")
q.make(fit=True)
img=q.make_image(fill_color="#ff55aa",back_color="#ffff11")
img.save("new1.png")
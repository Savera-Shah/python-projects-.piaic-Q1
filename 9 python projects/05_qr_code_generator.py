import qrcode
import qrcode.constants
from PIL import Image

qr =qrcode.QRCode(
    version= 1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 5
    
)
link_data="https://www.youtube.com/@BroCodez"
qr.add_data(link_data)
qr.make(fit=True)
image=qr.make_image(fill_color= "green" , back_color= "white")
image.save("qrcode.png")
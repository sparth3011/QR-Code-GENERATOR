import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('qr_code.png')
    return img

def scan_qr_code(image_path):
    with open(image_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.show()

    result = decode(Image.open(image_path))
    if result:
        return result[0].data.decode('utf-8')
    else:
        return "No QR code found in the image"

data = "http://parthagroworld.com/contact/index.html"
img = generate_qr_code(data)
scanned_data = scan_qr_code('qr_code.png')

print(f"Generated QR code with data: {data}")
print(f"Scanned QR code data: {scanned_data}")
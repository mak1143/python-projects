import qrcode

url = input("Enter the url: ").strip()
filePath = "/home/shoyo/Development/PYTHON-INV/NEW-PYTHON-DIR-PROJECTS/qrcode-folder/qrcode.png"
qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(filePath)
print(f"QR was succefully generated!")

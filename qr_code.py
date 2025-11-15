import qrcode

url = input("ENTER THE URL : ").strip()
file_path = "C:\\Users\\VARASHREE H A\\OneDrive\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR CODE WAS GENERATED!")
import qrcode

img=qrcode.make("https://www.youtube.com/")
img.save("youtubeQR.jpg")

# Another way to generate QRCode
qr=qrcode.QRCode(
    version=1,
    box_size=15,
    border=5
)
data="https://www.youtube.com/hybelabels"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color='white')
img.save("YoutubechannelQR.jpg")

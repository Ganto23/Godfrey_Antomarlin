import qrcode

def make_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,      
    )
    
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrimg.png")
    
if __name__ == "__main__":
    url = input("Enter a valid url: ")
    make_qrcode(url)
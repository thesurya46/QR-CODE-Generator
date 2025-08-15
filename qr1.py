import qrcode as qr 
img=qr.make("https://www.linkedin.com/in/suryasnata-panigrahi")
img.save("LINKEDIN_QR.png")
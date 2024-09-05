import pyqrcode 
import png 
from pyqrcode import QRCode 
  
url = "upi://pay?pa=7470948583@ptsbi&pn=Ayush%20%20Balyan&mc=0000&mode=02&purpose=00&orgid=159761&cust=1513294794"
# String which represents the QR code 
amount = input("Enter Amount: ")
url = url + "&am=" + str(amount) + ".00&cu=INR"
# Generate QR code 

print(url)

qr = pyqrcode.create(url) 
  
# Create and save the svg file namideng "myqr.svg" 
qr.svg("myqr.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png" 
qr.png('myqr.png', scale = 6) 
print("Completed")

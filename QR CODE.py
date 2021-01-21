# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
site = "https://github.com/elmike2113"
  
# Generate QR code 
url_qr = pyqrcode.create(site) 
  
# Create and save the svg file naming "myqr.svg" 
url_qr.svg("GitHub profile.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png" 
url_qr.png('GitHub profile.png', scale = 6) 
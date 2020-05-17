# This python module for creating qr code 
# first you have to install py2png and pyqrcode using pip
# After that run this lines of code
import pyqrcode
# replace Name with your name
x ="Name"
qr=pyqrcode.create(x)
qr.png("Name.png",scale=6)

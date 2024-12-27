import http.server
import socket
import socketserver
import os
import webbrowser
import qrcode

# Assigning the appropriate port value
PORT = 8010

# Change directory to access the files on the desktop (ensure the directory is correct for your setup)
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive')
os.chdir(desktop)

# Create an HTTP request Handler
Handler = http.server.SimpleHTTPRequestHandler

# Find the host name of the system
hostname = socket.gethostname()

# Find the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

# Convert the IP address into a QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(link)
qr.make(fit=True)

# Generate QR code image as PNG
img = qr.make_image(fill='black', back_color='white')

# Save the QR code as a PNG file
img.save("myqr.png")

# Open the QR code image in the web browser (ensure it's in a browser-supported format, e.g., PNG)
webbrowser.open('myqr.png')

# Create the HTTP server and serve the folder at PORT 8010
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    print("Type this in your browser:", IP)
    print("Or use the QRCode to access it.")
    httpd.serve_forever()

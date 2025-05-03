# import necessary modules

# for implementing the HTTP Web servers
import http.server

# provides access to the BSD socket interface
import socket

# a framework for network servers
import socketserver

# to display a Web-based documents to users
import webbrowser

# to generate qrcode
import pyqrcode
from pyqrcode import QRCode

# to access operating system control
import os

import argparse
import logging

# --- Security Warning ---
print("WARNING: This server exposes files to anyone on your local network. Do not use on untrusted networks.")

# --- Argument Parsing ---
parser = argparse.ArgumentParser(description="Simple Python File Share with QR code.")
parser.add_argument('--dir', type=str, default=os.path.join(os.environ['USERPROFILE'], 'OneDrive'), help='Directory to share (default: OneDrive)')
parser.add_argument('--port', type=int, default=8010, help='Port to use (default: 8010)')
args = parser.parse_args()

# --- Logging Setup ---
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# --- Directory Change ---
try:
    os.chdir(args.dir)
    logging.info(f"Serving directory: {os.getcwd()}")
except Exception as e:
    logging.error(f"Failed to change directory: {e}")
    exit(1)

PORT = args.port

# --- HTTP Handler ---
Handler = http.server.SimpleHTTPRequestHandler

# --- IP Address Discovery ---
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
        link = IP
    finally:
        s.close()
except Exception as e:
    logging.error(f"Failed to determine local IP address: {e}")
    exit(1)

# --- QR Code Generation ---
try:
    url = pyqrcode.create(link)
    url.svg("myqr.svg", scale=8)
    webbrowser.open('myqr.svg')
    logging.info("QR code generated and opened in browser.")
except Exception as e:
    logging.error(f"Failed to generate or open QR code: {e}")

# --- Start HTTP Server ---
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        logging.info(f"Serving at {IP}")
        logging.info("Type this in your browser or use the QR code.")
        httpd.serve_forever()
except Exception as e:
    logging.error(f"Failed to start HTTP server: {e}")
    exit(1)

# --- Requirements Note ---
# Required packages: pyqrcode
# To install: pip install pyqrcode
# (If you want PNG QR codes: pip install pypng)

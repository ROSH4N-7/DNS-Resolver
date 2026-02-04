import socket
import ssl
import whois
import tkinter as tk
from tkinter import messagebox
#Storing resolved domain records
records= []

# Collected SSL certificate issued and expiry dates
def get_ssl_info(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                return cert.get('notBefore', 'N/A'), cert.get('notAfter', 'N/A')
    except:
        return "N/A", "N/A"
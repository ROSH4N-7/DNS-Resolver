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
# Resolve domain and collect all related information
def resolve_domain():
    domain =entry_domain.get().strip()

    if domain == "":
        messagebox.showerror("Error", "Domain name cannot be empty")
        return
        try:
        # DNS resolution (domain → IP)
        ip = socket.gethostbyname(domain)
         # Reverse DNS lookup (IP → domain)
        try:
            reverse_dns = socket.gethostbyaddr(ip)[0]
        except:
            reverse_dns = "Not Available"
         # WHOIS lookup (domain registration date)
        reg_date = "Not Available"
        try:
            w = whois.whois(domain)
            reg_date = w.creation_date
            if isinstance(reg_date, list):
                reg_date = reg_date[0]
            if reg_date is None:
                reg_date = "Not Available"
        except:
            reg_date = "WHOIS Lookup Failed"


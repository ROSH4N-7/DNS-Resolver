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
    domain = entry_domain.get().strip()

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

        # SSL certificate details
        issued, expires = get_ssl_info(domain)

        # Prepare output text
        output = (
            f"Domain: {domain}\n"
            f"IP Address: {ip}\n"
            f"Reverse DNS: {reverse_dns}\n"
            f"Registered On: {reg_date}\n"
            f"SSL Issued On: {issued}\n"
            f"SSL Expires On: {expires}"
        )
        # Display output (read-only)
        text_output.config(state=tk.NORMAL)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, output)
        text_output.config(state=tk.DISABLED)
        
         # Store history
        records.append([domain, ip])
        update_listbox()

    except socket.gaierror:
        messagebox.showerror("Error", "DNS resolution failed")
        
# Update history listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for r in records:
        listbox.insert(tk.END, f"{r[0]} → {r[1]}")

#GUI Setup
window = tk.Tk()
window.title("Advanced DNS Information Tool")
window.geometry("520x520")

tk.Label(window, text="Advanced DNS Resolver", font=("Arial", 16)).pack(pady=10)

tk.Label(window, text="Enter Domain Name:").pack()
entry_domain = tk.Entry(window, width=35)
entry_domain.pack(pady=5)

tk.Button(window, text="Get Domain Info", command=resolve_domain).pack(pady=10)

text_output = tk.Text(window, height=10, width=60, state=tk.DISABLED)
text_output.pack(pady=10)

tk.Label(window, text="Resolved History:").pack()
listbox = tk.Listbox(window, width=60)
listbox.pack(pady=5)

tk.Button(window, text="Exit", command=window.quit).pack(pady=10)

window.mainloop()



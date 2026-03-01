# DNS-Resolver
This my project for semester 1 for module: Introduction to programming


## 📋 Description

This is a **user-friendly GUI application** that lets you enter any domain name and instantly get detailed DNS information:

- IP Address
- Reverse DNS (IP → Domain)
- Domain registration date (WHOIS)
- SSL certificate issued & expiry dates

It also keeps a **live history** of every domain you have resolved.


## ✨ Features

- Clean and simple graphical interface (Tkinter)
- Real-time DNS resolution using `socket`
- Reverse DNS lookup
- WHOIS registration date
- SSL certificate details (issued & expiry)
- History list of all previous resolutions
- Proper error handling (empty input, invalid domain, etc.)
- Read-only output area to prevent accidental editing


## 🛠️ Technologies Used

- **Python 3**
- **Tkinter** – GUI
- **socket** – DNS & network functions
- **ssl** – SSL certificate information
- **whois** (python-whois) – Domain registration data
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


## 🚀 How to Run

### 1. Install the required library
```bash
pip install python-whois
```

### 2. Running the code
```bash
python code.py
```
## 📖 Usage

1. Type a domain name in the box (example: google.com, github.com, youtube.com)
2. Click Get Domain Info
3. Results appear below
4. All previous queries are saved in the Resolved History list


## Project Structure
DNS-Resolver/
├── README.md          ← This file
├── code.py            ← Main program (fully commented)


## 🎯 What I Learned

1) Using Python’s built-in networking libraries (socket, ssl)
2) Working with external packages (whois)
3) Building a complete GUI application with Tkinter
4) Input validation and exception handling
5) Version control with Git & GitHub
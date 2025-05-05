# Webcam Spyware Protection Application

<div align="center">

![GitHub](https://img.shields.io/github/license/hemanth-devzone/Webcam-Security-Tool)
![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-blue.svg)
![Status](https://img.shields.io/badge/status-completed-brightgreen.svg)

</div>

## 🔒 Project Overview

A robust Python-based desktop security application that provides hardware-level protection against unauthorized webcam access. The application implements a secure two-factor authentication system using email-based OTP verification before allowing any changes to webcam settings. By directly modifying Windows Registry entries, it ensures complete control over webcam hardware, offering protection beyond software-level security.



## ✨ Key Features

- **Hardware-Level Security**: Direct modification of Windows Registry for physical webcam control
- **Two-Factor Authentication**: Email-based OTP verification system
- **Modern GUI Interface**: Clean and intuitive interface built with Tkinter
- **Project Information Portal**: Built-in web view for project and developer details
- **Real-time Status Updates**: Visual feedback for all security operations

## 🛠️ Tech Stack

### Frontend
<img alt="Tkinter" src="https://img.shields.io/badge/Tkinter-3.x-blue?style=for-the-badge&logo=python&logoColor=white"/>

### Backend
<img alt="Python" src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img alt="smtplib" src="https://img.shields.io/badge/SMTP-Email-ff69b4?style=for-the-badge&logo=gmail&logoColor=white"/>
<img alt="Windows Registry" src="https://img.shields.io/badge/Windows%20Registry-0078D6?style=for-the-badge&logo=windows&logoColor=white"/>

### Libraries Used
<img alt="Pillow" src="https://img.shields.io/badge/Pillow-Image%20Processing-yellow?style=for-the-badge&logo=python&logoColor=white"/>

## 📁 Project Structure

```plaintext
Webcam_Spyware_Protection/
├── Web_Cam_Security.py    # Main application file
├── README.md              # Documentation
└── resources/             # Embedded resources
    └── icons/             # Application icons and images
```
---

## 🔄 How It Works

1. **Launch :**
  - User starts the application
2. **Select Action :**
  - Choose to Enable/Disable webcam
3. **Authentication :**
  - Enter email address
  - Receive OTP via email
  - Verify OTP
4. **Registry Modification :**
  - On successful verification, modifies Windows Registry
  - Updates webcam hardware access settings
5. **Status Update :**
  -Provides real-time feedback on operation status

---

## 🚀 Setup Instructions

### Prerequisites

- Windows Operating System
- Python 3.x installed
- Active Internet Connection
- SMTP Access (for email delivery)

### Installation

```bash
git clone https://github.com/hemanth-devzone/Webcam-Security-Tool.git
cd Webcam-Security-Tool
pip install pillow secure-smtplib
python Web_Cam_Security.py
```
---

## 🔐 Security Highlights

- Hardware-Level Control : Direct registry modification for physical device control.
- Two-Factor Authentication : Email-based OTP verification.
- Secure Communication : TLS/SSL encrypted email delivery.
- Error Handling : Comprehensive exception management and rollback capability.
- Access Logging : Records of all enable/disable attempts.

---

## 🔜 Future Improvements

- Implement OAuth 2.0 for email authentication.
- Add OTP expiration mechanism.
- Enhance UI/UX with modern themes.
- Develop cross-platform support.
- Add system tray integration.
- Implement automated security updates.

---

## 📝 License

This project is proprietary software developed during an internship at Supraja Technologies. All rights reserved.

---

## 👨‍💻 Author

<p align="center">Hemanth Kumar Reddy K</p>
<p align="center">Project developed during Cybersecurity Internship at Supraja Technologies.</p>

---

## 🙏 Acknowledgments

- Supraja Technologies for project guidance and support
- Python community for excellent documentation
- Open-source contributors for inspiration

---
## Note
This application requires administrator privileges for Registry modifications. Use with caution and always verify webcam status after operations.
<p align="center">Made with ❤️ by Hemanth Kumar Reddy</p>

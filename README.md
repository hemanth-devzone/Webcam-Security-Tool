# Webcam Spyware Protection Application

## Project Overview

A Python-based desktop security tool designed to prevent unauthorized webcam access by enforcing OTP (One-Time Password) verification through email. The app modifies system registry settings to physically enable or disable the webcam device, ensuring user control over privacy.

---

## Key Features

- Secure Webcam Enable/Disable Control
- Email OTP Authentication
- User-Friendly GUI using Tkinter
- Direct Hardware-Level Protection
- Project Information View

---

## Tech Stack

- **Frontend:**  
  <img alt="Tkinter" src="https://img.shields.io/badge/Tkinter-3.x-blue?style=for-the-badge&logo=python&logoColor=white"/>

- **Backend:**  
  <img alt="Python" src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="smtplib" src="https://img.shields.io/badge/SMTP-Email-ff69b4?style=for-the-badge&logo=gmail&logoColor=white"/>
  <img alt="Windows Registry" src="https://img.shields.io/badge/Windows%20Registry-0078D6?style=for-the-badge&logo=windows&logoColor=white"/>

- **Libraries Used:**  
  <img alt="Pillow" src="https://img.shields.io/badge/Pillow-Image%20Processing-yellow?style=for-the-badge&logo=python&logoColor=white"/>

---

## Project Structure

- `Web_Cam_Security.py` — Main Python application script
- `Web_Cam_Security.exe` — Optional executable version
- Pillow images/resources embedded dynamically

---

## How It Works

1. User selects to Enable or Disable webcam.
2. Application sends a randomly generated OTP to the user's email.
3. User verifies the action by entering the OTP.
4. On correct OTP:
   - Webcam is either enabled or disabled at the system level by updating Windows Registry entries.
5. Project and developer information can be viewed via a browser window inside the app.

---

## Setup Instructions

### Prerequisites

- Windows OS machine
- Python 3.x installed
- Internet connection for email OTP delivery

### Installation

```bash
git clone https://github.com/hemanthreddy100/Webcam_Spyware__Hemanth.git
cd Webcam_Spyware__Hemanth
pip install pillow
python Web_Cam_Security.py
```
---

## Security Highlights

- Ensures only authorized users can control webcam access.
- OTP authentication provides an extra layer of protection.
- Direct hardware registry modification prevents malware bypassing software-only protections.

---

## Future Improvements

- Secure credential storage or OAuth-based mailing.
- Adding OTP expiration times.
- Improved UI feedback for success/failure.
- Cross-platform support (Linux/macOS).

---

## Author

- **Developer:** Hemanth Reddy
- **GitHub:** [hemanthreddy100](https://github.com/hemanthreddy100)

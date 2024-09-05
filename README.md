# Web Cam Security Application

## Overview

This project is designed to enhance the security of organizations by preventing unauthorized access to webcams through spyware. It implements a Physical Security Policy on webcams in devices, ensuring that users can enable or disable their webcams securely using One-Time Passwords (OTPs).

## Features

- **Webcam Control**: Users can enable or disable their webcams.
- **OTP Verification**: Sends a One-Time Password (OTP) via email for secure actions.
- **User Interface**: A simple and user-friendly interface built using Tkinter.
- **Project Information**: Displays project details in a separate window.

## Technologies Used

- Python
- Tkinter (for GUI)
- Pillow (for image handling)
- smtplib (for sending emails)
- Temporary HTML file generation (for project information display)

## Installation

To run this application, you need to have Python installed on your machine. Additionally, install the required packages using the following command:

```bash
pip install pillow secure-smtplib


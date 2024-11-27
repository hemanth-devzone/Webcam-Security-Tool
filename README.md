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

## How It Works:

**User Interaction**: When the user clicks the button to enable or disable the webcam, they are prompted to enter their email.
**OTP Generation**: The application generates an OTP and sends it to the user's email.
**OTP Verification**: The user must input the OTP to proceed. Upon successful verification, the webcam is either enabled or disabled.
**Project Info**: The user can click a button to open a browser displaying detailed project information, including project, developer, and company details.

## Code Breakdown:

**Package Management**: The code first checks if the required packages (pillow, secure-smtplib) are installed, installing them if necessary.
**OTP Generation**: A random OTP is generated for each action (either enabling or disabling the webcam).
**Email Sending**: smtplib is used to send the OTP to the user’s email, providing an extra layer of security.
**Registry Commands**: The webcam status is controlled through Windows Registry commands. When the user verifies the OTP, a command is run to either enable or disable the webcam.
**GUI Elements**: The app is built using Tkinter with buttons to trigger actions (enable/disable webcam), and a separate window for OTP input.

## Security Features:

**Webcam Control via Registry**: Disables or enables the webcam by modifying registry entries.
**OTP Validation**: Ensures that only authorized users can make changes to webcam settings.

## Project Benefits:

**Security Enhancement**: Provides a simple but effective way to control webcam access, protecting against unauthorized spyware.
**User Control**: Users have the ability to securely control their webcam access without complex setups.

## Installation

To run this application, you need to have Python installed on your machine. Additionally, install the required packages using the following command:

```bash
pip install pillow secure-smtplib
```

This tool can be very beneficial for ensuring physical security against spyware, especially in organizational environments.

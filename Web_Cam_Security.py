import tkinter as tk
from tkinter import messagebox
import subprocess
import tempfile
import os
import webbrowser
from PIL import Image, ImageTk
import base64
from tkinter import Tk, PhotoImage
import io
import sys
import os
import pkg_resources
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Define the required packages for the code 
required_packages = ['pillow', 'secure-smtplib',]
# Check if each required package is installed, and install it if not
for package in required_packages:
    try:
        pkg_resources.get_distribution(package)
    except pkg_resources.DistributionNotFound:
        print(f"{package} is not installed. Installing...")
        subprocess.check_call(['pip', 'install', package])



#Replace the 'base64_icon' with your actual base64-encoded image
base64_icon = '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'

#convert the base64 string to bytes
icon_data = base64.b64decode(base64_icon)

# Create the main window
root = tk.Tk()

# Create a photoImage object from the bytes and set it as a window icon
icon_image = PhotoImage(data=icon_data)
root.iconphoto(True, icon_image)

# Set window properties
root.title("Web Cam Security")
root.geometry("600x500")
window_width = 600
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg='black')

# Create a frame for button
button_frame = tk.Frame(root, bg="black")

# Label to display success messages
success_label = tk.Label(button_frame, text="", font=("Arial", 12, "bold"), bg="black", fg="#ff0000")
success_label.pack(pady=10)

# OTP related functions
def generate_otp(length=6):
    digits = "0123456789"
    OTP = "".join(random.choice(digits) for _ in range(length))
    return OTP

def send_otp_via_email(otp, sender_email, sender_password, recipient_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    subject = "Your OTP Code"
    body = f"Your OTP code is: {otp}"
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"OTP sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send OTP. Error: {e}")

# Email credentials for sending OTPs
sender_email = "webcamspywareproject@gmail.com"
sender_password = "hjpy kuii smdh suie"

# Promote the user to enter their email and proceed with the specific actions
def get_email_and_proceed(action):
    email_window = tk.Toplevel(root)
    email_window.title("Enter Email")
    email_window.geometry("300x200")

    email_label = tk.Label(email_window, text="Enter Email")
    email_label.pack()

    email_entry = tk.Entry(email_window)
    email_entry.pack()
    email_entry.focus()
    
# Get the email and proceed with the action
    def proceed_with_email():
        recipient_email = email_entry.get()
        if recipient_email:
            email_window.destroy()
            action(recipient_email)
        else:
            messagebox.showerror("Error", "Please enter an email address.")

    def ok_button(event=None):
        proceed_with_email()

    email_entry.bind("<Return>", ok_button)

    ok_button = tk.Button(email_window, text="OK", command=proceed_with_email)
    ok_button.pack(pady=10)

    cancel_button = tk.Button(email_window, text="Cancel", command=email_window.destroy)
    cancel_button.pack(pady=10)

# Display project information in a web browser
def project_info():
    html_code = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }
        .container {
            width: 100%; 
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            box-sizing: border-box;
            background: #fff;
            border: 1px solid #ddd;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-top: 30px;
            min-height: 70px;
        }
        header h1 {
            text-align: left;
            text-transform: uppercase;
            margin: 0;
            font-size: 24px;
            text-decoration: underline;
        }
        header img {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            border: 1px solid #ddd;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);

        }
        .content {
            padding: 20px;
        }
        h2 {
            text-decoration: underline;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        .floating-paragraph {
            margin-bottom: 20px;
            padding: 10px;
            text-align: justify;
        }

        @media only screen and (max-width: 600px) {
            header img {
                width: 60px;
                height: 60px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Project Information</h1>
            <img src="https://media.licdn.com/dms/image/C560BAQF3H-o_kgtM7g/company-logo_200_200/0/1630672249915?e=2147483647&v=beta&t=oXt-V7ICTw6_yYhr1nJyuacvpKi_QSTA6TrJHafSZ8w" alt="Supraja Technologies Logo">
        </header>
        <div class="content">
            <p class="floating-paragraph">
                This project was developed by <b>K.Hemanth Kumar Reddy</b> as a part of <b>Cybersecurity Internship</b>.
                This project is designed to <b>secure organizations in the real world from cyber frauds performed by hackers.</b>
            </p>

            <h2>Project Details</h2>
            <table>
                <tr>
                    <th>Project Details</th>
                    <th>Value</th>
                </tr>
                <tr>
                    <td>Project Name</td>
                    <td>Web Cam Security from Spyware</td>
                </tr>
                <tr>
                    <td>Project Description</td>
                    <td>Implementing Physical Security Policy on Web Cam in Devices to Prevent Spyware Activities</td>
                </tr>
                <tr>
                    <td>Project Start Date</td>
                    <td>26-05-2024</td>
                </tr>
                <tr>
                    <td>Project End Date</td>
                    <td>29-06-2024</td>
                </tr>
                <tr>
                    <td>Project Status</td>
                    <td><b>Completed</b></td>
                </tr>
            </table>

            <h2>Developer Details</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Employee ID</th>
                    <th>Email</th>
                </tr>
                <tr>
                    <td>K.Hemanth Kumar Reddy</td>
                    <td>ST#IS#6406</td>
                    <td>hemanthgreat100@gmail.com</td>
                </tr>
            </table>

            <h2>Company Details</h2>
            <table>
                <tr>
                    <th>Company</th>
                    <th>Value</th>
                </tr>
                <tr>
                    <td>Name</td>
                    <td>Supraja Technologies</td>
                </tr>
                <tr>
                    <td>Email</td>
                    <td>contact@suprajatechnologies.com</td>
                </tr>
            </table>
        </div>
    </div>
</body>
</html>


    """
    # Save the HTML content to a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.html') as temp_file:
        temp_file.write(html_code)
        temp_file_path = temp_file.name

    # Open the temporary HTML file in the default web browser
    webbrowser.open('file://' + os.path.realpath(temp_file_path))


#Define the function to be executed when button is clicked and does OTP verification
def button1_clicked(recipient_email):
    otp = generate_otp()
    send_otp_via_email(otp, sender_email, sender_password, recipient_email)

    # Create a OTP prompt dialog box
    otp_window = tk.Toplevel(root)
    otp_window.title("Enter OTP")
    otp_window.geometry("300x200")

    otp_label = tk.Label(otp_window, text="Enter OTP")
    otp_label.pack()

    otp_entry = tk.Entry(otp_window, show="*")
    otp_entry.pack()
    otp_entry.focus()
    

# Verify the OTP and disable the webcam if correct
    def ok_button(event=None):
        if otp_entry.get() == otp:
            delete_cmd = r'REG DELETE "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /f'
            subprocess.run(delete_cmd, shell=True)
            add_cmd = r'REG ADD "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /t REG_DWORD /d 1 /f'
            subprocess.run(add_cmd, shell=True)
            otp_window.destroy()
            success_label.config(text="Camera Disabled Successfully")
        else:
            error_label.config(text="Incorrect OTP. Please try again.")
            otp_entry .delete(0, tk.END)

# Close the OTP window
    def cancel_button():
       otp_window.destroy()

    otp_entry.bind("<Return>", ok_button)
     

    ok_button = tk.Button(otp_window, text="OK", command=ok_button)
    ok_button.pack(padx=10, pady=10)

    cancel_button_widget = tk.Button(otp_window, text="Cancel", command=cancel_button)
    cancel_button_widget.pack(padx=10, pady=10)

    error_label = tk.Label(otp_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

    

#Define the function to execute when the second button is clicked and does OTP verification
def button2_clicked(recipient_email):
    otp = generate_otp()
    send_otp_via_email(otp, sender_email, sender_password, recipient_email)
   
    #create a OTP prompt dialog box
    otp_window = tk.Toplevel(root)
    otp_window.title("Enter OTP")
    otp_window.geometry("300x200")

    otp_lable = tk.Label(otp_window, text="Enter OTP")
    otp_lable.pack()

    otp_entry = tk.Entry(otp_window, show="*")
    otp_entry.pack()
    otp_entry.focus()
    
# Verify the OTP and disable the webcam if correct
    def ok_button(event=None):
       if otp_entry.get()== otp:
        command = r'REG DELETE "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\CapabilityAccessManager\ConsentStore\webcam" /v Value /f"'
        subprocess.call(command, shell=True)
        otp_window.destroy()
        success_label.config(text="camera Enabled Successfully")
       else:
        error_label.config(text="Incorrect OTP.please try again")
        otp_entry.delete(0, tk.END)

# Close the OTP window
    def cancel_button():
        otp_window.destroy()

    otp_entry.bind("<Return>", ok_button)

    ok_button = tk.Button(otp_window, text="OK", command = ok_button)
    ok_button.pack()

    cancel_button_widget = tk.Button(otp_window, text="Cancel", command=cancel_button)
    cancel_button_widget.pack(padx=10, pady=10)
  

    error_label = tk.Label(otp_window, text="", font=("Arial",12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

# Button to show Project information    
info_button = tk.Button(root, text="Project Info", font=("Arial", 14, "bold"), bg="red", fg="white", command=project_info)
info_button.pack(pady=10)

# Lable to display project title
project_label = tk.Label(root, text="Preventing Spyware!!!", font=("Arial", 18, "bold"), bg="black", fg="white")
project_label.pack(pady=25)




#set base64 string image as the background
background_image_base64 ='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'
background_image_data = base64.b64decode(background_image_base64)
background_image = Image.open(io.BytesIO(background_image_data))
background_image = background_image.resize((200,150), Image.Resampling.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.pack()

# Button to disable and enable the webcam
button1 = tk.Button(button_frame, text="Disable Camera", font=("Arial", 14, "bold"), padx=10, pady=5, command=lambda: get_email_and_proceed(button1_clicked), bg="red", fg="white")
button2 = tk.Button(button_frame, text="Enable Camera", font=("Arial", 14, "bold"), padx=12, pady=5, command=lambda: get_email_and_proceed(button2_clicked), bg="Green", fg="white")

button1.pack(pady=10)
button2.pack(pady=10)

button_frame.pack(expand=True)

# Run the application
root.mainloop()

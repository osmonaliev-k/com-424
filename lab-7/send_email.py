import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email():
    sender_email = "osmonaliev_k@auca.kg"  # Replace with your email
    receiver_email = "kubilay.osmonaliev@gmail.com"  # Replace with the server owner's email
    password = "K426275g"  # Replace with your email password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Cron Job Alert'
    
    body = 'This is a test email sent from a cron job to the server owner.'
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)  # Replace with your SMTP server and port
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_email()
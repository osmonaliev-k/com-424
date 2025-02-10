import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = "osmonaliev_k@auca.kg"  # Replace with your email address
sender_password = "K426275g"  # Replace with your email password or app-specific password
receiver_email = "kubilay.osmonaliev@gmail.com"  # Replace with the recipient's email

subject = "Payment Verification Required"
body = """
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Payment Verification</title>
</head>
<body>
   <h2>Payment Verification</h2>
   <p>Please verify your payment information by clicking the link below:</p>
   <a href="http://localhost:8000/verify">Click here to verify your payment</a>
</body>
</html>
"""

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "html"))

try:
   server = smtplib.SMTP(smtp_server, smtp_port)
   server.starttls()
   server.login(sender_email, sender_password)
   text = message.as_string()
   server.sendmail(sender_email, receiver_email, text)
   print("Email sent successfully!")
except Exception as e:
   print(f"Error sending email: {e}")
finally:
   server.quit()

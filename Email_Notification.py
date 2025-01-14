import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email):
    sender_email = "abida.mohammad.us@gmail.com"
    sender_password = "ctas ohve fiun hmxz"  # Use App Password for Gmail

    # Create the email content
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, to_email, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Send a test email
send_email(
    subject="Test email from my python code",
    body="This is a test email sent using Python!",
    to_email="abidabegam.mohammad@gmail.com"
)
send_email(
    subject="Test Email from Abida",
    body="This is a test email from my python code",
    to_email="anwar.mohammad.us@gmail.com"
)

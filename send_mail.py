import smtplib
from email.mime.text import MIMEText


def send_mail(country, name, email, org, organization, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '763e2aa28f60f0'
    password = 'b9fd9cd6db9868'
    message = f"<h3>New Feedback Submission</h3><ul><li>Country: {country}</li><li>Name: {name}</li><li>Email: {email}</li><li>Organization: {org}</li><li>Organization Type: {organization}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

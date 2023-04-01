import EmailSender as es

# Creates EmailSender object.
email_sender = es.EmailSender(
    smtp_host="smtp.gmail.com",
    smtp_port=587,
    username='<SENDER_EMAIL>@gmail.com',
    password='<YOUR_APP_PASSWORD>', # NOT your ordinary sign-in password; look at README.md.
    recipients=["recipient2@example.com", "recipient2@example.com"]
)

# Prepare message.
message = email_sender.create_message(subject="Test", 
                                      html_content= '''
                                      <h1>Hello World!</h1>
                                      <p>This is an email from Python.</p>
                                      ''')
# Send message.
email_sender.send_email(message)

print("Program terminated.")


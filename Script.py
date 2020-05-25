import pandas as pd
import smtplib

e = pd.read_excel("Enter the path of excel file")
emails = e['Emails'].values

# Enter the SMTP for the account you are usin
server = smtplib.SMTP("smtp-mail.outlook.com", 587) # If hotmail is used, use the SMTP for hotmail.
server.starttls()
server.login("Email ID", "password")
msg = "Enter the message to be sent"
subject = "Enter the subject for the email "
body = "Subject: {}\n\n{}".format(subject, msg)

for email in emails:
    server.sendmail("Email ID", email, body)
server.quit()
